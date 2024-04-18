from dash.dependencies import Input, Output


def callbacks(app):
    # Update sidebar options color based on curr page
    @app.callback(
        Output("sidebar-home", "active"),
        Output("sidebar-home", "color"),
        Output("sidebar-overview", "active"),
        Output("sidebar-overview", "color"),
        Output("sidebar-compare", "active"),
        Output("sidebar-compare", "color"),
        Output("sidebar-data", "active"),
        Output("sidebar-data", "color"),
        Output("sidebar-about", "active"),
        Output("sidebar-about", "color"),
        Input("url", "pathname"),
    )
    def update_sidebar_color(pathname):
        if pathname == "/":
            return True, "purple", False, "black", False, "black", False, "black", False, "black"
        elif pathname == "/overview":
            return False, "black", True, "purple", False, "black", False, "black", False, "black"
        elif pathname == "/compare":
            return False, "black", False, "black", True, "purple", False, "black", False, "black"
        elif pathname == "/data":
            return False, "black", False, "black", False, "black", True, "purple", False, "black"
        elif pathname == "/about":
            return False, "black", False, "black", False, "black", False, "black", True, "purple"
