import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from components import home, compare, data, about
from data import visualization as vis


def data_callbacks(app):
    # Title
    @app.callback(
        Output('data-selected-crop', 'children'),
        Input('crops-dropdown', 'value')
    )
    def update_data_selected_crop(crop_value):
        return "You are about to download " + crop_value.lower() + " dataset."

    # Start year
    @app.callback(
        [Output('data-start-year-dropdown', 'options'),
         Output('data-start-year-dropdown', 'value')],
        Input('crops-dropdown', 'value')
    )
    def update_data_start_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[0]['YEAR']

    # End year
    @app.callback(
        [Output('data-end-year-dropdown', 'options'),
         Output('data-end-year-dropdown', 'value')],
        [Input('crops-dropdown', 'value'),
         Input('data-start-year-dropdown', 'value')]
    )
    def update_data_end_year_dropdown(crops_value, start_year):
        dataset = vis.get_dataset(crops_value)
        available_years = dataset['YEAR'].unique()
        filtered_years = [
            year for year in available_years if year >= start_year
        ]
        end_year_value = filtered_years[-1] if filtered_years else None
        return [{'label': str(year), 'value': year} for year in filtered_years], end_year_value

    # Download
    @app.callback(
        Output('data-download', 'data'),
        [Input('data-download-btn', 'n_clicks')],
        [State('crops-dropdown', 'value'),
         State('data-start-year-dropdown', 'value'),
         State('data-end-year-dropdown', 'value')],
        prevent_initial_call=True,
    )
    def download_dataset(n_clicks, crops_value, start_year, end_year):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]  # type: ignore

        if trigger_id == 'data-download-btn':
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[(dataset['YEAR'] >= start_year)
                              & (dataset['YEAR'] <= end_year)]
            return dcc.send_data_frame(dataset.to_csv, crops_value.lower()+'_dataset.csv', index=False)
        return None

# Preview Table
    @app.callback(
        Output('data-preview-table', 'data'),
        [Input('crops-dropdown', 'value'),
         Input('data-start-year-dropdown', 'value'),
         Input('data-end-year-dropdown', 'value')],
    )
    def update_data_preview_table(crops_value, start_year, end_year):
        dataset = vis.get_dataset(crops_value)
        dataset = dataset[(dataset['YEAR'] >= start_year)
                          & (dataset['YEAR'] <= end_year)]
        return dataset.to_dict('records')


def compare_callbacks(app):
    # Year dropdown
    @app.callback(
        [Output('compare-year-dropdown', 'options'),
         Output('compare-year-dropdown', 'value')],
        [Input('crops-dropdown', 'value')]
    )
    def update_compare_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']

    @app.callback(
        [Output('compare-brand-1-dropdown', 'options'),
         Output('compare-brand-1-dropdown', 'value'),
         Output('brand-alert-div', 'children')],
        [Input('crops-dropdown', 'value'),
         Input('compare-year-dropdown', 'value')]
    )
    def update_compare_brand_1_dropdown(crops_value, selected_year):
        dataset = vis.get_dataset(crops_value)
        dataset = dataset[dataset.YEAR == selected_year]
        brands = dataset['BRAND'].unique()
        brands = [brand for brand in brands if not pd.isna(brand)]
        brands.sort()
        if not brands:
            alert_message = html.Div(
                'No brands available for the selected crop and year!', style={'color': 'red', 'font-size': '30px'})
            return [], None, alert_message
        else:
            return [{'label': str(brand), 'value': brand} for brand in brands], brands[0], None

    # Brand 2 dropdown
    @app.callback(
        [Output('compare-brand-2-dropdown', 'options'),
         Output('compare-brand-2-dropdown', 'value')],
        [Input('crops-dropdown', 'value'),
         Input('compare-brand-1-dropdown', 'value'),
         Input('compare-year-dropdown', 'value')]
    )
    def update_compare_brand_2_dropdown(crops_value, brand_1, selected_year):
        dataset = vis.get_dataset(crops_value)
        dataset = dataset[dataset.YEAR == selected_year]
        brands = dataset['BRAND'].unique()
        brands = [brand for brand in brands if not pd.isna(brand)]
        if brand_1 in brands:
            brands.remove(brand_1)
        brands.sort()
        if not brands:
            return [], None
        else:
            return [{'label': str(brand), 'value': brand} for brand in brands], brands[1]

    # Yield Brand Bar graph
    @app.callback(
        Output('compare-yield-brand-1-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('compare-year-dropdown', 'value'),
         Input('compare-brand-1-dropdown', 'value')]
    )
    def update_compare_yield_brand_1_graph(crops_value, selected_year, brand_1):
        return vis.compare_yield_brand(crops_value, selected_year, brand_1, False)

    @app.callback(
        Output('compare-yield-brand-2-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('compare-year-dropdown', 'value'),
         Input('compare-brand-2-dropdown', 'value')]
    )
    def update_compare_yield_brand_2_graph(crops_value, selected_year, brand_2):
        return vis.compare_yield_brand(crops_value, selected_year, brand_2, True)

    # Title
    @app.callback(
        Output('compare-second-title', 'children'),
        Input('crops-dropdown', 'value')
    )
    def update_data_selected_crop(crop_value):
        return "Days Yield by Genotype" if crop_value == "Sunflower" else ("Genotype Yield" if crop_value == "Soybean" else "Genotype Moist")

    # Moist Name Scatter graph

    @app.callback(
        Output('compare-moist-name-1-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('compare-year-dropdown', 'value'),
         Input('compare-brand-1-dropdown', 'value')]
    )
    def update_compare_moist_name_brand_1_graph(crops_value, selected_year, brand_1):
        return vis.compare_moist_name(crops_value, selected_year, brand_1, False)

    @app.callback(
        Output('compare-moist-name-2-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('compare-year-dropdown', 'value'),
         Input('compare-brand-2-dropdown', 'value')]
    )
    def update_compare_moist_yield_brand_2_graph(crops_value, selected_year, brand_2):
        return vis.compare_moist_name(crops_value, selected_year, brand_2, True)


def home_callbacks(app):
    # Brand Yield per year
    @app.callback(
        [Output('brand-year-dropdown', 'options'),
         Output('brand-year-dropdown', 'value')],
        [Input('crops-dropdown', 'value')]
    )
    def update_brand_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        brands = dataset['BRAND'].unique()
        brands = [brand for brand in brands if not pd.isna(brand)]
        brands.sort()

        default = ''
        if crops_value == 'Corn':
            default = 'GOLDEN HARVEST'
        elif crops_value == 'Soybean':
            default = 'ASGROW'
        elif crops_value == 'Sunflower':
            default = 'Syngenta'
        elif crops_value == 'Wheat':
            default = 'AGSECO'
        return [{'label': str(brand), 'value': brand} for brand in brands], default

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

# Mean and Total (map) Yield per County
    @app.callback(
        [Output('yield-county-year-dropdown', 'options'),
         Output('yield-county-year-dropdown', 'value')],
        [Input('crops-dropdown', 'value')]
    )
    def update_yield_county_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']

    @app.callback(
        Output('yield-county-graph', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('yield-county-year-dropdown', 'value')]
    )
    def update_yield_county_graph(crops_value, year_value):
        return vis.mean_yield_county(crops_value, year_value)

    @app.callback(
        Output('yield-county-map', 'figure'),
        [Input('crops-dropdown', 'value'),
         Input('yield-county-year-dropdown', 'value')]
    )
    def update_yield_county_map(crops_value, year_value):
        return vis.total_yield_county(crops_value, year_value)

# Mean Yield per year
    @app.callback(
        Output('yield-year-graph', 'figure'),
        Input('crops-dropdown', 'value')
    )
    def update_yield_year_graph(crops_value):
        return vis.yield_year(crops_value)

# Table
    @app.callback(
        Output('table-data', 'data'),
        Input('crops-dropdown', 'value')
    )
    def update_table(crops_value):
        return vis.table(crops_value)


def main_callbacks(app):
 # Update page Index
    @app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/':
            return home.layout
        elif pathname == '/compare':
            return compare.layout
        elif pathname == '/data':
            return data.layout
        elif pathname == '/about':
            return about.layout
        else:
            return home.layout
    # Maybe add a 404 "URL not found" page here
