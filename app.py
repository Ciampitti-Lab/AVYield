from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from db import get_config
from components import controls
import register

app = Dash(
    get_config('dash', 'app_title'),
    suppress_callback_exceptions=True,
    external_stylesheets=[
        getattr(dbc.themes, get_config('dash', 'theme')), "styles.css"],
)
server = app.server

app.title = get_config('dash', 'app_title')
app._favicon = favicon = get_config('template', 'logo_src')

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
