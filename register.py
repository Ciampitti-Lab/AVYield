import pandas as pd
import dash
import plotly.graph_objects as go
from dash import dcc, html, callback_context, dash_table
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
from components import home, compare, data, about
from data import visualization as vis
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import base64
import io

from components import controls


def data_callbacks(app):
    # Title
    @app.callback(
        Output('data-selected-crop', 'children'),
        Input('data-crops-dropdown', 'value')
    )
    def update_data_selected_crop(crop_value):
        text_before = f"Set the parameters to download the "
        text_modified = html.Span(crop_value.lower(), style={
                                  "font-weight": "bold"})
        text_after = f" dataset:"

        return html.Div([text_before, text_modified, text_after])

    # Update Icon in Crops Dropdown
    @app.callback(
        Output('data-crops-dropdown', 'icon'),
        Input('data-crops-dropdown', 'value')
    )
    def update_header_dropdown_icon(selected_crop):
        icons = {
            "Canola": DashIconify(icon="mdi:oil-saver", height=26),
            "Corn": DashIconify(icon="mdi:corn", height=26),
            "Sorghum": DashIconify(icon="fluent:food-grains-20-filled", height=26),
            "Soybean": DashIconify(icon="fluent-emoji-high-contrast:beans", height=26),
            "Wheat": DashIconify(icon="lucide:wheat", height=26),
            "Sunflower": DashIconify(icon="fluent-emoji-high-contrast:sunflower", height=26),
            "Custom": DashIconify(icon="mdi:user", height=26),
        }
        return icons[selected_crop]

    # Start year
    @app.callback(
        [Output('data-start-year-dropdown', 'data'),
         Output('data-start-year-dropdown', 'value')],
        Input('data-crops-dropdown', 'value')
    )
    def update_data_start_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[0]['YEAR']

    # End year
    @app.callback(
        [Output('data-end-year-dropdown', 'data'),
         Output('data-end-year-dropdown', 'value')],
        [Input('data-crops-dropdown', 'value'),
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
        [State('data-crops-dropdown', 'value'),
         State('data-start-year-dropdown', 'value'),
         State('data-end-year-dropdown', 'value')],
        prevent_initial_call=True,
    )
    def download_dataset(n_clicks, crops_value, start_year, end_year):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]  # type: ignore

        if trigger_id == 'data-download-btn':
            column_names = ['YEAR', 'LOC', 'COUNTY_CITY', 'BRAND',
                            'NAME', 'YIELD', 'WATER_REGIME']
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[column_names]
            dataset = dataset[(dataset['YEAR'] >= start_year)
                              & (dataset['YEAR'] <= end_year)]
            return dcc.send_data_frame(dataset.to_csv, crops_value.lower()+'_dataset.csv', index=False)
        return None

    # Preview Table
    @app.callback(
        Output('data-preview-table', 'data'),
        Output('data-table-skeleton', 'visible'),
        [Input('data-crops-dropdown', 'value'),
         Input('data-start-year-dropdown', 'value'),
         Input('data-end-year-dropdown', 'value'),
         Input('update-interval', 'n_intervals')],
    )
    def update_data_preview_table(crops_value, start_year, end_year, n_intervals):
        column_names = ['YEAR', 'LOC', 'COUNTY_CITY', 'BRAND',
                        'NAME', 'YIELD', 'WATER_REGIME']
        if n_intervals > 1:
            # Show only column names with an empty table for the first 5 seconds
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[column_names]
            dataset = dataset[(dataset['YEAR'] >= start_year)
                              & (dataset['YEAR'] <= end_year)]
            return dataset.to_dict('records'), False

        data = [[''] * len(column_names) for _ in range(20)]
        empty_dataframe = pd.DataFrame(data, columns=column_names)
        return empty_dataframe.to_dict('records'), True


def handle_triggers(n_clicks, second_opt):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if trigger_id == 'compare-clear-btn' or trigger_id == 'compare-first-dropdown' or trigger_id == 'crops-dropdown' or trigger_id == 'filter-opt':
        return go.Figure()
    if n_clicks is None:
        return dash.no_update
    if second_opt is None:
        return dash.no_update
    return None


def compare_callbacks(app):
    # Upload Data Modal
    @app.callback(
        Output("upload-modal", "opened"),
        Input("upload-modal-button", "n_clicks"),
        State("upload-modal", "opened"),
        prevent_initial_call=True,
    )
    def custom_data_modal(n_clicks, opened):
        return not opened

    # Upload Data
    def parse_contents(content, filename):
        content_type, content_string = content.split(',')

        decoded = base64.b64decode(content_string)

        if 'csv' not in filename and 'xls' not in filename:
            df = None
            children = html.Div([
                dmc.Alert(
                    "Make sure that you are uploading a .xls or .csv file.",
                    title=dcc.Markdown(f"Failed to load file: *{filename}*"),
                    color="red",
                    withCloseButton=False,
                ),

            ])
        else:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))

            required_columns = ['YEAR', 'WATER_REGIME', 'NAME', 'COUNTY_CITY']

            # Check if all required columns are present in the DataFrame
            missing_columns = [
                col for col in required_columns if col not in df.columns
            ]
            if missing_columns:
                children = html.Div([
                    dmc.Alert(
                        f"Missing columns {', '.join(missing_columns)}, some visualizations may be affected.",
                        title=dcc.Markdown(
                            f"File successfully loaded: *{filename}*"),
                        color="orange",
                        withCloseButton=False,
                    ),
                    dash_table.DataTable(
                        df.to_dict('records'),
                        [{'name': i, 'id': i} for i in df.columns],
                        page_size=10,
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'even'},
                                'backgroundColor': 'rgb(220, 220, 220)',
                            }
                        ],
                        style_cell={
                            'text-align': 'left'
                        },
                    )
                ])
            else:
                children = html.Div([
                    dmc.Alert(
                        f"All required columns found.",
                        title=dcc.Markdown(
                            f"File successfully loaded: *{filename}*"),
                        color="violet",
                        withCloseButton=False,
                        mb=10,
                    ),
                    dash_table.DataTable(
                        df.to_dict('records'),
                        [{'name': i, 'id': i} for i in df.columns],
                        page_size=10,
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'even'},
                                'backgroundColor': 'rgb(220, 220, 220)',
                            }
                        ],
                        style_cell={
                            'text-align': 'left'
                        },
                    )
                ])

        return df, children

    @app.callback(
        Output('custom-data-store', 'data'),
        Output("upload-modal-children", "children"),
        Input('upload-btn', 'contents'),
        State('upload-btn', 'filename'),
    )
    def update_custom_storage(custom_data, filename):
        if custom_data is not None:  # stop modal from cleaning plots
            df, children = parse_contents(custom_data, filename)
            if df is None:
                return None, children
            return df.to_json(orient='records'), children
        return None, None

    # Update Options in Crops Dropdown based on the states !! Change this implementation later !!
    @app.callback(
        Output('crops-dropdown', 'data', allow_duplicate=True),
        Output('crops-dropdown', 'value', allow_duplicate=True),
        Input('states-dropdown', 'value'),
        prevent_initial_call='initial_duplicate'
    )
    def update_crops_dropdown_by_state(state):
        if state == "KS":
            return ["Canola", "Corn", "Sorghum", "Soybean", "Sunflower", "Wheat"], "Canola"
        else:
            return ["Canola"], "Canola"

    # Update Options in Crops Dropdown
    @app.callback(
        Output('crops-dropdown', 'data'),
        Output('crops-dropdown', 'value'),
        Input('custom-data-store', 'data'),
        Input('crops-dropdown', 'data'),
        Input('crops-dropdown', 'value'),
    )
    def update_crops_dropdown_options(c_data, crops_data, crops_value):
        if c_data is not None:
            if "Custom" not in crops_data:
                new_opt = crops_data + ["Custom"]
                return new_opt, "Custom"
            else:
                return crops_data, crops_value
        elif c_data is None and "Custom" in crops_data:
            return ["Canola", "Corn", "Sorghum", "Soybean", "Sunflower", "Wheat"], "Canola"
        else:
            return crops_data, crops_value

    # Update Icon in Crops Dropdown
    @app.callback(
        Output('crops-dropdown', 'icon'),
        Input('crops-dropdown', 'value')
    )
    def update_header_dropdown_icon(selected_crop):
        icons = {
            "Canola": DashIconify(icon="mdi:oil-saver", height=26),
            "Corn": DashIconify(icon="mdi:corn", height=26),
            "Sorghum": DashIconify(icon="fluent:food-grains-20-filled", height=26),
            "Soybean": DashIconify(icon="fluent-emoji-high-contrast:beans", height=26),
            "Wheat": DashIconify(icon="lucide:wheat", height=26),
            "Sunflower": DashIconify(icon="fluent-emoji-high-contrast:sunflower", height=26),
            "Custom": DashIconify(icon="mdi:user", height=26),
        }
        return icons[selected_crop]

    # First dropdown
    @app.callback(
        Output('compare-first-dropdown', 'data'),
        Output('compare-first-dropdown', 'value'),
        Output('compare-first-dropdown', 'icon'),
        Output('compare-first-dropdown', 'style'),
        Input('custom-data-store', 'data'),
        Input('crops-dropdown', 'value'),
        Input('filter-opt', 'value'),
        Input('states-dropdown', 'value'),
    )
    def update_compare_first_dropdown(c_data, crops_value, filter, state):
        if crops_value != "Custom":
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[dataset.STATE == state]
        else:
            dataset = pd.read_json(io.StringIO(c_data))

        if filter == 'genotype':
            return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()], dataset.iloc[-1]['YEAR'], DashIconify(icon="ph:calendar-light", height=26), {"width": 150}
        elif filter == 'year':
            dataset.loc[:, 'NAME'] = dataset['NAME'].astype(str)
            return [{'label': str(name), 'value': name} for name in sorted(dataset['NAME'].unique())], dataset.iloc[0]['NAME'], DashIconify(icon="ph:dna", height=26), {"width": 230}

    # Second dropdown
    @app.callback(
        Output('compare-second-dropdown', 'data'),
        Output('compare-second-dropdown', 'value'),
        Output('compare-second-dropdown', 'icon'),
        Output('compare-second-dropdown', 'style'),
        Input('custom-data-store', 'data'),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('filter-opt', 'value'),
        Input('states-dropdown', 'value'),
    )
    def update_compare_genotype_dropdown(c_data, crops_value, first_dropdown_selection, filter, state):
        if crops_value != "Custom":
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[dataset.STATE == state]
        else:
            dataset = pd.read_json(io.StringIO(c_data))

        if filter == 'genotype':
            dataset = dataset[dataset.YEAR == first_dropdown_selection]
            names = dataset['NAME'].unique()
            names = [name for name in names if not pd.isna(name)]
            names.sort()
            return [{'label': str(name), 'value': name} for name in names], names[0], DashIconify(icon="ph:dna", height=26), {"width": 230}
        elif filter == 'year':
            dataset = dataset[dataset.NAME == first_dropdown_selection]
            years = dataset['YEAR'].unique()
            return [{'label': year, 'value': year} for year in years], years[0], DashIconify(icon="ph:calendar-light", height=26), {"width": 150}

    # Clear storage
    @app.callback(
        Output("add-opt-output", "children"),
        Output("selected-opt-store", "data"),
        Input("compare-clear-btn", "n_clicks"),
        Input("compare-first-dropdown", "value"),
        Input('filter-opt', 'value'),
    )
    def clear_genotype_storage(n_clicks, selected_year, selected_items):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger_id == 'clear-genotype-btn' or trigger_id == 'filter-opt':
            return None, None
        return None, None

    # Add and Clear Genotype button
    @app.callback(
        Output("add-opt-output", "children", allow_duplicate=True),
        Output("input-alert", "hide"),
        Output("input-alert", "title"),
        Output("input-alert", "children"),
        Output("selected-opt-store", "data", allow_duplicate=True),
        Input("compare-add-btn", "n_clicks"),
        Input('filter-opt', 'value'),
        State("compare-second-dropdown", "value"),
        State("add-opt-output", "children"),
        State("selected-opt-store", "data"),
        prevent_initial_call=True
    )
    def update_items_output(n_clicks, filter, selected_items, current_output, stored_items):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if stored_items is None:
            stored_items = []
            current_output = []

        if n_clicks > 0 and selected_items:
            if selected_items not in stored_items:
                if len(stored_items) >= 5:
                    return current_output, False, 'Exceeded item limit!', 'You can only add a maximum of five items.', stored_items

                stored_items.append(selected_items)
                current_output.append(
                    dmc.MantineProvider(
                        theme={
                            "colors": {
                                "purple": [
                                    "#FAF9FD",
                                    "#DED7F2",
                                    "#C2B1EE",
                                    "#A588F2",
                                    "#8758FF",
                                    "#774AEB",
                                    "#6A41D5",
                                    "#613DBD",
                                    "#5C429F",
                                    "#574486",
                                    "#514373"
                                ]
                            },
                        },
                        children=[
                            dmc.Badge(selected_items, color='purple', size='xl', mt=10)]
                    )
                )
                return current_output, True, None, None, stored_items
            elif selected_items in stored_items and trigger_id != 'filter-opt':
                return current_output, False, 'Data Already Added!', 'Duplicates entries are not allowed.', stored_items
        return current_output, True, None, None, stored_items

    # Yield Genotype Bar graph
    @app.callback(
        Output('compare-yield-bar-graph', 'figure'),
        Input('compare-add-btn', 'n_clicks'),
        Input("compare-clear-btn", 'n_clicks'),
        Input('custom-data-store', 'data'),
        Input("custom-crop", "value"),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('selected-opt-store', 'data'),
        Input('filter-opt', 'value'),
        Input('units-selection', 'value'),
        Input('states-dropdown', 'value'),
        State("selected-opt-store", "data"),
    )
    def update_compare_yield_bar_graph(n_clicks, n_clicks_clear, c_data, custom_crop_value, crops_value, first_opt, second_opt, filter, unit, state, stored_items):
        if stored_items is None:
            fig = go.Figure()
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            return fig
        else:
            custom_df = pd.read_json(io.StringIO(
                c_data)) if c_data is not None else None
            return vis.compare_yield_bar(crops_value, first_opt, second_opt, state, unit, filter, True, custom_df, custom_crop_value) if handle_triggers(n_clicks, second_opt) is None else handle_triggers(n_clicks, second_opt)

    # Yield Genotype Box graph
    @app.callback(
        Output('compare-yield-box-graph', 'figure'),
        Input('compare-add-btn', 'n_clicks'),
        Input("compare-clear-btn", 'n_clicks'),
        Input('custom-data-store', 'data'),
        Input("custom-crop", "value"),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('selected-opt-store', 'data'),
        Input('filter-opt', 'value'),
        Input('units-selection', 'value'),
        Input('states-dropdown', 'value'),
        State("selected-opt-store", "data"),
    )
    def update_compare_yield_box_graph(n_clicks, n_clicks_clear, c_data, custom_crop_value, crops_value, first_opt, second_opt, filter, unit, state, stored_items):
        if stored_items is None:
            fig = go.Figure()
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            return fig
        else:
            custom_df = pd.read_json(io.StringIO(
                c_data)) if c_data is not None else None
            return vis.compare_yield_box(crops_value, first_opt, second_opt, state, unit, filter, True, custom_df, custom_crop_value) if handle_triggers(n_clicks, second_opt) is None else handle_triggers(n_clicks, second_opt)

    # County Bar Graph
    @app.callback(
        Output('compare-county-yield-bar-graph', 'figure'),
        Input('compare-add-btn', 'n_clicks'),
        Input("compare-clear-btn", 'n_clicks'),
        Input('custom-data-store', 'data'),
        Input("custom-crop", "value"),
        Input('crops-dropdown', 'value'),
        Input('compare-first-dropdown', 'value'),
        Input('selected-opt-store', 'data'),
        Input('filter-opt', 'value'),
        Input('units-selection', 'value'),
        Input('states-dropdown', 'value'),
        State("selected-opt-store", "data"),
    )
    def update_compare_county_yield_bar_graph(n_clicks, n_clicks_clear, c_data, custom_crop_value, crops_value, first_opt, second_opt, filter, unit, state, stored_items):
        if stored_items is None:
            fig = go.Figure()
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            return fig
        else:
            custom_df = pd.read_json(io.StringIO(
                c_data)) if c_data is not None else None
            return vis.compare_county_yield_bar_graph(crops_value, first_opt, second_opt, state, unit, filter, custom_df, custom_crop_value) if handle_triggers(n_clicks, second_opt) is None else handle_triggers(n_clicks, second_opt)


def home_callbacks(app):
    @app.callback(
        Output("home-modal", "opened"),
        Input("home-modal-button", "n_clicks"),
        State("home-modal", "opened"),
        prevent_initial_call=True,
    )
    def toggle_modal(n_clicks, opened):
        return not opened


def control_callbacks(app):
    # Update sidebar options color based on curr page
    @app.callback(
        Output('sidebar-home', 'active'),
        Output('sidebar-home', 'color'),
        Output('sidebar-compare', 'active'),
        Output('sidebar-compare', 'color'),
        Output('sidebar-data', 'active'),
        Output('sidebar-data', 'color'),
        Output('sidebar-about', 'active'),
        Output('sidebar-about', 'color'),
        Input('url', 'pathname'))
    def update_sidebar_color(pathname):
        if pathname == '/':
            return True, "purple", False, "black", False, "black", False, "black"
        elif pathname == '/compare':
            return False, "black", True, "purple", False, "black", False, "black"
        elif pathname == '/data':
            return False, "black", False, "black", True, "purple", False, "black"
        elif pathname == '/about':
            return False, "black", False, "black", False, "black", True, "purple"


def main_callbacks(app):
 # Update page Index
    @app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/':
            return [home.layout, controls.footer]
        elif pathname == '/compare':
            return [compare.layout, controls.footer]
        elif pathname == '/data':
            return [data.layout, controls.footer]
        elif pathname == '/about':
            return [about.layout, controls.footer]
        else:
            return home.layout
    # Maybe add a 404 "URL not found" page here

    @app.callback(
        Output("page-content", "style"),
        Input("url", "pathname"),
    )
    def update_style(pathname):
        if pathname != '/':
            return {
                "margin-left": "12rem",
                "margin-right": "2rem",
                "padding": "2rem 1rem",
                "padding-bottom": "0px"
            }
