from dash import dcc, html, dash_table

layout = html.Div(
    [
        html.H1('Table'),
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

        html.H1('Mean Yield per County by Year'),
        html.Div([
            html.H3('Year:', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='yield-county-year-dropdown',
                clearable=False,
                style={'margin-right': '30px'}
            ),
        ], style={'display': 'flex'}),
        dcc.Graph(id='yield-county-graph'),

        html.H1('Mean Brand Yield per Year'),
        html.Div([
            html.H3('Brand:', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='brand-year-dropdown',
                clearable=False,
                style={'margin-right': '150px'}
            ),
        ], style={'display': 'flex'}),
        dcc.Graph(id='brand-year-graph'),

        html.H1('Yield per Brand'),
        html.Div([
            html.H3('Year:', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='yield-brand-dropdown',
                clearable=False,
                style={'margin-right': '30px'}
            ),
        ], style={'display': 'flex'}),
        dcc.Graph(id='yield-brand-graph'),

        html.H1('Mean Yield per Year'),
        dcc.Graph(id='yield-year-graph'),


    ]
)
