from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import os
from flask import send_from_directory
from config import config
from components import controls
from register import main, data, overview, compare, control, home

app = Dash(
    config.dash.app_title,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        getattr(dbc.themes, config.dash.theme), "styles.css"],
)

server = app.server

app.title = config.dash.app_title
app._favicon = favicon = config.template.logo_src

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        controls.sidebar,
        html.Div(id="page-content"),
    ],
)


# Serve sitemap.xml
@server.route("/sitemap.xml")
def serve_sitemap():
    return send_from_directory(os.getcwd(), "sitemap.xml")


main.callbacks(app)
data.callbacks(app)
overview.callbacks(app)
compare.callbacks(app)
control.callbacks(app)
home.callbacks(app)

if __name__ == "__main__":
    # app.run_server(host='0.0.0.0', port=8050) # local-host
    # app.run_server(debug=True)
    app.run_server(debug=True, host="0.0.0.0", port=8080,
                   use_reloader=False)  # Docker
