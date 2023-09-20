import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc, html, dash_table

layout = dbc.Container([
    html.Div([
        html.H1(
            'Data',
            style={'text-align': 'left', 'font-weight': '600', 'margin-bottom': '0px'}
        ),
        html.H6(
            'Last Updated: September 19, 2023.',
            style={'text-align': 'left', 'color': '#7D7D7D', 'margin-top': '0px'}
        )
    ]),

    html.Div([
        html.H3(
            id='data-selected-crop',
            style={'text-align': 'left', 'font-weight': '300', 'margin-top': '20px'}
        ),
    ]),

    dbc.Stack([
        html.Div([
            dmc.Select(
                id='data-start-year-dropdown',
                style={"width": 150}, 
                radius=20,
                icon=DashIconify(icon="ph:calendar-light", height=26),
            ),
        ]),
        html.Div([
            dmc.Select(
                id='data-end-year-dropdown',
                style={"width": 150}, 
                radius=20,
                icon=DashIconify(icon="ph:calendar-light", height=26),
            ),
        ]),
        html.Div([
            dmc.Button(
                "Download Dataset",
                className="me-4",
                variant="outline",
                id="data-download-btn",
                leftIcon=DashIconify(icon="material-symbols:download"),
                color='violet',
                radius=20,
                n_clicks=0,
            ),
            dcc.Download(id="data-download"),
        ]),
    ], direction="horizontal", gap=3, style={"margin-bottom": 20}),

    dash_table.DataTable(
        id='data-preview-table',
        page_size=20,
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
