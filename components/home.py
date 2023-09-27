from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.H1(
            'Crop Trials Analysis Tool',
            style={'text-align': 'left',
                   'font-weight': '600', 'margin-bottom': '0px'}
        ),
        html.H6(
            'Welcome bla bla bla.',
            style={'text-align': 'left',
                   'color': '#7D7D7D', 'margin-top': '0px', 'margin-bottom': '40px'}
        )
    ]),
    html.Div(
        dbc.Container(
            [
                html.H1("Jumbotron", className="display-3"),
                html.P(
                    "Use Containers to create a jumbotron to call attention to "
                    "featured content or information.",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Use utility classes for typography and spacing to suit the "
                    "larger container."
                ),
                html.P(
                    dbc.Button("Learn more", color="primary"), className="lead"
                ),
            ],
            fluid=True, className="py-3"
        ),
        className="p-3 bg-light rounded-3 homejumbo"
    )
])
