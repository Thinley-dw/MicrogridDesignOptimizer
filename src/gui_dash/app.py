"""
Dash GUI entrypoint.
Tabs: Inputs | Results | Validation
"""
from dash import Dash, html, dcc
from gui_dash.callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True, title="Microgrid Design Optimizer")

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='inputs', children=[
        dcc.Tab(label='Inputs', value='inputs'),
        dcc.Tab(label='Results', value='results'),
        dcc.Tab(label='Validation', value='validation')
    ]),
    html.Div(id='tabs-content')
])

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
