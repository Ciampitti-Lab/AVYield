import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from config import config
from components import controls
import register

app = Dash(
    config.dash.app_title,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        getattr(dbc.themes, config.dash.theme), "styles.css"],
)

app.title = config.dash.app_title
app._favicon = favicon = config.template.logo_src

CONTENT_STYLE = {
    "margin-left": "12rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        controls.sidebar,
        html.Div(id='page-content', style=CONTENT_STYLE),
        controls.footer,
    ],
)

register.main_callbacks(app)
register.data_callbacks(app)
register.compare_callbacks(app)
register.control_callbacks(app)
register.home_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
