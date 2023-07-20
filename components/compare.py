import dash_bootstrap_components as dbc
from dash import dcc, html

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
], fluid=True)
