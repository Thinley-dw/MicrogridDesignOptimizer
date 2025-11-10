"""Emissions-optimised mode heuristic for microgrid design."""
from __future__ import annotations

from typing import Any, Dict

from core.dispatch_simulator import simulate_dispatch
from core.reliability_engine import ReliabilityEngine
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def run_emissions_mode(config: Dict[str, Any], reliability_engine: ReliabilityEngine) -> Dict[str, Any]:
    """Execute emissions-first optimisation workflow.

    Args:
        config: Parsed configuration dictionary containing presets and data.
        reliability_engine: Shared reliability engine instance.

    Returns:
        Dictionary with optimisation results to feed into downstream modules.
    """
    LOGGER.info("Starting emissions-optimised mode")
    # TODO: Implement emissions-focused sizing and dispatch scheduling.
    dispatch_results = simulate_dispatch(config, strategy="emissions")
    # TODO: Integrate reliability adjustments using `reliability_engine`.
    results: Dict[str, Any] = {
        "mode": "emissions",
        "dispatch": dispatch_results,
        "config": config,
    }
    return results
