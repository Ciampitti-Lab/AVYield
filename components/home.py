from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash_player as dp

layout = html.Div([
    html.Div(
        dbc.Container(
            [
                html.H1(
                    "Crop Trials Analysis Tool",
                    className="display-2",
                    style={
                        "color": "white",
                        "text-shadow": "3px 3px 4px rgba(0, 0, 0, 0.4)",
                        "font-weight": "400"
                    }
                ),
                html.P(
                    "Short explanation about eh tool will go here.",
                    className="lead ",
                    style={
                        "color": "white",
                        "text-shadow": "2px 2px 3px rgba(0, 0, 0, 0.75)",
                    }
                ),
                html.Hr(className="my-2", style={"color": "white"}),
                html.P(
                    "General info about the dashboard will go here.",
                    style={
                        "color": "white",
                        "text-shadow": "2px 2px 3px rgba(0, 0, 0, 0.75)",
                        "font-weight": "400",
                        "margin-bottom": "1px"
                    }
                ),
                html.P(
                    "Analytical overview explanation will go here.",
                    style={
                        "color": "white",
                        "text-shadow": "2px 2px 3px rgba(0, 0, 0, 0.75)",
                        "font-weight": "400",
                        "margin-bottom": "1px"
                    }
                ),
                html.P(
                    "Download the data info will go here.",
                    style={
                        "color": "white",
                        "text-shadow": "2px 2px 3px rgba(0, 0, 0, 0.75)",
                        "font-weight": "400",
                        "margin-bottom": "20px"
                    }
                ),
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
                        # title='Tutorial',
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
                ], className="lead"),
            ],
            fluid=True, className="py-3 "
        ),
        className="p-3 bg-light rounded-5 home-jumbotron shadows-jumbotron"
    )
])
