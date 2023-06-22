import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from config import config
from components import hf
from callbacks import hf_callbacks, main_callbacks

app = Dash(
    config.dash.app_title,
    external_stylesheets=[
        getattr(dbc.themes, config.dash.theme), "styles.css"],
)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        hf.header,
        html.Div(id='page-content'),
        hf.footer,
    ],
)

hf_callbacks.register_header_callbacks(app)
main_callbacks.register_main_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
