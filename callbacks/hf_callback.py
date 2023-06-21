from dash.dependencies import Input, Output


def register_header_callbacks(app):
    @app.callback(
        Output("selected-university", "children"),
        [Input("uni-dropdown", "value")]
    )
    def get_selected_uni(value):
        return print(value)
