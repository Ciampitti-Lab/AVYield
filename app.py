import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from config import config
from components import hf
from callbacks import register

app = Dash(
    config.dash.app_title,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        getattr(dbc.themes, config.dash.theme), "styles.css"],
)

app.title = config.dash.app_title
app._favicon = favicon = config.template.fa_logo_src

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        hf.header,
        html.Div(id='page-content'),
        hf.footer,
    ],
)

register.main_callbacks(app)
register.data_callbacks(app)
register.compare_callbacks(app)
register.home_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
