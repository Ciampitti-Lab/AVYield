import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

layout = dbc.Container([
    dbc.Row([
        html.H1(
            'Compare page',
            style={'text-align': 'center'}
        )
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='compare-year-dropdown',
                clearable=False,
            ),
        ]),
        dbc.Col([
            dcc.Dropdown(
                id='compare-brand-1-dropdown',
                clearable=False,
            ),
        ]),
        dbc.Col([
            dcc.Dropdown(
                id='compare-brand-2-dropdown',
                clearable=False
            ),
        ]),
    ]),
    html.Div(id='brand-alert-div'),

    html.Br(),
    html.Br(),

    dbc.Row([
        html.H1(
            "Genotype Yield",
            style={'text-align': 'center'}
        )
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='compare-yield-brand-1-graph')], width=6),
        dbc.Col([dcc.Graph(id='compare-yield-brand-2-graph')], width=6),
    ]),

    html.Br(),
    html.Br(),

    dbc.Row([
        html.H1(
            id='compare-second-title',
            style={'text-align': 'center'}
        )
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='compare-moist-name-1-graph')], width=6),
        dbc.Col([dcc.Graph(id='compare-moist-name-2-graph')], width=6),
    ]),

    html.Br(),
    # old home vis down here

    dbc.Row([
            dbc.Row([
                html.H1(
                    'Table',
                    style={'text-align': 'center'}
                )
            ]),
            dash_table.DataTable(
                id='table-data',
                page_size=5,
                style_data_conditional=[
                    {
                        'if': {'row_index': 'even'},
                        'backgroundColor': 'rgb(220, 220, 220)',
                    }
                ],
                style_cell={
                    'text-align': 'left'
                }
            ),
            ]),

    dbc.Row([
        dbc.Row([
            html.H1(
                'Yield per County by Year',
                style={'text-align': 'center'}
            )
        ]),
        dbc.Row([
            dcc.Dropdown(
                id='yield-county-year-dropdown',
                clearable=False,
            )
        ]),
        dbc.Row([
            dbc.Col([dcc.Graph(id='yield-county-graph')], width=6),
            dbc.Col([dcc.Graph(id='yield-county-map')], width=6),
        ]),
    ]),

    dbc.Row([
        dbc.Row([
            html.H1(
                'Mean Brand Yield per Year',
                style={'text-align': 'center'}
            )
        ]),
        dbc.Row([
            dcc.Dropdown(
                id='brand-year-dropdown',
                clearable=False,
            )
        ]),
        dcc.Graph(id='brand-year-graph'),
    ]),

    dbc.Row([
        dbc.Row([
            html.H1(
                'Yield per Brand',
                style={'text-align': 'center'}
            )
        ]),
        dcc.Dropdown(
            id='yield-brand-dropdown',
            clearable=False,
        ),
        dcc.Graph(id='yield-brand-graph'),
    ]),

    dbc.Row([
        dbc.Row([
            html.H1(
                'Mean Yield per Year',
                style={'text-align': 'center'}
            )
        ]),
        dcc.Graph(id='yield-year-graph'),
    ]),
], fluid=True)
