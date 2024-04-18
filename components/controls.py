import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import Dash, dcc, html
from config import config
from dash_iconify import DashIconify


title = config.dash.app_title

crops = ["Corn", "Soybean", "Sunflower", "Wheat"]


def get_icon(icon):
    return DashIconify(icon=icon, height=18)


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "#F6F6F6",
    "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.04), 0 6px 20px 0 rgba(0, 0, 0, 0.07)"
}

CONTENT_STYLE = {
    "margin-left": "10rem",
}

sidebar = html.Div([
    html.Div([
        html.A([
            html.Img(src=config.template.logo_src, className="sidebarLogo", style={
                'width': '40%', 'height': 'auto'}),
            html.Img(src=config.template.id3a_vertical_logo, className="sidebarLogo", style={
                'width': '90%', 'height': 'auto'}),
        ], href="/",)
    ], style={'text-align': 'center'}),
    html.Div(
        style={'display': 'flex', 'justify-content': 'center',
               'align-items': 'center'},
        children=[
            html.Hr(style={'height': '2px', 'width': '80%', 'border': '10px',
                           'border-radius': '10px', 'background-color': '#616060'})
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
                    "#514373"
                ]
            },
        },
        children=[
            dbc.Nav([
                dmc.NavLink(
                    label=dmc.Text("Home", weight=400),
                    icon=get_icon(icon="bi:house-door-fill"),
                    href="/",
                    variant="filled",
                    active=False,
                    color="red",
                    id='sidebar-home'
                ),
                dmc.NavLink(
                    icon=get_icon(icon="fluent-mdl2:calendar-year"),
                    label=dmc.Text("Overview", weight=400),
                    href="/overview",
                    variant="filled",
                    active=True,
                    color="purple",
                    id='sidebar-overview'
                ),
                dmc.NavLink(
                    icon=get_icon(icon="ph:presentation-chart"),
                    label=dmc.Text("Compare", weight=400),
                    href="/compare",
                    variant="filled",
                    active=True,
                    color="purple",
                    id='sidebar-compare'
                ),
                dmc.NavLink(
                    label=dmc.Text("Data", weight=400),
                    icon=get_icon(icon="bxs:data"),
                    href="/data",
                    variant="filled",
                    active=False,
                    id='sidebar-data'
                ),
                dmc.NavLink(
                    label=dmc.Text("About", weight=400),
                    icon=get_icon(icon="material-symbols:info"),
                    href="/about",
                    variant="filled",
                    active=False,
                    id='sidebar-about'
                ),
            ],
                vertical=True,
                pills=True,
            ),
        ]
    ),
], style=SIDEBAR_STYLE)


footer = html.Div(
    html.Footer(
        [
            html.A([
                html.Img(src=config.template.kansas_corn_logo, className="sidebarLogo", style={
                    'width': '5%', 'height': 'auto'}),
            ], href=config.kansas_corn_url, target='_blank'),
            html.A([
                html.Img(src=config.template.CSI_logo, className="sidebarLogo", style={
                    'width': '7%', 'height': 'auto'}),
            ], href=config.CSI_url, target='_blank'),
            html.A([
                html.Img(src=config.template.logo_src, className="sidebarLogo", style={
                    'width': '3%', 'height': 'auto'}),
            ], href=config.ciampitti_url, target='_blank'),
            html.A([
                html.Img(src=config.template.id3a_logo, className="sidebarLogo", style={
                    'width': '18%', 'height': 'auto'}),
            ], href=config.id3a_url, target='_blank'),
        ],
        className="text-center footer",
    ),
)
