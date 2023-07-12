import pandas as pd
from dash.dependencies import Input, Output
from components import home, data, about
from data import visualization as vis


def home_callbacks(app):
    # Brand Yield per year
    @app.callback(
        [Output('brand-year-dropdown', 'options'),
         Output('brand-year-dropdown', 'value')],
        [Input('crops-dropdown', 'value')]
    )
    def update_brand_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        default = ''
        if crops_value == 'Corn':
            default = 'GOLDEN HARVEST'
        elif crops_value == 'Soybean':
            default = 'ASGROW'
        elif crops_value == 'Sunflower':
            default = 'Syngenta'
        elif crops_value == 'Wheat':
            default = 'AGSECO'

        return [{'label': str(brand), 'value': brand} for brand in dataset['BRAND'].unique() if not pd.isna(brand)], default

    @app.callback(
        Output('brand-year-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('brand-year-dropdown', 'value')]
    )
    def update_brand_year_graph(crops_value, brand_value):
        return vis.brand_year(crops_value, brand_value)

# Yield per brand per year
    @app.callback(
        [Output('yield-brand-dropdown', 'options'),
         Output('yield-brand-dropdown', 'value')],
        [Input('crops-dropdown', 'value')]
    )
    def update_yield_brand_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']

    @app.callback(
        Output('yield-brand-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('yield-brand-dropdown', 'value')]
    )
    def update_yield_brand_graph(crops_value, year_value):
        return vis.yield_brand(crops_value, year_value)

# Mean Yield per year
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
