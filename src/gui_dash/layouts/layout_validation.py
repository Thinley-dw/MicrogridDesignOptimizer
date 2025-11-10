"""Dash layout definition for Monte Carlo validation tab."""
from __future__ import annotations

from dash import html

layout_validation = html.Div([
    html.H2("Reliability Validation"),
    html.P("Run Monte Carlo simulations to verify availability targets."),
    html.Button("Run Validation", id="run-validation", n_clicks=0),
    html.Div(id="validation-status"),
])
