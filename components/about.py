import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from config import config
from dash_iconify import DashIconify

about_text = """
The Crop Genotype Yield Dashboard was meticulously crafted with farmers in mind. This tool serves as your guide to making well-informed decisions on crop selection, tailored to your location and specific year. It offers a user-friendly interface with customizable insights, ensuring the perfect fit for your unique farming requirements. The tool is a way of clustering all the crop trials data in one place. Join us in reshaping agriculture through data-driven decision-making."""


ciampitti_lab = """
Our mission is to foster excellence in research and service, devoted to the innovation and focusing on integrating new technologies and data science for improving the overall prediction of the behavior of farming systems, with the focus on our farmers.
"""

license_text = """
MIT License

Copyright (c) 2023 Ciampitti Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
        pic = "https://media.licdn.com/dms/image/C5603AQGw9vPFTyNuXA/profile-displayphoto-shrink_800_800/0/1627047084122?e=1707350400&v=beta&t=knXW8Kcs8xNyt7klGiQq-bkITxDyLeSlzM6wp1LPh4o"
        name = "Ignacio Ciampitti"
        prof = "Agronomist"
        title = "Ciampitti Lab Leader"
        link = "https://www.agronomy.k-state.edu/about/people/faculty/ciampitti-ignacio/"
    elif person == "Carlos":
        pic = "https://media.licdn.com/dms/image/D5603AQH82E5UpIYQAQ/profile-displayphoto-shrink_200_200/0/1696041319368?e=1708560000&v=beta&t=smxE4cXQy0NKFCjrOjKWmzIIBLL8JlDIsMSma5wyCBY"
        name = "Carlos Hernandez"
        prof = "Agronomist"
        title = "Research Associate at Kansas State University"
        link = "https://www.linkedin.com/in/carlos-hernandez-265797a1/"
    elif person == "Lucas":
        pic = "https://media.licdn.com/dms/image/C4D03AQEbWSyuWIwVgQ/profile-displayphoto-shrink_200_200/0/1660946478693?e=1708560000&v=beta&t=ytDtIQR2S6Ob3SYsS8GTWw3SteoG63Ip0ATbhyjh9sc"
        name = "Lucas Hiroshi Suguiura"
        prof = "Agronomist"
        title = "Research Scholar at Kansas State University"
        link = "https://www.linkedin.com/in/lucas-hiroshi-suguiura-60260a162/"

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
                    dcc.Markdown(about_text)
                ]),
                dbc.Row([
                    html.H3("Ciampitti Lab"),
                    dcc.Markdown(ciampitti_lab)
                ]),
                dbc.Row([
                    html.H3("License and User Agreement"),
                    dcc.Markdown(license_text)
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
                    createNewPFP("Lucas"),
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
