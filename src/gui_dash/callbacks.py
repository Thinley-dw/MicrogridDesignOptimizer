"""Defines Dash callbacks linking GUI to optimisation backend."""
from __future__ import annotations

from dash import Input, Output
from src.main import main


def register_callbacks(app) -> None:
    """Register Dash callbacks with the given app instance."""

    @app.callback(Output('tabs-content','children'),
                  Input('tabs','value'))
    def render_tab(tab):
        if tab == 'inputs':
            from gui_dash.layouts.layout_inputs import layout_inputs
            return layout_inputs
        elif tab == 'results':
            from gui_dash.layouts.layout_results import layout_results
            return layout_results
        else:
            from gui_dash.layouts.layout_validation import layout_validation
            return layout_validation

    # TODO: Add callbacks linking GUI interactions to backend execution via `main`.
