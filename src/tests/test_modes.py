"""Pytest stubs for optimisation mode workflows."""
from __future__ import annotations

from core.emissions_mode import run_emissions_mode
from core.lcoe_mode import run_lcoe_mode
from core.reliability_engine import ReliabilityEngine


def _build_config() -> dict:
    return {
        "preset": {"mode": "emissions"},
        "run_validation": False,
    }


def test_run_emissions_mode_returns_results() -> None:
    """Emissions mode should return a results dictionary."""
    config = _build_config()
    engine = ReliabilityEngine()
    results = run_emissions_mode(config, engine)
    assert results["mode"] == "emissions"


def test_run_lcoe_mode_returns_results() -> None:
    """LCOE mode should return a results dictionary."""
    config = _build_config()
    config["preset"]["mode"] = "lcoe"
    engine = ReliabilityEngine()
    results = run_lcoe_mode(config, engine)
    assert results["mode"] == "lcoe"
