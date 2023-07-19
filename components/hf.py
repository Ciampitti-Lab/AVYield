import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from config import config

title = config.dash.app_title

crops = ["Corn", "Soybean", "Sunflower", "Wheat"]

header = html.Div(
    [
        html.Nav(
            className="navbar navbar-expand-lg navbar-light bg-light",
            children=[
                html.A(
                    [
                        html.Img(
                            src=config.template.fa_logo_src,
                            className="logo",
                        ),
                        html.Span(title, className="navbar-brand-title"),
                    ],
                    className="navbar-brand",
                    href="/",
                ),
                html.Div(
                    id="navbarNav",
                    className="collapse navbar-collapse justify-content-between",
                    children=[
                        html.Ul(
                            className="navbar-nav",
                            children=[
                                html.Li(
                                    className="nav-item",
                                    children=[
                                        dcc.Link("Home", href="/",
                                                 className="nav-link")
                                    ],
                                ),
                                html.Li(
                                    className="nav-item",
                                    children=[
                                        dcc.Link("Compare", href="/compare",
                                                 className="nav-link")
                                    ],
                                ),
                                html.Li(
                                    className="nav-item",
                                    children=[
                                        dcc.Link("Data", href="/data",
                                                 className="nav-link")
                                    ],
                                ),
                                html.Li(
                                    className="nav-item",
                                    children=[
                                        dcc.Link("About", href="/about",
                                                 className="nav-link")
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="nav-item dropdown",
                            children=[
                                dcc.Dropdown(
                                    id="crops-dropdown",
                                    options=crops,
                                    value=crops[0],
                                    clearable=False,
                                    className="dropdown-item",
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Br(),
        html.Div(id="content"),
        html.Div(id="selected-crop", style={"display": "none"}),
    ]
)

footer = html.Div(
    html.Footer(
        [
            html.Span("\u00A9"),
            " 2023 ",
            html.A(
                "Ciampitti Lab",
                href="https://ciampittilab.wixsite.com/ciampitti-lab",
                target="_blank"
            ),
            ". MIT License. Visit on ",
            html.A(
                "Github",
                href=config.github_url,
            ),
            ".",
        ],
        className="text-center my-2",
    ),
)
