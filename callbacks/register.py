import pandas as pd
import dash
import plotly.graph_objects as go
from dash import dcc, html, callback_context
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
    # First dropdown
    @app.callback(
        Output('compare-first-dropdown', 'options'),
        Output('compare-first-dropdown', 'value'),
        Input('crops-dropdown', 'value'),
        Input('filter-opt', 'value')
    )
    def update_compare_first_dropdown(crops_value, filter):
        dataset = vis.get_dataset(crops_value)
        if filter == 'genotype':
            return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']
        elif filter == 'year':
            return [{'label': str(name), 'value': name} for name in sorted(dataset['NAME'].unique())], dataset.iloc[0]['NAME']

    # Second dropdown
    @app.callback(
        Output('compare-second-dropdown', 'options'),
        Output('compare-second-dropdown', 'value'),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('filter-opt', 'value')
    )
    def update_compare_genotype_dropdown(crops_value, selected_filter, filter):
        dataset = vis.get_dataset(crops_value)
        if filter == 'genotype':
            dataset = dataset[dataset.YEAR == selected_filter]
            names = dataset['NAME'].unique()
            names = [name for name in names if not pd.isna(name)]
            names.sort()
            return [{'label': str(name), 'value': name} for name in names], names[0]
        elif filter == 'year':
            dataset = dataset[dataset.NAME == selected_filter]
            years = dataset['YEAR'].unique()
            return [{'label': year, 'value': year} for year in years], years[0]

    # Add and Clear Genotype button
    @app.callback(
        Output("add-opt-output", "children", allow_duplicate=True),
        Output("already-added-alert", "is_open"),
        Output("selected-opt-store", "data", allow_duplicate=True),
        Input("compare-add-btn", "n_clicks"),
        State("compare-second-dropdown", "value"),
        State("add-opt-output", "children"),
        State("selected-opt-store", "data"),
        State("already-added-alert", "is_open"),
        prevent_initial_call=True
    )
    def update_genotype_output(n_clicks, selected_genotype, current_output, stored_genotypes, is_open):
        if stored_genotypes is None:
            stored_genotypes = []

        if n_clicks > 0 and selected_genotype:
            if selected_genotype not in stored_genotypes:
                stored_genotypes.append(selected_genotype)
                if current_output is None:
                    new_output = f"Genotype(s): {selected_genotype}"
                else:
                    new_output = f"{current_output}, {selected_genotype}"
                return new_output, is_open, stored_genotypes
            else:
                return current_output, not is_open, stored_genotypes
        return current_output, False, stored_genotypes

    @app.callback(
        Output("add-opt-output", "children"),
        Output("selected-opt-store", "data"),
        Input("compare-clear-btn", "n_clicks"),
        Input("compare-first-dropdown", "value"),
    )
    def clear_genotype_storage(n_clicks, selected_year):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger_id == 'clear-genotype-btn':
            return None, None
        return None, None

    # Yield Genotype Bar graph
    @app.callback(
        Output('compare-yield-bar-graph', 'figure'),
        Input('compare-add-btn', 'n_clicks'),
        Input("compare-clear-btn", 'n_clicks'),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('selected-opt-store', 'data'),
        Input('filter-opt', 'value'),
    )
    def update_compare_yield_bar_graph(n_clicks, n_clicks_clear, crops_value, first_opt, second_opt, filter):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == 'compare-clear-btn' or trigger_id == 'compare-first-dropdown' or trigger_id == 'crops-dropdown' or trigger_id == 'filter-opt':
            return go.Figure()
        if n_clicks is None:
            return dash.no_update
        if second_opt is None:
            return dash.no_update
        return vis.compare_yield_bar(crops_value, first_opt, second_opt, filter, True)

    # Moist Genotype Box graph
    @app.callback(
        Output('compare-yield-box-graph', 'figure'),
        Input('compare-add-btn', 'n_clicks'),
        Input("compare-clear-btn", 'n_clicks'),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('selected-opt-store', 'data'),
        Input('filter-opt', 'value'),
    )
    def update_compare_yield_box_graph(n_clicks, n_clicks_clear, crops_value, first_opt, second_opt, filter):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == 'compare-clear-btn' or trigger_id == 'compare-first-dropdown' or trigger_id == 'crops-dropdown' or trigger_id == 'filter-opt':
            return go.Figure()
        if n_clicks is None:
            return dash.no_update
        if second_opt is None:
            return dash.no_update
        return vis.compare_yield_box(crops_value, first_opt, second_opt, filter, True)


# def home_callbacks(app):
#     # Brand Yield per year
#     @app.callback(
#         [Output('brand-year-dropdown', 'options'),
#          Output('brand-year-dropdown', 'value')],
#         [Input('crops-dropdown', 'value')]
#     )
#     def update_brand_year_dropdown(crops_value):
#         dataset = vis.get_dataset(crops_value)
#         brands = dataset['BRAND'].unique()
#         brands = [brand for brand in brands if not pd.isna(brand)]
#         brands.sort()

#         default = ''
#         if crops_value == 'Corn':
#             default = 'GOLDEN HARVEST'
#         elif crops_value == 'Soybean':
#             default = 'ASGROW'
#         elif crops_value == 'Sunflower':
#             default = 'Syngenta'
#         elif crops_value == 'Wheat':
#             default = 'AGSECO'
#         return [{'label': str(brand), 'value': brand} for brand in brands], default

#     @app.callback(
#         Output('brand-year-graph', 'figure'),
#         [Input('crops-dropdown', 'value'),
#          Input('brand-year-dropdown', 'value')]
#     )
#     def update_brand_year_graph(crops_value, brand_value):
#         return vis.brand_year(crops_value, brand_value)

# # Yield per brand per year
#     @app.callback(
#         [Output('yield-brand-dropdown', 'options'),
#          Output('yield-brand-dropdown', 'value')],
#         [Input('crops-dropdown', 'value')]
#     )
#     def update_yield_brand_dropdown(crops_value):
#         dataset = vis.get_dataset(crops_value)
#         return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']

#     @app.callback(
#         Output('yield-brand-graph', 'figure'),
#         [Input('crops-dropdown', 'value'),
#          Input('yield-brand-dropdown', 'value')]
#     )
#     def update_yield_brand_graph(crops_value, year_value):
#         return vis.yield_brand(crops_value, year_value)

# # Mean and Total (map) Yield per County
#     @app.callback(
#         [Output('yield-county-year-dropdown', 'options'),
#          Output('yield-county-year-dropdown', 'value')],
#         [Input('crops-dropdown', 'value')]
#     )
#     def update_yield_county_year_dropdown(crops_value):
#         dataset = vis.get_dataset(crops_value)
#         return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR']

#     @app.callback(
#         Output('yield-county-graph', 'figure'),
#         [Input('crops-dropdown', 'value'),
#          Input('yield-county-year-dropdown', 'value')]
#     )
#     def update_yield_county_graph(crops_value, year_value):
#         return vis.mean_yield_county(crops_value, year_value)

#     @app.callback(
#         Output('yield-county-map', 'figure'),
#         [Input('crops-dropdown', 'value'),
#          Input('yield-county-year-dropdown', 'value')]
#     )
#     def update_yield_county_map(crops_value, year_value):
#         return vis.total_yield_county(crops_value, year_value)

# # Mean Yield per year
#     @app.callback(
#         Output('yield-year-graph', 'figure'),
#         Input('crops-dropdown', 'value')
#     )
#     def update_yield_year_graph(crops_value):
#         return vis.yield_year(crops_value)

# # Table
#     @app.callback(
#         Output('table-data', 'data'),
#         Input('crops-dropdown', 'value')
#     )
#     def update_table(crops_value):
#         return vis.table(crops_value)


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
