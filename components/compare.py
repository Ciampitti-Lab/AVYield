import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html, dash_table
from dash_iconify import DashIconify

def get_icon(icon):
    return DashIconify(icon=icon, height=18)

layout = dbc.Container([
    html.Div([
        html.H1(
            'Analytical Overview',
            style={'text-align': 'left', 'font-weight': '600', 'margin-bottom': '0px'}
        ),
        html.H6(
            'Last Updated: September 19, 2023.',
            style={'text-align': 'left', 'color': '#7D7D7D', 'margin-top': '0px'}
        )
    ]),
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
            dbc.Stack([
                html.Div([
                    dmc.SegmentedControl(
                        id="units-selection",
                        value="bu-ac",
                        data=[
                            {"label": "bu/ac", "value": "bu-ac"},
                            {"label": "Mg/ha", "value": "mg-ha"},
                        ],
                        radius=30,
                        color="purple",
                        mt=10,
                        mb=10,
                    ),
                ]),                
                html.Div([
                    dmc.SegmentedControl(
                        id="filter-opt",
                        value="genotype",
                        data=[
                            {"label": "Filter by Genotype", "value": "genotype"},
                            {"label": "Filter by Year", "value": "year"},
                        ],
                        radius=30,
                        color="purple",
                        mt=10,
                        mb=10,
                    )   
                ]),
                
            ], direction="horizontal", gap=3),
        ]
    ),
    dbc.Stack([
        dcc.Store(id='selected-opt-store'),
        html.Div([
            dmc.Select(
                id='compare-first-dropdown',
                style={"width": 150}, 
                radius=20,
                icon=DashIconify(icon="ph:calendar-light", height=26),
            ),
        ]),
        html.Div([
            dmc.Select(
                id='compare-second-dropdown',
                style={"width": 230},
                radius=20,
                icon=DashIconify(icon="ph:dna", height=26),
            ),
        ]),
        html.Div([
            dmc.Button(
                "Add data",
                className="me-4",
                variant="outline",
                id="compare-add-btn",
                leftIcon=DashIconify(icon="gala:add"),
                color='green',
                radius=20,
                n_clicks=0,
            ),
            dmc.Button(
                "Clear all data",
                className="me-4",
                variant="outline",
                id="compare-clear-btn",
                leftIcon=DashIconify(icon="pajamas:remove"),
                color='red',
                radius=20,
                n_clicks=0,
            ),
        ]),
    ], direction="horizontal", gap=3),

    dmc.Group(id="add-opt-output"),
    dbc.Col([
        dmc.Alert(
            "This alert will dismiss itself after 3 seconds!",
            title="Auto Dismissing Alert!",
            id="input-alert",
            color="violet",
            duration=3000,
            hide=True,
            mt=10,
            radius=20
        )
    ]),

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
