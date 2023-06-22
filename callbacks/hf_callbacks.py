from dash.dependencies import Input, Output
from data import visualization as vis


def register_header_callbacks(app):
    @app.callback(
        Output("selected-crop", "children"),
        [Input("crops-dropdown", "value")]
    )
    def get_selected_crop(value):
        vis.select_data(value)
        return value
