from dash.dependencies import Input, Output
from components import home, compare, data, about, controls


def callbacks(app):
    # Update page Index
    @app.callback(Output("page-content", "children"), Input("url", "pathname"))
    def display_page(pathname):
        if pathname == "/":
            return [home.layout, controls.footer]
        elif pathname == "/compare":
            return [compare.layout, controls.footer]
        elif pathname == "/data":
            return [data.layout, controls.footer]
        elif pathname == "/about":
            return [about.layout, controls.footer]
        else:
            return home.layout

    # Maybe add a 404 "URL not found" page here

    @app.callback(
        Output("page-content", "style"),
        Input("url", "pathname"),
    )
    def update_style(pathname):
        if pathname != "/":
            return {
                "margin-left": "12rem",
                "margin-right": "2rem",
                "padding": "2rem 1rem",
                "padding-bottom": "0px",
            }
