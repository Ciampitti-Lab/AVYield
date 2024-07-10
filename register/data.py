import pandas as pd
import dash
from flask import jsonify
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
from data import visualization as vis
from dash_iconify import DashIconify
from config import config


def callbacks(app):
    # Title
    @app.callback(
        Output("data-selected-crop",
               "children"), Input("data-crops-dropdown", "value")
    )
    def update_data_selected_crop(crop_value):
        text_before = f"Set the parameters to download the "
        text_modified = html.Span(crop_value.lower(), style={
                                  "font-weight": "bold"})
        text_after = f" dataset:"

        return html.Div([text_before, text_modified, text_after])

    # Update Icon in Crops Dropdown
    @app.callback(
        Output("data-crops-dropdown",
               "icon"), Input("data-crops-dropdown", "value")
    )
    def update_header_dropdown_icon(selected_crop):
        icons = {
            "Canola": DashIconify(icon="mdi:oil-saver", height=26),
            "Corn": DashIconify(icon="mdi:corn", height=26),
            "Sorghum": DashIconify(icon="fluent:food-grains-20-filled", height=26),
            "Soybean": html.Img(src=config.template.soybean_vector, height=26),
            "Wheat": DashIconify(icon="lucide:wheat", height=26),
            "Sunflower": DashIconify(
                icon="fluent-emoji-high-contrast:sunflower", height=26
            ),
            "Custom": DashIconify(icon="mdi:user", height=26),
        }
        return icons[selected_crop]

    # Start year
    @app.callback(
        [
            Output("data-start-year-dropdown", "data"),
            Output("data-start-year-dropdown", "value"),
        ],
        Input("data-crops-dropdown", "value"),
    )
    def update_data_start_year_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        return [
            {"label": str(year), "value": year} for year in dataset["YEAR"].unique()
        ], dataset.iloc[0]["YEAR"]

    # End year
    @app.callback(
        [
            Output("data-end-year-dropdown", "data"),
            Output("data-end-year-dropdown", "value"),
        ],
        [
            Input("data-crops-dropdown", "value"),
            Input("data-start-year-dropdown", "value"),
        ],
    )
    def update_data_end_year_dropdown(crops_value, start_year):
        dataset = vis.get_dataset(crops_value)
        available_years = dataset["YEAR"].unique()
        filtered_years = [
            year for year in available_years if year >= start_year]
        end_year_value = filtered_years[-1] if filtered_years else None
        return [
            {"label": str(year), "value": year} for year in filtered_years
        ], end_year_value

    # Raw view routing
    @app.server.route("/data/raw/<query>")
    def display_raw_data(query):
        crop = query.split("-")[0]
        year = query.split("-")[1]
        end_year = query.split("-")[2]
        dataset = vis.get_dataset(crop.capitalize())
        # Need to add error handling here later
        dataset = dataset[
            (dataset["YEAR"] >= int(year)) & (dataset["YEAR"] <= int(end_year))
        ]
        return jsonify(dataset.to_dict(orient="records"))

    # Download
    @app.callback(
        Output("data-download", "data"),
        [Input("data-download-btn", "n_clicks")],
        [
            State("data-crops-dropdown", "value"),
            State("data-start-year-dropdown", "value"),
            State("data-end-year-dropdown", "value"),
        ],
        prevent_initial_call=True,
    )
    def download_dataset(n_clicks, crops_value, start_year, end_year):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]  # type: ignore

        if trigger_id == "data-download-btn":
            column_names = [
                "YEAR",
                "LOC",
                "COUNTY_CITY",
                "BRAND",
                "NAME",
                "YIELD",
                "WATER_REGIME",
            ]
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[column_names]
            dataset = dataset[
                (dataset["YEAR"] >= start_year) & (dataset["YEAR"] <= end_year)
            ]
            return dcc.send_data_frame(
                dataset.to_csv, crops_value.lower() + "_dataset.csv", index=False
            )
        return None

    # Docs modal
    @app.callback(
        Output("data-docs-modal", "opened"),
        Input("data-docs-btn", "n_clicks"),
        State("data-docs-modal", "opened"),
        prevent_initial_call=True,
    )
    def toggle_modal(n_clicks, opened):
        return not opened

    # Docs Table
    @app.callback(
        Output("data-docs-table", "data"),
        Output("data-docs-skeleton", "visible"),
        [
            Input("data-crops-dropdown", "value"),
            Input("update-interval", "n_intervals"),
        ],
    )
    def update_data_docs_table(crops_value, n_intervals):
        column_names = ["Attribute", "Type", "Description"]
        if n_intervals > 1:
            # Show only column names with an empty table for the first 5 seconds
            dataset = pd.read_csv(config.data.docs_path)
            dataset = dataset[dataset["Dataset"].isin([crops_value, "All"])]
            dataset = dataset[column_names]
            return dataset.to_dict("records"), False

        data = [[""] * len(column_names) for _ in range(20)]
        empty_dataframe = pd.DataFrame(
            data, columns=column_names)
        return empty_dataframe.to_dict("records"), True

    # Preview Table
    @app.callback(
        Output("data-preview-table", "data"),
        Output("data-table-skeleton", "visible"),
        [
            Input("data-crops-dropdown", "value"),
            Input("data-start-year-dropdown", "value"),
            Input("data-end-year-dropdown", "value"),
            Input("update-interval", "n_intervals"),
        ],
    )
    def update_data_preview_table(crops_value, start_year, end_year, n_intervals):
        column_names = [
            "YEAR",
            "LOC",
            "COUNTY_CITY",
            "BRAND",
            "NAME",
            "YIELD",
            "WATER_REGIME",
        ]
        if n_intervals > 1:
            # Show only column names with an empty table for the first 5 seconds
            dataset = vis.get_dataset(crops_value)
            dataset = dataset[column_names]
            dataset = dataset[
                (dataset["YEAR"] >= start_year) & (dataset["YEAR"] <= end_year)
            ]
            return dataset.to_dict("records"), False

        data = [[""] * len(column_names) for _ in range(20)]
        empty_dataframe = pd.DataFrame(data, columns=column_names)
        return empty_dataframe.to_dict("records"), True
