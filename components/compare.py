import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html, dash_table
from dash_iconify import DashIconify
from datetime import datetime, date


def get_icon(icon):
    return DashIconify(icon=icon, height=18)

layout = dbc.Container([
    dbc.Row([
        html.H1(
            'Compare page',
            style={'text-align': 'center'}
        )
    ]),
    dbc.Col([
        dbc.RadioItems(
            options=[
                {"label": "bu/ac", "value": "bu-ac"},
                {"label": "Mg/ha", "value": "mg-ha"},
            ],
            value='bu-ac',
            id="units-selection",
            inline=True,
        ),
    ]),
    dbc.Col([
        dbc.RadioItems(
            options=[
                {"label": "Filter by Genotype", "value": "genotype"},
                {"label": "Filter by Year", "value": "year"},
            ],
            value='genotype',
            id="filter-opt",
            inline=True,
        ),
    ]),
    dbc.Row([
        dcc.Store(id='selected-opt-store'),
        dbc.Col([
            dmc.Select(
                id='compare-first-dropdown',
                # style={"width": 150}, 
                radius=20,
                icon=DashIconify(icon="ph:calendar-light", height=26),
            ),
        ]),
        dbc.Col([
            dmc.Select(
                id='compare-second-dropdown',
                # style={"width": 230},
                radius=20,
                icon=DashIconify(icon="ph:dna", height=26),
            ),
        ]),
        dbc.Col([
            dmc.Button(
                "Add Genotype",
                className="me-4",
                variant="outline",
                id="compare-add-btn",
                leftIcon=DashIconify(icon="gala:add"),
                color='green',
                radius=20,
                n_clicks=0,
            ),
            dmc.Button(
                "Clear Genotypes",
                className="me-4",
                variant="outline",
                id="compare-clear-btn",
                leftIcon=DashIconify(icon="pajamas:remove"),
                color='red',
                radius=20,
                n_clicks=0,
            ),
        ]),
    ]),

    dbc.Row([html.H4(id="add-opt-output")]),
    dbc.Col([
        dbc.Alert(
            id="input-alert",
            is_open=False,
            duration=2000,
            color="danger",
            className="text-center",
            style={"display": "inline-block", "margin": "0 auto"}
        ),
    ], className="d-flex justify-content-center"),

    # Graphs
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='compare-yield-bar-graph',
                config={
                    'displayModeBar': False
                }
            )
        ], className="compare-plot", width=5),
        dbc.Col([
            dcc.Graph(
                id='compare-yield-box-graph',
                config={
                    'displayModeBar': False
                }
            )
        ], className="compare-plot", width=5),
    ], justify="between"),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='compare-county-yield-map',
                config={
                    'displayModeBar': False
                }
            )
        ], className="compare-plot", width=5),
        dbc.Col([
            dcc.Graph(
                id='compare-county-yield-bar-graph',
                config={
                    'displayModeBar': False
                }
            )
        ], className="compare-plot", width=5),
    ], justify="between"),

    # dbc.Row([
    #     dbc.Row([
    #         html.H1(
    #             'Table',
    #             style={'text-align': 'center'}
    #         )
    #     ]),
    #     dash_table.DataTable(
    #         id='table-data',
    #         page_size=5,
    #         style_data_conditional=[
    #             {
    #                 'if': {'row_index': 'even'},
    #                 'backgroundColor': 'rgb(220, 220, 220)',
    #             }
    #         ],
    #         style_cell={
    #             'text-align': 'left'
    #         }
    #     ),
    # ]),
], fluid=True)
