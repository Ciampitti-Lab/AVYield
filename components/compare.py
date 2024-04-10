import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify
from config import config


crops = ["Canola", "Corn", "Sorghum", "Soybean", "Sunflower", "Wheat"]


def get_icon(icon):
    return DashIconify(icon=icon, height=18)


layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Analytical Overview",
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
            ]
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
                dbc.Stack(
                    [
                        html.Div(
                            [
                                dmc.Button(
                                    "Upload your own data",
                                    className="",
                                    id="upload-modal-button",
                                    variant="filled",
                                    leftIcon=DashIconify(icon="lucide:upload"),
                                    color="purple",
                                    radius=20,
                                    n_clicks=0,
                                ),
                                dmc.Modal(
                                    id="upload-modal",
                                    centered=True,
                                    zIndex=10000,
                                    size="xl",
                                    withCloseButton=False,
                                    children=[
                                        html.H1(
                                            "Upload your own dataset!",
                                            style={
                                                "text-align": "left",
                                                "font-weight": "600",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        html.H5(
                                            f"The dataset must contain the following columns so visualizations are as expected:",
                                            style={
                                                "text-align": "left",
                                                "color": "#00000",
                                                "margin-top": "10px",
                                            },
                                        ),
                                        html.Ul(
                                            [
                                                html.Li("YEAR: year of the trial."),
                                                html.Li(
                                                    "COUNTY: name of the location of the trial."
                                                ),
                                                html.Li(
                                                    "NAME: genotype name of the trial."
                                                ),
                                                html.Li(
                                                    "WATER_REGIME: water regime of the trial, accepted values are Irrigated or Dryland."
                                                ),
                                            ]
                                        ),
                                        html.Hr(),
                                        dmc.RadioGroup(
                                            [
                                                dmc.Radio(l, value=l)
                                                for l in [
                                                    "Canola",
                                                    "Corn",
                                                    "Sorghum",
                                                    "Soybean",
                                                    "Sunflower",
                                                    "Wheat",
                                                ]
                                            ],
                                            id="custom-crop",
                                            value="Corn",
                                            label="Ensure accurate unit conversion by selecting your crop:",
                                            size="md",
                                            mt=10,
                                            mb=20,
                                        ),
                                        dcc.Upload(
                                            id="upload-btn",
                                            children=html.Div(
                                                [
                                                    html.Div(
                                                        [  # Upload Btn
                                                            "Drag and Drop or ",
                                                            html.A("Select File"),
                                                        ],
                                                        style={
                                                            "width": "100%",
                                                            "height": "60px",
                                                            "lineHeight": "60px",
                                                            "borderWidth": "1px",
                                                            "borderStyle": "dashed",
                                                            "borderRadius": "5px",
                                                            "textAlign": "center",
                                                            "margin": "10px",
                                                        },
                                                    )
                                                ]
                                            ),
                                            multiple=False,
                                        ),
                                        dcc.Store(id="custom-data-store"),
                                        html.Div(id="upload-modal-children"),
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
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
                            ]
                        ),
                        html.Div(
                            [
                                dmc.SegmentedControl(
                                    id="filter-opt",
                                    value="genotype",
                                    data=[
                                        {
                                            "label": "Filter by Genotype",
                                            "value": "genotype",
                                        },
                                        {"label": "Filter by Year", "value": "year"},
                                    ],
                                    radius=30,
                                    color="purple",
                                    mt=10,
                                    mb=10,
                                )
                            ]
                        ),
                    ],
                    direction="horizontal",
                    gap=3,
                ),
            ],
        ),
        dbc.Stack(
            [
                dcc.Store(id="selected-opt-store"),
                dmc.Select(
                    id="crops-dropdown",
                    data=crops,
                    value=crops[0],
                    className="crops-dropdown",
                    style={"width": 160},
                    radius=20,
                    icon=DashIconify(icon="tdesign:corn", height=26),
                ),
                dmc.Select(
                    id="states-dropdown",
                    value="KS",
                    className="crops-dropdown",
                    style={"width": 160},
                    radius=20,
                    icon=DashIconify(icon="emojione:flag-for-united-states", height=26),
                ),
                html.Div(
                    [
                        dmc.Select(
                            id="compare-first-dropdown",
                            style={"width": 150},
                            radius=20,
                            icon=DashIconify(icon="ph:calendar-light", height=26),
                        ),
                    ]
                ),
                html.Div(
                    [
                        dmc.Select(
                            id="compare-second-dropdown",
                            style={"width": 230},
                            radius=20,
                            icon=DashIconify(icon="ph:dna", height=26),
                        ),
                    ]
                ),
                html.Div(
                    [
                        dmc.Button(
                            "Add data",
                            className="me-4",
                            variant="outline",
                            id="compare-add-btn",
                            leftIcon=DashIconify(icon="gala:add"),
                            color="green",
                            radius=20,
                            n_clicks=0,
                        ),
                        dmc.Button(
                            "Clear all data",
                            className="me-2",
                            variant="outline",
                            id="compare-clear-btn",
                            leftIcon=DashIconify(icon="pajamas:remove"),
                            color="red",
                            radius=20,
                            n_clicks=0,
                        ),
                    ]
                ),
            ],
            direction="horizontal",
            gap=3,
        ),
        dmc.Group(id="add-opt-output"),
        dbc.Col(
            [
                dmc.Alert(
                    "This alert will dismiss itself after 3 seconds!",
                    title="Auto Dismissing Alert!",
                    id="input-alert",
                    color="violet",
                    duration=3000,
                    hide=True,
                    mt=10,
                    radius=20,
                )
            ]
        ),
        # Graphs
        dbc.Row(
            [
                dbc.Col(
                    [
                        dmc.LoadingOverlay(
                            dcc.Graph(
                                id="compare-county-yield-bar-graph",
                                config={"displayModeBar": False},
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
                    ],
                    className="compare-big-plot",
                    width=5,
                ),
            ],
            justify="between",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dmc.LoadingOverlay(
                            dcc.Graph(
                                id="compare-yield-bar-graph",
                                config={"displayModeBar": False},
                                style={"margin-top": "20px"},
                            ),
                            loaderProps={
                                "variant": "dots",
                                "color": "violet",
                                "size": "xl",
                            },
                            radius=40,
                        )
                    ],
                    className="compare-plot",
                    width=5,
                ),
                dbc.Col(
                    [
                        dmc.LoadingOverlay(
                            dcc.Graph(
                                id="compare-yield-box-graph",
                                config={"displayModeBar": False},
                                style={"margin-top": "20px"},
                            ),
                            loaderProps={
                                "variant": "dots",
                                "color": "violet",
                                "size": "xl",
                            },
                            radius=40,
                        )
                    ],
                    className="compare-plot",
                    width=5,
                ),
            ],
            justify="between",
        ),
    ]
)
