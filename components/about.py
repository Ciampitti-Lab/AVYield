import dash_bootstrap_components as dbc
from dash import dcc, html
from config import config

layout = dbc.Container(
    [
        dbc.Row(
            [
                html.H1("This is the about page",
                        className="about-title"),
                dbc.Col(
                    html.Img(
                        src=config.template.about_img_src,
                        className="img-fluid about-header-img",
                    ),
                    width=12,
                    align="center",
                )
            ],
            className="mb-4",
            align="center"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                html.H3("About us"),
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                    "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                                    "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                                    "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                                    "Integer non augue mattis, iaculis urna in, condimentum urna. "
                                    "Nam hendrerit, ligula nec tristique tincidunt, "
                                    "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                html.H3("About the project"),
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                    "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                                    "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                                    "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                                    "Integer non augue mattis, iaculis urna in, condimentum urna. "
                                    "Nam hendrerit, ligula nec tristique tincidunt, "
                                    "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                html.H3("License and User Agreement"),
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                    "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                                    "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                                    "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                                    "Integer non augue mattis, iaculis urna in, condimentum urna. "
                                    "Nam hendrerit, ligula nec tristique tincidunt, "
                                    "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                                ),
                            ],
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    html.Img(
                        src=config.template.logo_src,
                        className="img-fluid about-logo",
                    ),
                    width=6,
                    align="center",
                ),
            ],
            className="mb-5",
        ),
    ],
    fluid=True,
)
