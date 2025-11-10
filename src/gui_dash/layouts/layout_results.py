"""Dash layout definition for optimisation results tab."""
from __future__ import annotations

from dash import dcc, html

layout_results = html.Div([
    html.H2("Optimisation Results"),
    html.P("Review dispatch, cost, and emissions performance metrics."),
    dcc.Graph(id="dispatch-graph"),
    dcc.Graph(id="cost-graph"),
    dcc.Graph(id="emissions-graph"),
])
