import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


def callbacks(app):
    @app.callback(
        Output("home-modal", "opened"),
        Input("home-modal-button", "n_clicks"),
        State("home-modal", "opened"),
        prevent_initial_call=True,
    )
    def toggle_modal(n_clicks, opened):
        return not opened
