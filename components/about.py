import dash_bootstrap_components as dbc
from dash import dcc, html

layout = html.Div([
    html.H1('About'),
    dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
    html.Br()
])
