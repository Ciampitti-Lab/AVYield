import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify
from config import config


crops = ["Canola", "Corn", "Sorghum", "Soybean", "Sunflower", "Wheat"]


def get_icon(icon):
    return DashIconify(icon=icon, height=18)


layout = html.Div([
    html.Div([
        html.H1(
            "Data Overview",
            style={
                "text-align": "left",
                "font-weight": "600",
                "margin-bottom": "0px",
            },
        ),
        html.H6(
            f"Last Updated: {config.last_updated}.",
            style={
                "text-align": "left",
                "color": "#7D7D7D",
                "margin-top": "0px",
                "margin-bottom": "25px",
            },
        ),
    ]),
    dbc.Stack([
        dmc.Select(
            id="ov-crops-dropdown",
            data=crops,
            value=crops[0],
            className="crops-dropdown",
            style={"width": 160},
            radius=20,
            icon=DashIconify(icon="tdesign:corn", height=26),
        ),
        dmc.Select(
            id="ov-states-dropdown",
            value="KS",
            className="crops-dropdown",
            style={"width": 160},
            radius=20,
            icon=DashIconify(
                icon="emojione:flag-for-united-states", height=26),
        ),
        html.Div([
            dmc.Select(
                id="ov-year-dropdown",
                style={"width": 150},
                searchable=True,
                radius=20,
                icon=DashIconify(
                    icon="ph:calendar-light", height=26),
            )]
        ),
        html.Div([
            dmc.Select(
                id="ov-loc-dropdown",
                style={"width": 230},
                searchable=True,
                radius=20,
                icon=DashIconify(
                    icon="carbon:location", height=26),
            )]
        ),
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
                        "#514373",
                    ]
                },
            },
            children=[
                html.Div([
                    dmc.SegmentedControl(
                        id="ov-units-selection",
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
            ],
        ),
    ], direction="horizontal", gap=3,),
    # Graphs
    dbc.Row([
        dbc.Col([
            dmc.LoadingOverlay(
                dcc.Graph(
                    id="ov-bar-graph",
                    config={"displayModeBar": True, "displaylogo": False},
                    style={"margin-top": "20px"},
                ),
                loaderProps={
                    "variant": "dots",
                    "color": "violet",
                    "size": "xl",
                },
                radius=40,
                id="loading",
            )
        ], className="compare-big-plot", width=5,),
    ], justify="between",),
]
)
