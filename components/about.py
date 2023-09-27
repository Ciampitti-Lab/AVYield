import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from config import config
from dash_iconify import DashIconify


def createNewPFP(person):
    if person == "Pedro":
        pic = "https://avatars.githubusercontent.com/u/41391182?v=4"
        name = "Pedro Henrique M. Cisdeli"
        prof = "Computer Science Undergrad Student"
        title = "Visiting Scholar at Kansas State University"
        link = "https://github.com/cisdeli"
    elif person == "Gustavo":
        pic = "https://avatars.githubusercontent.com/u/104911112?v=4"
        name = "Gustavo Nocera Santiago"
        prof = "Biosystems Engineer"
        title = "MSc. Student at Kansas State University"
        link = "https://github.com/GustavoSantiago113"
    elif person == "Ignacio":
        pic = "https://media.licdn.com/dms/image/C5603AQGw9vPFTyNuXA/profile-displayphoto-shrink_800_800/0/1627047083112?e=1701302400&v=beta&t=76UtycQjrdli4qAx2TR_xAf0YjG5Ez7ze03m8Yn1SWo"
        name = "Ignacio Ciampitti"
        prof = "Agronomist"
        title = "Ciampitti Lab Leader"
        link = "https://www.agronomy.k-state.edu/about/people/faculty/ciampitti-ignacio/"
    elif person == "Carlos":
        pic = "https://media.licdn.com/dms/image/D5603AQFxde-3s-7DEA/profile-displayphoto-shrink_800_800/0/1665602270810?e=1701302400&v=beta&t=r0jUqkM1WdqE_njekYXFgVKgpry9a0nEzIQ5Z9nl8fM"
        name = "Carlos Hernandez"
        prof = "Agronomist"
        title = "Research Scholar at Kansas State University"
        link = "https://www.linkedin.com/in/carlos-hernandez-265797a1/"

    return [
        dmc.Anchor(
            dmc.Avatar(
                src=pic, radius=300, size=100, className='about-avatar'
            ),
            href=link,
            target="_blank"
        ),
        html.Div(className='vertical-separator'),
        dmc.Stack([
            html.H6(
                name,
                style={
                    "margin-top": "10px",
                    "margin-bottom": "0px",
                }
            ),
            html.H6(
                prof,
                style={
                    "margin-top": "0px",
                    "margin-bottom": "0px",
                }
            ),
            html.H6(
                title,
                style={
                    "margin-top": "0px",
                    "margin-bottom": "10px",
                }
            ),
        ], spacing=1),
    ]


layout = html.Div([
    html.Div([
        html.H1(
            "About Us",
            style={
                "text-align": "left",
                "font-weight": "600",
                "margin-bottom": "0px",
            },
        ),
        html.H6(
            "Useful information, paper and right-of-use.",
            style={
                "text-align": "left",
                "color": "#7D7D7D",
                "margin-top": "0px",
                "margin-bottom": "10px",
            },
        ),
    ]),
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
                ],
            },
        },
        children=[
            dmc.Group([
                dmc.Anchor(
                    dmc.Button(
                        "Paper",
                        leftIcon=DashIconify(
                            icon="quill:paper", height=24),
                        size="md",
                        radius=30,
                        color="purple",
                        variant="outline",
                    ),
                    href=config.paper_url,
                    target="_blank",
                ),
                dmc.Anchor(
                    dmc.Button(
                        "Github",
                        leftIcon=DashIconify(
                            icon="mdi:github", height=24),
                        size="md",
                        radius=30,
                        color="purple",
                        variant="outline",
                    ),
                    href=config.github_url,
                    target="_blank",
                ),
                dmc.Anchor(
                    dmc.Button(
                        "Ciampitti Lab",
                        leftIcon=dmc.Avatar(
                            src=config.template.logo_src,
                            size=24,
                            radius="xs",
                            mr=0,
                        ),
                        size="md",
                        radius=30,
                        color="purple",
                        variant="outline",
                    ),
                    href=config.ciampitti_url,
                    target="_blank",
                ),
            ], style={"margin-bottom": "40px"})
        ]
    ),
    dbc.Row([
        dbc.Col([
            dbc.Stack([
                dbc.Row([
                    html.H3("About the project"),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                        "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                        "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                        "Integer non augue mattis, iaculis urna in, condimentum urna. "
                        "Nam hendrerit, ligula nec tristique tincidunt, "
                        "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                        "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                        "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                        "Integer non augue mattis, iaculis urna in, condimentum urna. "
                        "Nam hendrerit, ligula nec tristique tincidunt, "
                        "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                    ),
                ]),
                dbc.Row([
                    html.H3("Ciampitti Lab"),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                        "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                        "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                        "Integer non augue mattis, iaculis urna in, condimentum urna. "
                        "Nam hendrerit, ligula nec tristique tincidunt, "
                        "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                    ),
                ]),
                dbc.Row([
                    html.H3("License and User Agreement"),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                        "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                        "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                        "Integer non augue mattis, iaculis urna in, condimentum urna. "
                        "Nam hendrerit, ligula nec tristique tincidunt, "
                        "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Quisque semper eleifend nisi, id lobortis dolor dignissim ac. "
                        "In eu quam est. Nullam eu felis sed urna ultricies finibus. "
                        "Pellentesque interdum dolor et ante placerat, ac placerat ante varius. "
                        "Integer non augue mattis, iaculis urna in, condimentum urna. "
                        "Nam hendrerit, ligula nec tristique tincidunt, "
                        "nisi lorem aliquet risus, sed bibendum sem mi in urna."
                    ),
                ]),
            ]),
        ]),
        dbc.Col([
            dmc.Stack([
                html.H3(
                    "Contributors",
                    style={
                        "text-align": "center",
                        "font-weight": "400",
                        "margin-top": "0px",
                        "margin-bottom": "5px",
                    },
                ),
                dmc.Group(
                    createNewPFP("Pedro"),
                    position="left",
                    className="about-pfp-container"
                ),
                dmc.Group(
                    createNewPFP("Carlos"),
                    position="left",
                    className="about-pfp-container"
                ),
                dmc.Group(
                    createNewPFP("Gustavo"),
                    position="left",
                    className="about-pfp-container"
                ),
                dmc.Group(
                    createNewPFP("Ignacio"),
                    position="left",
                    className="about-pfp-container"
                ),
            ], align='center')
        ], width=5),
    ])
])
