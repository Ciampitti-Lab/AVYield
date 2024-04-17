import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc, html, dash_table
from config import config

crops = ["Canola", "Corn", "Sorghum", "Soybean", "Sunflower", "Wheat"]


layout = html.Div([
    html.Div([
        html.H1(
            'Data',
            style={'text-align': 'left',
                   'font-weight': '600', 'margin-bottom': '0px'}
        ),
        html.H6(
            f'Last Updated: {config.last_updated}.',
            style={'text-align': 'left', 'color': '#7D7D7D', 'margin-top': '0px'}
        )
    ]),

    html.Div([
        html.H3(
            id='data-selected-crop',
            style={'text-align': 'left',
                   'font-weight': '300', 'margin-top': '20px'}
        ),
    ]),

    dbc.Stack([
        dmc.Select(
            id="data-crops-dropdown",
            data=crops,
            value=crops[0],
            className="crops-dropdown",
            style={"width": 160},
            radius=20,
            icon=DashIconify(icon="tdesign:corn", height=26),
        ),
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
                className="me-1",
                variant="outline",
                id="data-download-btn",
                leftIcon=DashIconify(icon="material-symbols:download"),
                color='violet',
                radius=20,
                n_clicks=0,
            ),
            dcc.Download(id="data-download"),
        ]),
        html.Div([
            dmc.Button(
                "Show Documentation",
                variant="outline",
                id="data-docs-btn",
                leftIcon=DashIconify(icon="oui:documentation"),
                color='violet',
                radius=20,
                n_clicks=0,
            ),
            dmc.Modal(
                id="data-docs-modal",
                centered=True,
                zIndex=10000,
                size="1500px",
                withCloseButton=False,
                children=[
                    dmc.Skeleton(
                        dash_table.DataTable(
                            id='data-docs-table',
                            page_size=20,
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'even'},
                                    'backgroundColor': 'rgb(220, 220, 220)',
                                }
                            ],
                            style_cell={
                                'text-align': 'left',
                                'white-space': 'normal',
                                'height': 'auto',
                                'minWidth': '150px',
                                'width': '150px',
                                'maxWidth': '150px',
                            },
                        ),
                        id='data-docs-skeleton',
                        visible=False
                    )
                ],
            ),

        ]),
    ], direction="horizontal", gap=3, style={"margin-bottom": 20}),

    dcc.Interval(id='update-interval', interval=1000,
                 n_intervals=0, max_intervals=2),
    dmc.Skeleton(
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
            },
        ),
        id='data-table-skeleton',
        visible=False
    )
])
