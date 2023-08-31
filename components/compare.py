import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

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
                # {"label": "lb/ac", "value": "lb-ac"},
                {"label": "Mg/ha", "value": "mg-ha"},
                # {"label": "kg/ha", "value": "kg-ha"},
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
            dcc.Dropdown(
                id='compare-first-dropdown',
                clearable=False,
            ),
        ], width=4),
        dbc.Col([
            dcc.Dropdown(
                id='compare-second-dropdown',
                clearable=False,
            ),
        ], width=4),
        dbc.Col([
            dbc.Button(
                "Add Genotype",
                color='secondary',
                className="me-4",
                id="compare-add-btn",
                n_clicks=0
            ),
            dbc.Button(
                "Clear Genotypes",
                color='danger',
                id="compare-clear-btn",
                n_clicks=0
            ),
        ]),
    ]),

    dbc.Row([html.H4(id="add-opt-output")]),
    dbc.Col([
        dbc.Alert(
            id="input-alert",
            is_open=True,
            duration=2000,
            color="danger",
            className="text-center",
            style={"display": "inline-block", "margin": "0 auto"}
        ),
    ], className="d-flex justify-content-center"),

    dbc.Row([
        dbc.Col([dcc.Graph(id='compare-yield-bar-graph')], width=6),
        dbc.Col([dcc.Graph(id='compare-yield-box-graph')], width=6),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='compare-county-yield-map')], width=6),
        dbc.Col([dcc.Graph(id='compare-county-yield-bar-graph')], width=6),
    ]),


    html.Br(),
    # old home vis down here

    # dbc.Row([
    #     dbc.Row([
    #         html.H1(
    #             'Yield per County by Year',
    #             style={'text-align': 'center'}
    #         )
    #     ]),
    #     dbc.Row([
    #         dcc.Dropdown(
    #             id='yield-county-year-dropdown',
    #             clearable=False,
    #         )
    #     ]),
    #     dbc.Row([
    #         dbc.Col([dcc.Graph(id='yield-county-graph')], width=6),
    #         dbc.Col([dcc.Graph(id='yield-county-map')], width=6),
    #     ]),
    # ]),

    # dbc.Row([
    #     dbc.Row([
    #         html.H1(
    #             'Mean Brand Yield per Year',
    #             style={'text-align': 'center'}
    #         )
    #     ]),
    #     dbc.Row([
    #         dcc.Dropdown(
    #             id='brand-year-dropdown',
    #             clearable=False,
    #         )
    #     ]),
    #     dcc.Graph(id='brand-year-graph'),
    # ]),

    # dbc.Row([
    #     dbc.Row([
    #         html.H1(
    #             'Yield per Brand',
    #             style={'text-align': 'center'}
    #         )
    #     ]),
    #     dcc.Dropdown(
    #         id='yield-brand-dropdown',
    #         clearable=False,
    #     ),
    #     dcc.Graph(id='yield-brand-graph'),
    # ]),

    # dbc.Row([
    #     dbc.Row([
    #         html.H1(
    #             'Mean Yield per Year',
    #             style={'text-align': 'center'}
    #         )
    #     ]),
    #     dcc.Graph(id='yield-year-graph'),
    # ]),

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
