"""Pytest stubs for layout and BOS evaluation."""
from __future__ import annotations

from core.layout_bos import evaluate_layout


def test_evaluate_layout_inserts_layout_key() -> None:
    """Layout evaluation should append a layout entry to results."""
    results = {"economics": {}}
    layout = evaluate_layout(results)
    assert "layout" in layout
