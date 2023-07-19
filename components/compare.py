import dash_bootstrap_components as dbc
from dash import dcc, html

layout = html.Div([
    html.H1("Compare page"),
    html.Div([
        html.H3('Year:', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='compare-year-dropdown',
            clearable=False,
            style={'margin-right': '30px'}
        ),
        html.H3('Brands:', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='compare-brand-1-dropdown',
            clearable=False,
            style={'margin-right': '150px'}
        ),
        dcc.Dropdown(
            id='compare-brand-2-dropdown',
            clearable=False,
            style={'margin-right': '150px'}
        ),
    ], style={'display': 'flex'}),
    html.Div(id='brand-alert-div'),
    html.H4("Genotype Yield", style={
        'margin-top': '40px'}),
    html.Div([
        dcc.Graph(id='compare-yield-brand-1-graph'),
        dcc.Graph(id='compare-yield-brand-2-graph'),
    ], style={'display': 'flex', 'margin-top': '0px'}),

    html.H4(id='compare-second-title', style={
        'margin-top': '40px'}),
    html.Div([
        dcc.Graph(id='compare-moist-name-1-graph'),
        dcc.Graph(id='compare-moist-name-2-graph'),
    ], style={'display': 'flex', 'margin-top': '0px'}),
])
