import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

layout = dbc.Container([
    dbc.Row([
        html.H1(
            'Data',
            style={'text-align': 'center'}
        )
    ]),
    html.H2(id='data-selected-crop', style={'text-align': 'center'}),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='data-start-year-dropdown',
                clearable=False,
            ),
        ]),
        dbc.Col([
            dcc.Dropdown(
                id='data-end-year-dropdown',
                clearable=False,
            ),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Button("Download Dataset", id="data-download-btn"),
            dcc.Download(id="data-download")
        ], style={'display': 'flex', 'justify-content': 'center'}),
    ], className='g-0'),

    html.Br(),

    html.H2("Preview",  style={'text-align': 'center'}),
    dash_table.DataTable(
        id='data-preview-table',
        page_size=10,
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
], fluid=True)
