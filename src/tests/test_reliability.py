"""Pytest stubs for reliability engine functionality."""
from __future__ import annotations

from core.reliability_engine import ReliabilityEngine


def test_reliability_engine_initialisation() -> None:
    """Ensure the reliability engine can be instantiated and configured."""
    engine = ReliabilityEngine()
    engine.configure({"target": 0.999})
    availability = engine.evaluate_availability({})
    assert "system_availability" in availability
