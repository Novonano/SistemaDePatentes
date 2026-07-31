"""
Orquestrador do fluxo de busca, avaliação e relatório.
"""

import json
import hashlib
import logging
import os
import re
import time
from datetime import datetime
from typing import Callable, Dict, List, Tuple

from analysis_utils import (
    COMPARATIVE_ANALYSIS_NO_INPUT,
    has_substantive_comparative_analysis,
)
import config
from evaluator.llm_evaluator import OllamaEvaluator
from logging_utils import log_event
from models.patent import Patent, PatentEvaluation
from pipeline.features import PipelineFeatures
from pipeline.memory import MemorySidecar
from pipeline.orchestrator_observers import build_default_observers
from pipeline.observers import (
    ErrorEvent,
    EventBus,
    Observer,
    PatentEvent,
    PipelineEvent,
    ProgressEvent,
    StageEvent,
)
from pipeline.router import ThemeRouter
from pipeline.state import RunState
from pipeline.protocol import build_review_protocol
from report.generator import ReportGenerator
from scraper.base import BaseScraper
from scraper.epo import EPOScraper
from scraper.google_patents import GooglePatentsScraper
from scraper.patentscope import PatentscopeScraper

logger = logging.getLogger(__name__)


class RunStateStore:
    """Persiste o estado incremental da execução em disco."""

    def __init__(self, output_dir: str, run_id: str):
        self.output_dir = output_dir
        self.state_path = os.path.join(output_dir, f"run_state_{run_id}.json")
        self.latest_path = os.path.join(output_dir, "run_state_latest.json")
        os.makedirs(self.output_dir, exist_ok=True)

    def save(self, state: RunState) -> None:
        """Escreve a versão atual do estado em arquivos JSON."""
        payload = state.to_dict()

        for path in (self.state_path, self.latest_path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)

    def save_artifact(self, filename: str, payload: dict) -> str:
        """Salva um artefato JSON auxiliar."""
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        return path


def print_banner() -> None:
    """Emite evento de inicialização do agente."""
    log_event(
        logger,
        logging.INFO,
        "agent_startup",
        component="patent-agent",
        description="Agente de Web Scraping de Patentes",
    )


def print_progress(step: str, current: int = 0, total: int = 0) -> None:
    """Emite progresso como log estruturado."""
    if total > 0:
        percent = round((current / total) * 100, 1) if total else 0.0
        log_event(
            logger,
            logging.INFO if current == total else logging.DEBUG,
            "progress",
            step=step,
            current=current,
            total=total,
            percent=percent,
        )
    else:
        log_event(
            logger,
            logging.INFO,
            "progress",
            step=step,
        )


def _log_stage(stage: str, title: str, level: int = logging.INFO, **fields: object) -> None:
    """Emite transições de etapa do pipeline."""
    log_event(
        logger,
        level,
        "stage_transition",
        stage=stage,
        title=title,
        **fields,
    )


def _normalize_text(value: str) -> str:
    """Normaliza texto para deduplicação."""
    return re.sub(r"\s+", " ", (value or "").strip()).lower()


def _normalize_patent_id(value: str) -> str:
    """Normaliza identificadores de patente e números de publicação."""
    return re.sub(r"[^A-Z0-9]", "", (value or "").upper())


def _record_id_from_key(key: str) -> str:
    """Gera identificador interno estável para a execução."""
    digest = hashlib.sha1((key or "record").encode("utf-8")).hexdigest()[:12]
    return f"rec_{digest}"


def _display_patent_id(patent: Patent) -> str:
    """Retorna o melhor identificador legível para humanos."""
    return patent.patent_id or patent.record_id or "N/A"


def _identity_key(patent: Patent) -> Tuple[str, str]:
    """Gera uma chave estável de identidade e informa sua base."""
    pid = _normalize_patent_id(patent.patent_id)
    if pid:
        return f"id:{pid}", "patent_id"

    if patent.url:
        url = patent.url.split("#", 1)[0].split("?", 1)[0].strip().lower()
        if url:
            return f"url:{url}", "url"

    title = _normalize_text(patent.title)
    if title:
        return f"title:{title}", "title"

    content_seed = {
        "abstract": _normalize_text(patent.abstract),
        "snippet": _normalize_text(patent.snippet),
        "assignee": _normalize_text(patent.assignee),
        "publication_date": _normalize_text(patent.publication_date),
        "filing_date": _normalize_text(patent.filing_date),
    }
    if any(content_seed.values()):
        encoded = json.dumps(content_seed, sort_keys=True, ensure_ascii=False).encode("utf-8")
        return f"content:{hashlib.sha1(encoded).hexdigest()}", "content"

    fallback_seed = {
        "source": _normalize_text(patent.source),
        "inventors": [_normalize_text(item) for item in patent.inventors],
        "url": patent.url.strip().lower(),
    }
    encoded = json.dumps(fallback_seed, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return f"fallback:{hashlib.sha1(encoded).hexdigest()}", "fallback"


def _family_key(patent: Patent) -> str:
    """Gera uma assinatura conservadora de família para dedupe inter-publicação."""
    title = _normalize_text(patent.title)
    assignee = _normalize_text(patent.assignee)
    inventor = _normalize_text(patent.inventors[0]) if patent.inventors else ""
    year_match = re.search(r"(19|20)\d{2}", patent.filing_date or patent.publication_date or "")
    year = year_match.group(0) if year_match else ""

    if title and ((assignee and year) or (inventor and year) or (assignee and inventor)):
        payload = {
            "title": title,
            "assignee": assignee,
            "inventor": inventor,
            "year": year,
        }
        encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
        return f"family:{hashlib.sha1(encoded).hexdigest()}"
    return ""


def _entity_key(record_id: str, patent_id: str) -> str:
    """Resolve a chave interna preferencial de patente/avaliação."""
    return record_id or _normalize_patent_id(patent_id) or patent_id or ""


def _evaluation_map(evaluations: List[PatentEvaluation]) -> Dict[str, PatentEvaluation]:
    """Indexa avaliações pela chave interna estável."""
    return {
        _entity_key(evaluation.record_id, evaluation.patent_id): evaluation
        for evaluation in evaluations
        if _entity_key(evaluation.record_id, evaluation.patent_id)
    }


def _pair_patents_with_evaluations(
    patents: List[Patent],
    evaluations: List[PatentEvaluation],
) -> List[Tuple[Patent, PatentEvaluation]]:
    """Relaciona patentes e avaliações por record_id, não pela ordem da lista."""
    eval_map = _evaluation_map(evaluations)
    pairs: List[Tuple[Patent, PatentEvaluation]] = []
    for patent in patents:
        key = _entity_key(patent.record_id, patent.patent_id)
        evaluation = eval_map.get(key)
        if evaluation is not None:
            pairs.append((patent, evaluation))
    return pairs


def _build_config_snapshot(
    query: str,
    max_results: int,
    model: str,
    output_dir: str,
    features: PipelineFeatures,
) -> Dict[str, object]:
    """Monta um snapshot estável da configuração da execução."""
    return {
        "pipeline_version": "1.1",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "query": query,
        "max_results": max_results,
        "model": model,
        "output_dir": output_dir,
        "feature_flags": features.to_dict(),
        "thresholds": {
            "include": config.SCREEN_INCLUDE_THRESHOLD,
            "review": config.SCREEN_REVIEW_THRESHOLD,
            "manual_review_limit": config.SCREEN_MAX_ITEMS_FOR_REVIEW,
        },
        "runtime": {
            "ollama_base_url": config.OLLAMA_BASE_URL,
            "ollama_timeout": config.OLLAMA_TIMEOUT,
        },
        "sources": [
            "Google Patents",
            "Patentscope",
        ],
    }


def _hash_snapshot(snapshot: Dict[str, object]) -> str:
    """Calcula hash estável do snapshot."""
    encoded = json.dumps(snapshot, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _merge_patents(base: Patent, incoming: Patent) -> Patent:
    """Combina campos não vazios de duas versões da mesma patente."""
    if not base.record_id and incoming.record_id:
        base.record_id = incoming.record_id
    if not base.family_id and incoming.family_id:
        base.family_id = incoming.family_id
    if not base.title and incoming.title:
        base.title = incoming.title
    if not base.abstract and incoming.abstract:
        base.abstract = incoming.abstract
    if not base.assignee and incoming.assignee:
        base.assignee = incoming.assignee
    if not base.filing_date and incoming.filing_date:
        base.filing_date = incoming.filing_date
    if not base.publication_date and incoming.publication_date:
        base.publication_date = incoming.publication_date
    if not base.url and incoming.url:
        base.url = incoming.url
    if not base.snippet and incoming.snippet:
        base.snippet = incoming.snippet
    if incoming.source:
        if not base.source:
            base.source = incoming.source
        elif incoming.source not in base.source:
            base.source = f"{base.source}; {incoming.source}"

    for inventor in incoming.inventors:
        if inventor not in base.inventors:
            base.inventors.append(inventor)

    return base


def _dedupe_patents(patents: List[Patent]) -> Tuple[List[Patent], Dict[str, int]]:
    """Remove duplicatas mantendo a melhor versão de cada patente."""
    deduped: Dict[str, Patent] = {}
    stats = {
        "records_with_content_identity": 0,
        "records_with_fallback_identity": 0,
        "family_duplicates_removed": 0,
    }

    for patent in patents:
        key, basis = _identity_key(patent)
        patent.record_id = _record_id_from_key(key)

        if key in deduped:
            deduped[key] = _merge_patents(deduped[key], patent)
        else:
            deduped[key] = patent
            if basis == "content":
                stats["records_with_content_identity"] += 1
            elif basis == "fallback":
                stats["records_with_fallback_identity"] += 1

    family_deduped: Dict[str, Patent] = {}
    for patent in deduped.values():
        family_key = _family_key(patent)
        if family_key:
            patent.family_id = family_key
            patent.record_id = _record_id_from_key(family_key)
        else:
            patent.family_id = ""

        merge_key = family_key or f"record:{patent.record_id}"
        if merge_key in family_deduped:
            family_deduped[merge_key] = _merge_patents(family_deduped[merge_key], patent)
            if family_key:
                stats["family_duplicates_removed"] += 1
        else:
            family_deduped[merge_key] = patent

    return list(family_deduped.values()), stats


def _build_manual_review_queue(
    patents: List[Patent],
    evaluations: List[PatentEvaluation],
    limit: int,
) -> Tuple[List[Dict[str, object]], int]:
    """Constrói um contrato explícito para a fila de revisão manual."""
    queue_candidates: List[Dict[str, object]] = []
    for patent, evaluation in _pair_patents_with_evaluations(patents, evaluations):
        if not (evaluation.manual_review_required or evaluation.screening_decision == "review" or evaluation.llm_error):
            continue
        queue_candidates.append({
            "record_id": patent.record_id,
            "patent_id": patent.patent_id,
            "family_id": patent.family_id,
            "title": patent.title,
            "reason": evaluation.route_reason or evaluation.screening_reason,
            "route": evaluation.analysis_route,
            "screening_score": evaluation.screening_score,
            "screening_decision": evaluation.screening_decision,
            "llm_error": evaluation.llm_error,
        })

    queue_candidates.sort(
        key=lambda item: (
            0 if item.get("llm_error") else 1,
            -(item.get("screening_score") or 0),
            item.get("title") or "",
        )
    )
    limited = queue_candidates[:limit]
    deferred = max(len(queue_candidates) - len(limited), 0)
    return limited, deferred


def _cluster_label(patent: Patent, evaluation: PatentEvaluation) -> str:
    """Atribui um cluster temático determinístico."""
    text = " ".join([
        patent.title,
        patent.abstract,
        patent.snippet,
        evaluation.summary,
        evaluation.technical_domain,
    ]).lower()

    rules = [
        ("CO2 Cycle Configurations", ["cycle", "transcritical", "ejector", "economizer", "compressor", "cop"]),
        ("CO2 Phase Properties", ["phase", "triple point", "critical point", "property"]),
        ("Cryogenic Energy Systems", ["cryogenic", "liquid air", "laes", "cold storage", "boil-off"]),
        ("Phase Change Materials", ["pcm", "phase change", "latent heat", "encapsulat"]),
        ("Thermal Transfer Mechanisms", ["boiling", "condensation", "heat transfer", "nucleate"]),
        ("Economic Optimization", ["economic", "cost", "tariff", "optimization", "arbitrage"]),
        ("Solid CO2 Storage", ["solid co2", "dry ice", "sublim"]),
    ]

    for label, keywords in rules:
        if any(keyword in text for keyword in keywords):
            return label

    if evaluation.technical_domain:
        return evaluation.technical_domain
    return "General / Other"


def _prisma_stage_artifact(state: RunState, counts: Dict[str, int]) -> Dict[str, object]:
    """Monta um artefato PRISMA-like para o relatório e o estado."""
    return {
        "flow": {
            "identification": {
                "raw_records": counts.get("raw_scraped", 0),
                "unique_records": counts.get("unique_patents", 0),
                "duplicates_removed": counts.get("duplicates_removed", 0),
            },
            "screening": {
                "screened": counts.get("screened", 0),
                "included": counts.get("included", 0),
                "review": counts.get("review", 0),
                "excluded": counts.get("excluded", 0),
            },
            "eligibility": {
                "full_extractions": counts.get("full_extractions", 0),
                "manual_review_required": counts.get("manual_review_required", 0),
                "manual_review_deferred": counts.get("manual_review_deferred", 0),
            },
            "coverage": {
                "missing_abstract": counts.get("missing_abstract", 0),
                "missing_id": counts.get("missing_id", 0),
            },
            "synthesis": {
                "analyzed_records": counts.get("full_extractions", 0),
                "comparative_analysis_generated": has_substantive_comparative_analysis(
                    state.comparative_analysis
                ),
            },
        },
        "criteria": state.protocol.get("criteria", {}),
        "thresholds": state.protocol.get("thresholds", {}),
        "version": state.protocol.get("version", ""),
    }


def _build_top_patents(patents: List[Patent], evaluations: List[PatentEvaluation], limit: int = 5) -> List[Dict[str, object]]:
    """Seleciona as patentes mais relevantes para o contexto compartilhado."""
    paired = [
        (patent, evaluation)
        for patent, evaluation in _pair_patents_with_evaluations(patents, evaluations)
        if evaluation.screening_decision == "include" and not evaluation.llm_error
    ]
    paired.sort(key=lambda item: item[1].relevance_score, reverse=True)
    top = []
    for patent, evaluation in paired[:limit]:
        top.append({
            "record_id": patent.record_id,
            "family_id": patent.family_id,
            "patent_id": patent.patent_id,
            "title": patent.title,
            "score": evaluation.relevance_score,
            "screening_decision": evaluation.screening_decision,
            "thematic_cluster": evaluation.thematic_cluster,
            "route": evaluation.analysis_route,
            "evidence_snippets": evaluation.evidence_snippets[:2],
        })
    return top


def _build_route_summary(evaluations: List[PatentEvaluation]) -> Dict[str, int]:
    """Agrega estatísticas de roteamento por tipo de análise."""
    summary: Dict[str, int] = {}
    for evaluation in evaluations:
        route = evaluation.analysis_route or "unrouted"
        summary[route] = summary.get(route, 0) + 1
    return summary


def _count_diagnostic_kinds(items: List[Dict[str, object]]) -> Dict[str, int]:
    """Conta diagnósticos por tipo."""
    counts: Dict[str, int] = {}
    for item in items:
        kind = item.get("kind", "unknown") or "unknown"
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def _build_observability_metrics(state: RunState) -> Dict[str, object]:
    """Expande métricas de observabilidade por rota, fonte e falha."""
    route_metrics: Dict[str, Dict[str, object]] = {}
    for evaluation in state.evaluations:
        route = evaluation.analysis_route or "unrouted"
        bucket = route_metrics.setdefault(route, {
            "count": 0,
            "include": 0,
            "review": 0,
            "exclude": 0,
            "llm_errors": 0,
        })
        bucket["count"] += 1
        decision = (evaluation.screening_decision or "unknown").lower()
        if decision in {"include", "review", "exclude"}:
            bucket[decision] += 1
        if evaluation.llm_error:
            bucket["llm_errors"] += 1

    source_metrics: Dict[str, Dict[str, object]] = {}
    for source_name, raw_results in state.patents_by_source.items():
        diagnostics = state.scraper_diagnostics.get(source_name, [])
        source_metrics[source_name] = {
            "raw_results": raw_results,
            "duration_seconds": round(float(state.scraper_durations.get(source_name, 0) or 0), 3),
            "diagnostic_counts": _count_diagnostic_kinds(diagnostics),
        }

    llm_by_operation: Dict[str, Dict[str, int]] = {}
    for operation, metric in state.llm_telemetry.get("operations", {}).items():
        llm_by_operation[operation] = {
            "calls": int(metric.get("calls", 0) or 0),
            "failures": int(metric.get("failures", 0) or 0),
            "retries": int(metric.get("retries", 0) or 0),
            "degraded_skips": int(metric.get("degraded_skips", 0) or 0),
        }

    scraper_failure_counts: Dict[str, int] = {}
    for items in state.scraper_diagnostics.values():
        for kind, count in _count_diagnostic_kinds(items).items():
            scraper_failure_counts[kind] = scraper_failure_counts.get(kind, 0) + count

    failure_metrics = {
        "run_errors": len(state.errors),
        "records_with_llm_error": sum(1 for evaluation in state.evaluations if evaluation.llm_error),
        "llm_total_failures": int(state.llm_telemetry.get("total_failures", 0) or 0),
        "llm_by_operation": llm_by_operation,
        "scraper_diagnostics_by_kind": scraper_failure_counts,
    }

    return {
        "routes": dict(sorted(route_metrics.items(), key=lambda item: (-item[1]["count"], item[0]))),
        "sources": dict(sorted(source_metrics.items())),
        "failures": failure_metrics,
    }


def _build_writing_context(state: RunState) -> Dict[str, object]:
    """Compacta o estado para consumo do writer/relatório."""
    return {
        "protocol": state.protocol,
        "coverage_metrics": state.coverage_metrics,
        "top_patents": _build_top_patents(state.patents, state.evaluations),
        "thematic_clusters": state.thematic_clusters,
        "route_summary": _build_route_summary(state.evaluations),
        "feature_flags": state.feature_flags,
        "snapshot_hash": state.snapshot_hash,
    }


def _record_stage_metric(
    state: RunState,
    stage: str,
    start_time: float,
    end_time: float,
    status: str,
    items_processed: int = 0,
    detail: str = "",
) -> None:
    """Registra métricas estruturadas de etapa e loga a transição."""
    metric = {
        "stage": stage,
        "status": status,
        "duration_seconds": round(end_time - start_time, 3),
        "items_processed": items_processed,
        "detail": detail,
    }
    state.stage_metrics.append(metric)
    log_event(
        logger,
        logging.INFO,
        "stage_metric",
        stage=stage,
        status=status,
        duration_seconds=metric["duration_seconds"],
        items_processed=items_processed,
        detail=detail,
    )


def _build_thematic_clusters(
    patents: List[Patent],
    evaluations: List[PatentEvaluation],
) -> Dict[str, object]:
    """Agrupa patentes em clusters temáticos para síntese."""
    clusters: Dict[str, Dict[str, object]] = {}

    for patent, evaluation in _pair_patents_with_evaluations(patents, evaluations):
        if evaluation.screening_decision != "include" or evaluation.llm_error:
            continue

        label = _cluster_label(patent, evaluation)
        evaluation.thematic_cluster = label

        cluster = clusters.setdefault(label, {
            "cluster": label,
            "count": 0,
            "patent_ids": [],
            "titles": [],
            "average_score": 0.0,
            "average_confidence": 0.0,
            "evidence_count": 0,
            "top_patents": [],
            "summary": "",
        })
        cluster["count"] += 1
        cluster.setdefault("record_ids", []).append(patent.record_id)
        cluster["patent_ids"].append(patent.patent_id)
        cluster["titles"].append(patent.title)
        cluster["average_score"] += evaluation.relevance_score
        cluster["average_confidence"] += evaluation.confidence
        cluster["evidence_count"] += len(evaluation.evidence_snippets)

    for cluster in clusters.values():
        count = cluster["count"] or 1
        cluster["average_score"] = round(cluster["average_score"] / count, 2)
        cluster["average_confidence"] = round(cluster["average_confidence"] / count, 2)

    return {
        "clusters": sorted(
            clusters.values(),
            key=lambda item: (item["count"], item["average_score"]),
            reverse=True,
        ),
        "total_clusters": len(clusters),
    }



def run_agent(
    query: str,
    max_results: int,
    model: str,
    output_dir: str,
    features: PipelineFeatures | None = None,
    scrapers: List[BaseScraper] | None = None,
    evaluator_factory: Callable[..., OllamaEvaluator] | None = None,
    state_sink: Callable | None = None,
    observers: "List[Observer] | None" = None,
) -> RunState:
    """Fachada fina que delega para ``PipelineOrchestrator``.

    Mantem a assinatura historica para todos os callers (api, main, ablation,
    upgrade_benchmark, test_frozen_pipeline). A implementacao real dos
    estagios vive em ``pipeline.pipeline_orchestrator``.

    ``observers`` permite injetar observers customizados no barramento
    da execucao. Quando ``None``, apenas o conjunto default e usado; quando
    fornecido, os observers extras sao inscritos apos os default.

    A fachada atua como composition root e
    monta o conjunto de observers via ``build_default_observers``, repassando
    um ``observers_builder`` ao ``PipelineOrchestrator``. A classe deixa de
    conhecer a fabrica concreta.
    """
    from pipeline.orchestrator_observers import build_default_observers
    from pipeline.observers import Observer
    from pipeline.pipeline_orchestrator import PipelineOrchestrator

    extras = list(observers) if observers else []

    def _build_ctx_observers(state, store, memory):
        defaults = build_default_observers(
            state,
            store,
            memory,
            logger,
            print_progress,
            include_memory=False,
            include_persistence=False,
        )
        return defaults + extras

    return PipelineOrchestrator(
        query=query,
        max_results=max_results,
        model=model,
        output_dir=output_dir,
        features=features,
        scrapers=scrapers,
        evaluator_factory=evaluator_factory,
        state_sink=state_sink,
        observers_builder=_build_ctx_observers,
    ).run()
