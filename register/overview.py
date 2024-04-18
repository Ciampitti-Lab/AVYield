import pandas as pd
import dash
import plotly.graph_objects as go
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
from data import visualization as vis
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import base64
import io


def callbacks(app):
    # Update Icon in Crops Dropdown
    @app.callback(Output("ov-crops-dropdown", "icon"), Input("ov-crops-dropdown", "value"))
    def update_ov_crops_dropdown_icon(selected_crop):
        icons = {
            "Canola": DashIconify(icon="mdi:oil-saver", height=26),
            "Corn": DashIconify(icon="mdi:corn", height=26),
            "Sorghum": DashIconify(icon="fluent:food-grains-20-filled", height=26),
            "Soybean": DashIconify(icon="fluent-emoji-high-contrast:beans", height=26),
            "Wheat": DashIconify(icon="lucide:wheat", height=26),
            "Sunflower": DashIconify(
                icon="fluent-emoji-high-contrast:sunflower", height=26
            ),
        }
        return icons[selected_crop]

    @app.callback(
        Output("ov-states-dropdown", "data"),
        Output("ov-states-dropdown", "value"),
        Input("ov-crops-dropdown", "value"),
    )
    def update_state_by_crops_dropdown(crops_value):
        dataset = vis.get_dataset(crops_value)
        dataset.loc[:, "STATE"] = dataset["STATE"].astype(str)
        return (
            [
                {"label": str(state), "value": state}
                for state in sorted(dataset["STATE"].unique())
            ],
            "KS",
        )

    # First dropdown
    @app.callback(
        Output("ov-year-dropdown", "data"),
        Output("ov-year-dropdown", "value"),
        Input("ov-crops-dropdown", "value"),
        Input("ov-states-dropdown", "value"),
    )
    def update_ov_loc_dropdown(crops_value, state):
        dataset = vis.get_dataset(crops_value)
        dataset = dataset[dataset.STATE == state]

        return (
            [
                {"label": str(year), "value": year}
                for year in dataset["YEAR"].unique()
            ],
            dataset.iloc[-1]["YEAR"],
        )

    # Second dropdown
    @app.callback(
        Output("ov-loc-dropdown", "data"),
        Output("ov-loc-dropdown", "value"),
        Input("ov-crops-dropdown", "value"),
        Input("ov-states-dropdown", "value"),
        Input("ov-year-dropdown", "value"),
    )
    def update_ov_loc_dropdown(crops_value, state, year):
        dataset = vis.get_dataset(crops_value)
        dataset = dataset[dataset.STATE == state]
        dataset = dataset[dataset.YEAR == year]
        return (
            [
                {"label": loc, "value": loc}
                for loc in dataset["COUNTY_CITY"].unique()
            ],
            dataset.iloc[-1]["COUNTY_CITY"],
        )

    # Yield Genotype Bar graph
    @app.callback(
        Output("ov-bar-graph", "figure"),
        Input("ov-crops-dropdown", "value"),
        Input("ov-year-dropdown", "value"),
        Input("ov-loc-dropdown", "value"),
        Input("ov-units-selection", "value"),
        Input("ov-states-dropdown", "value"),
    )
    def update_ov_yield_bar_graph(crops_value, first_opt, second_opt, unit, state):
        return (
            vis.ov_yield_bar(
                crops_value,
                first_opt,
                second_opt,
                state,
                unit,
            )
        )
