from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from config import config
from components import hf
from callbacks import hf_callback

app = Dash(
    config.dash.app_title,

    external_stylesheets=[getattr(dbc.themes, config.dash.theme), "styles.css"])

app.layout = html.Div(
    [
        hf.header,
        hf.footer,
    ]
)

hf_callback.register_header_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
