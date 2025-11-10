"""Dash layout definition for input configuration tab."""
from __future__ import annotations

from dash import dcc, html

layout_inputs = html.Div([
    html.H2("Configuration Inputs"),
    html.P("Upload or edit microgrid configuration parameters."),
    dcc.Upload(
        id="upload-config",
        children=html.Div(["Drag and Drop or Select Files"]),
        multiple=False,
    ),
    html.Div(id="config-preview"),
])
