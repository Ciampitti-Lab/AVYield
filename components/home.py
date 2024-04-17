from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash_player as dp
from dash_iconify import DashIconify
from config import config


cards = [
    {
        "key": "1",
        "header": "CornYield0N",
        "caption": "The corny0 tool is based on a Machine Learning model to predict corn yield without N fertilizer as an approximation of soil N supply developed by Correndo et al. (2021).",
        "src": "https://static.wixstatic.com/media/deef4b_d950a38feeaa49d2986a067c424da4f1~mv2.png/v1/fill/w_654,h_360,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/paste-39B54D97.png",
        "caption_class_name": "custom-caption rounded lead",
        "img_class_name": "w-100 custom-img",
        "href": "https://ciampittilab.shinyapps.io/cornyield0N/",
        "target": "_blank"
    },
    {
        "key": "2",
        "header": "DONMaiz",
        "caption": "Compilation and analysis of 788 corn N fertilization trials carried out under a wide spectrum of soil and weather conditions across the Pampas.",
        "src": "https://static.wixstatic.com/media/deef4b_805fb6f94df5406eb231f72d8313efbd~mv2.png/v1/fill/w_656,h_360,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/paste-2E73617F.png",
        "caption_class_name": "custom-caption rounded lead",
        "img_class_name": "w-100 custom-img",
        "href": "https://ciampittilab.shinyapps.io/DONMaiz/#section-principal",
        "target": "_blank"
    },
    {
        "key": "3",
        "header": "CorN",
        "caption": "Using this tool, a farmer can know, based on their region, the economical and agronomic optimum rate for his/her corn.",
        "src": config.template.corn_img_src,
        "caption_class_name": "custom-caption rounded lead",
        "img_class_name": "w-100 custom-img",
        "href": "https://ciampittilab.shinyapps.io/CorN/",
        "target": "_blank"
    }
]


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
                                height=350,
                            )
                        ),
                        dmc.Group(
                            [
                                dmc.Text(name, weight=500),
                                dmc.Badge("NEW", color="green",
                                          variant="light"),
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
                    style={"width": 600},
                ),
                href=url,
                target="_blank",
                style={"text-decoration": "none"}
            )
        ])


layout = html.Div([
    html.Div([
        html.H1(
            "Crop Trials Analysis Tool",
            style={'text-align': 'left',
                   'font-weight': '600', 'margin-bottom': '0px'}
        ),
        html.H2(
            "Year-to-year crop genotype yield analysis made simple.",
            style={'text-align': 'left',
                   'font-style': 'italic', 'margin-top': '0px', 'margin-bottom': '0px'}
        ),
        html.H6(
            f'Last Updated: {config.last_updated}.',
            style={'text-align': 'left', 'color': '#7D7D7D', 'margin-top': '0px'}
        )
    ]),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.H2(
                    "Overview",
                    style={
                        "text-align": "left",
                        "font-weight": "600",
                        "margin-bottom": "0px",
                        "margin-top": "20px",
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
            ], style={"margin-top": "10px"}),
            dbc.Stack([
                dcc.Markdown(
                    "***Analysis Tool:*** Explore genotype-specific yield insights across multiple years and analyze the impact of water regimes and geographic locations on yields. Select the settings for the first three dropdowns, and use the last dropdown exclusively to adjust the data you wish to filter, choosing between genotype or year. For genotype filtering, fix the crop, state, and year, and alternate among various genotypes. For year filtering, keep the crop, state and genotype dropdowns constant, and cycle through different years. Additionally, you can upload your own data to compare with the existing datasets.",
                    style={"font-size": "20px", "margin-top": "10px"}
                ),
                dcc.Markdown(
                    "***Data***: Download the data for your personal use. Access our extensive database to support your individual analysis and projects. Furthermore, we are providing some basic documentation and context to help you understand the data better. If you need more information, please contact us.",
                    style={"font-size": "20px", "margin-top": "5px"}
                ),
                #
                dcc.Markdown(
                    "***Contact Us***: Get in touch with us easily using the provided contact information. We're here to assist you and answer any questions.",
                    style={"font-size": "20px", "margin-top": "5px"}
                ),
            ]),
        ], width=6),
        dbc.Col([
            html.H2(
                "Related Resources",
                style={
                    "text-align": "left",
                    "font-weight": "600",
                    "margin-bottom": "0px",
                    "margin-top": "20px",
                },
            ),
            html.H6(
                "Try out some other tools from our Lab/external sources.",
                style={
                    "text-align": "left",
                    "color": "#7D7D7D",
                    "margin-top": "0px",
                    "margin-bottom": "30px",
                },
            ),
            dbc.Row([
                dbc.Carousel(
                    items=[
                        card for card in cards
                    ],
                    class_name="carousel-fade",
                    variant="dark",
                    controls=False,
                    indicators=True,
                    ride='carousel',
                    interval=3000,
                )
            ]),
        ], width=6),
    ]),
])
