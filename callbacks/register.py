from dash.dependencies import Input, Output
from components import home, data, about
from data import visualization as vis


def home_callbacks(app):
    @app.callback(
        Output('yield-brand-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('yield-brand-dropdown', 'value')]
    )
    def update_yield_brand_graph(crops_value, year_value):
        return vis.yield_brand(crops_value, year_value)

    @app.callback(
        Output('yield-brand-dropdown', 'options'),
        [Input('crops-dropdown', 'value')]
    )
    def update_yield_brand_dropdown(value):
        return vis.get_year_interval(value)

    @app.callback(
        Output('yield-year-graph', 'figure'),
        Input('crops-dropdown', 'value')
    )
    def update_yield_year_graph(value):
        return vis.yield_year(value)


def main_callbacks(app):
 # Update page Index
    @app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/':
            return home.layout
        elif pathname == '/data':
            return data.layout
        elif pathname == '/about':
            return about.layout
        else:
            return home.layout
    # Maybe add a 404 "URL not found" page here
