from dash import dcc, html
from data.pre_processing import county_data

layout = html.Div(
    [
        # html.H1('Select a County in Kansas'),
        # dcc.Dropdown(
        #     id='county-dropdown',
        #     options=[{'label': county, 'value': county}
        #              for county in county_data['COUNTY']],
        #     value=county_data['COUNTY'].iloc[0]
        # ),
        html.H1('Yield per Brand'),
        html.H3('Year'),
        dcc.Dropdown(
            id='yield-brand-dropdown',
            value=2019
        ),
        dcc.Graph(id='yield-brand-graph'),

        html.H1('Yield per Year'),
        dcc.Graph(id='yield-year-graph'),
    ]
)
