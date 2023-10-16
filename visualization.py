from dash import dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
import db

conversion_rates = {  # From bu/ac
    'bu-ac': {
        'Corn': 1,
        'Wheat': 1,
        'Soybean': 1,
        'Sunflower': 1,
    },
    'lb-ac': {
        'Corn': 62.77/1.121,
        'Wheat': 67.25/1.121,
        'Soybean': 67.25/1.121,
        'Sunflower': 33.625/1.121,
    },
    'mg-ha': {
        'Corn': 0.0628,
        'Wheat': 0.0673,
        'Soybean': 0.0673,
        'Sunflower': 0.0336,
    },
    'kg-ha': {
        'Corn': 62.77,
        'Wheat': 67.25,
        'Soybean': 67.25,
        'Sunflower': 33.625,
    }
}


# Table data
# def table(selected_crop):
#     df = datasets[selected_crop]

#     columns_to_select = ['YEAR', 'YIELD', 'COUNTY', 'BRAND', 'NAME']
#     if 'PCODE' in df.columns:
#         columns_to_select.append('PCODE')
#     df = df[columns_to_select]

#     df.loc[:, 'YIELD'] = df['YIELD'].round(2)
#     df = df.sort_values('YEAR', ascending=False)

#     return df.to_dict('records')


# Compare Yield Bar Graph
def compare_yield_bar(selected_crop, first_opt, second_opt, unit, filter, legend_flag):
    conv_rate = conversion_rates.get(unit, {}).get(selected_crop, None)
    unit_str = unit.replace('-', '/').replace('m', 'M')

    df, col2 = db.get_compare_df(
        selected_crop, filter, first_opt, second_opt, conv_rate
    )
    df = df.groupby([col2, 'WATER_REGIME'])['YIELD'].mean().reset_index()

    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    fig = px.bar(df, x=col2, y='YIELD',
                 color_discrete_map=color_map,
                 color='WATER_REGIME', barmode='group',
                 labels={'NAME': 'Genotype', 'YIELD': f'Yield ({unit_str})',
                         'WATER_REGIME': 'Water Regime', 'YEAR': 'Year'})
    fig.update_layout(showlegend=legend_flag)
    fig.update_layout(
        title={
            'text': f"{first_opt} Average Yield for the Selected {filter.capitalize()}(s)"},
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# Compare Yield Box graph
def compare_yield_box(selected_crop, first_opt, second_opt, unit, filter, legend_flag):
    conv_rate = conversion_rates.get(unit, {}).get(selected_crop, None)
    unit_str = unit.replace('-', '/').replace('m', 'M')

    df, col2 = db.get_compare_df(
        selected_crop, filter, first_opt, second_opt, conv_rate
    )

    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    fig = px.box(
        df,
        x=col2,
        y='YIELD',
        color_discrete_map=color_map,
        color='WATER_REGIME',
        labels={'MOIST': 'Moist', 'YIELD': f'Yield ({unit_str})',
                'WATER_REGIME': 'Water Regime', 'NAME': 'Genotype', 'DAYS': 'Days'},
    )

    fig.update_layout(showlegend=legend_flag)
    fig.update_layout(
        title={'text': f"{first_opt} Yield Distribution Box Plot for the Selected {filter.capitalize()}(s)"},
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# Compare County Bar
def compare_county_yield_bar_graph(selected_crop, first_opt, second_opt, unit, filter):
    conv_rate = conversion_rates.get(unit, {}).get(selected_crop, None)
    unit_str = unit.replace('-', '/').replace('m', 'M')

    df, col2 = db.get_compare_df(
        selected_crop, filter, first_opt, second_opt, conv_rate
    )

    df = df[[col2, 'WATER_REGIME', 'COUNTY', 'YIELD']]

    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    fig = px.bar(df, x='COUNTY', y='YIELD',
                 color_discrete_map=color_map,
                 facet_col=col2,
                 color='WATER_REGIME', barmode='group',
                 labels={'NAME': 'Name', 'YIELD': f'Yield ({unit_str})',
                         'WATER_REGIME': 'Water Regime', 'YEAR': 'Year', 'COUNTY': 'County'})

    fig.for_each_annotation(lambda a: a.update(
        text=a.text.replace("Name=", ""))
    )
    fig.for_each_xaxis(lambda x: x.update({'title': ''}))
    fig.update_layout(
        title={
            'text': f"Yield Distribution by County for the Selected {filter.capitalize()}(s)"},
        paper_bgcolor="rgba(0,0,0,0)",
    )
    fig.add_annotation(
        showarrow=False,
        xanchor='center',
        xref='paper',
        x=0.5,
        yref='paper',
        y=-0.26,
        text='County'
    )
    return fig


# Compare County Map
def compare_county_map(selected_crop, first_opt, second_opt, unit, filter):
    conv_rate = conversion_rates.get(unit, {}).get(selected_crop, None)
    unit_str = unit.replace('-', '/').replace('m', 'M')

    df, _ = db.get_compare_df(
        selected_crop, filter, first_opt, second_opt, conv_rate
    )
    df = df.groupby(['COUNTY'])['YIELD'].mean().reset_index()
    df["COUNTY"] = df["COUNTY"].apply(lambda x: x.capitalize())

    geodata = json.loads(db.get_geodata())

    names_list = [feature['properties']['name']
                  for feature in geodata['features']]
    missing_names_df = pd.DataFrame(
        {'COUNTY': [name for name in names_list if name not in df['COUNTY'].values], 'YIELD': 0})

    total_yield_county = pd.concat([df, missing_names_df], ignore_index=True)
    total_yield_county['YIELD'] = total_yield_county['YIELD'].round(2)
    total_yield_county['YIELD'] = total_yield_county['YIELD'].round(2)
    zero_yield_df = total_yield_county[total_yield_county['YIELD'] == 0]
    non_zero_yield_df = total_yield_county[total_yield_county['YIELD'] != 0]

    trace_zero_yield = go.Choroplethmapbox(
        geojson=geodata,
        featureidkey="properties.name",
        locations=zero_yield_df['COUNTY'],
        z=zero_yield_df['YIELD'],
        colorscale=[[0, "white"], [1, "white"]],
        showscale=False
    )

    trace_non_zero_yield = go.Choroplethmapbox(
        geojson=geodata,
        featureidkey="properties.name",
        locations=non_zero_yield_df['COUNTY'],
        z=non_zero_yield_df['YIELD'],
        colorscale="Sunsetdark",
        showscale=True,
        colorbar=dict(title=f'Yield ({unit_str})')
    )

    fig = go.Figure(data=[trace_zero_yield, trace_non_zero_yield])
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=5.2,
        mapbox_center={"lat": 38.5, "lon": -98.5},
        title='County-Level Genotype Average Yield Map',
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig
