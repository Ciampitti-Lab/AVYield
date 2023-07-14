import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

layout = html.Div([
    html.H1('Data'),
    html.H2(id='data-selected-crop'),
    html.Div([
        html.H3('From:', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='data-start-year-dropdown',
            clearable=False,
            style={'margin-right': '30px'}
        ),
        html.H3('To:', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='data-end-year-dropdown',
            clearable=False,
            style={'margin-right': '30px'}
        ),
        html.Button("Download Dataset", id="data-download-btn"),
        dcc.Download(id="data-download")
    ], style={'display': 'flex'}),

    html.H2("Preview"),
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
])
