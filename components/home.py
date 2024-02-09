from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash_player as dp
from dash_iconify import DashIconify
from config import config

page_style = {
    "margin-left": "2rem",
    "margin-right": "0rem",
    "padding": "1rem 1rem",
}

header_style = {
    "margin-left": "10rem",
}


def getCard(name, description, imageURL, url):
    return dmc.MantineProvider(
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
                ],
            },
        },
        children=[
            html.A(
                dmc.Card(
                    children=[
                        dmc.CardSection(
                            dmc.Image(
                                src=imageURL,
                                height=200,
                            )
                        ),
                        dmc.Group(
                            [
                                dmc.Text(name, weight=500),
                                # dmc.Badge("NEW", color="green",
                                #           variant="light"),
                            ],
                            position="center",
                            mt="md",
                            mb="xs",
                        ),
                        dmc.Text(
                            description,
                            size="sm",
                            color="dimmed",
                            style={"text-align": "center"}
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"width": 400},
                ),
                href=url,
                target="_blank",
                style={"text-decoration": "none"}
            )
        ])


layout = html.Div([
    html.Div(
        dbc.Container([
            html.H1(
                "Crop Trials Analysis Tool",
                className="display-1",
                style={
                    "color": "white",
                    "text-shadow": "3px 3px 4px rgba(0, 0, 0, 0.4)",
                    "font-weight": "400",
                    "margin-bottom": "0px"
                }
            ),
            html.H1(
                "Year-to-year crop genotype yield analysis made simple.",
                className="display-5",
                style={
                    "color": "white",
                    "text-shadow": "2px 2px 3px rgba(0, 0, 0, 0.45)",
                    "margin-top": "0px",
                }
            ),
            html.Hr(className="lead", style={
                    "color": "white", "width": "60%", "margin-right": "2em"}),

            html.Div([
                dmc.Button(
                    "Learn more",
                    variant="gradient",
                    gradient={"from": "#774aeb",
                              "to": "#613dbd", "deg": 225},
                    className='shadows-jumbotron',
                    id='home-modal-button'
                ),
                dmc.Modal(
                    id="home-modal",
                    centered=True,
                    zIndex=10000,
                    size="xl",
                    withCloseButton=False,
                    children=[
                        dp.DashPlayer(
                            url="https://www.youtube.com/watch?v=gs4d0_AKQi8",
                            width="100%",
                            height="500px",
                        )
                    ],
                ),
            ]),
        ], fluid=True, className=""),
        className="p-3 bg-light home-jumbotron shadows-jumbotron mb-1"
    ),

    dbc.Row([
        dbc.Stack([
            html.Div([
                html.H1(
                    "Overview",
                    style={
                        "text-align": "left",
                        "font-weight": "600",
                        "margin-bottom": "0px",
                        "margin-top": "5px",
                    },
                ),
                html.H6(
                    "Dashboard guide.",
                    style={
                        "text-align": "left",
                        "color": "#7D7D7D",
                        "margin-top": "0px",
                        "margin-bottom": "0px",
                    },
                ),
            ]),
            dcc.Markdown(
                "* ***Analysis Tool:*** Explore genotype-specific yield insights across multiple years. Analyze the impact of water regimes and geographic locations on yields.",
                style={"font-size": "20px", "margin-top": "10px"}
            ),
            dcc.Markdown(
                "* ***Data***: Download the data for your personal use. Access our extensive database to support your individual analysis and projects.",
                style={"font-size": "20px", "margin-top": "5px"}
            ),
            #
            dcc.Markdown(
                "* ***Contact Us***: Get in touch with us easily using the provided contact information. We're here to assist you and answer any questions.",
                style={"font-size": "20px", "margin-top": "5px"}
            ),
        ]),
    ], style=page_style),
    dbc.Row([
        html.H1(
            "Related Projects",
            style={
                "text-align": "left",
                "font-weight": "600",
                "margin-bottom": "10px",
                "margin-top": "0px",
            },
        ),
        dmc.Group([
            getCard("CornYield0N", "The corny0 tool is based on a Machine Learning model to predict corn yield without N fertilizer as an approximation of soil N supply developed by Correndo et al. (2021).",
                    "https://static.wixstatic.com/media/deef4b_d950a38feeaa49d2986a067c424da4f1~mv2.png/v1/fill/w_654,h_360,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/paste-39B54D97.png", "https://ciampittilab.shinyapps.io/cornyield0N/"),
            getCard("DONMaiz", "Compilation and analysis of 788 corn N fertilization trials carried out under a wide spectrum of soil and weather conditions across the Pampas.",
                    "https://static.wixstatic.com/media/deef4b_805fb6f94df5406eb231f72d8313efbd~mv2.png/v1/fill/w_656,h_360,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/paste-2E73617F.png", "https://ciampittilab.shinyapps.io/DONMaiz/#section-principal"),
            getCard("CorN", "Using this tool, a farmer can know, based on their region, the economical and agronomic optimum rate for his/her corn.",
                    config.template.corn_img_src, "https://ciampittilab.shinyapps.io/CorN/"),
        ], position='center', grow=True, style={"margin-top": "15px", "margin-bottom": "15px"})

    ], style=page_style),
], style=header_style)
