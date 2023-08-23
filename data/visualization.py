from data.pre_processing import datasets
from dash import dash_table
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import geopandas as gpd
import pandas as pd
import numpy as np
from config import config
import json


# General methods
def print_data(selected_crop):
    print("Selected crop: ", selected_crop)
    print(datasets[selected_crop].head())


def get_dataset(selected_crop):
    return datasets[selected_crop]


def set_mean_yield_bar_graph(df, crop, title):
    if crop == 'Corn' or crop == 'Wheat':
        mean_yield_year = df.groupby('YEAR').agg(
            {'YIELD': lambda x: round(x.mean(), 2),
             'MOIST': lambda x: round(x.mean(), 2)}
        ).reset_index()
        color_col = 'MOIST'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year', 'MOIST': 'Moist'}
        color_cont_scale = px.colors.sequential.Aggrnyl
    elif crop == 'Sunflower':
        mean_yield_year = df.groupby('YEAR').agg(
            {'YIELD': lambda x: round(x.mean(), 2),
             'DAYS': lambda x: round(x.mean(), 2)}
        ).reset_index()
        color_col = 'DAYS'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year', 'DAYS': 'Days'}
        color_cont_scale = px.colors.sequential.Viridis
    else:
        mean_yield_year = df.groupby('YEAR')['YIELD'].mean().reset_index()
        mean_yield_year['YIELD'] = round(mean_yield_year['YIELD'], 2)
        color_col = 'YIELD'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year'}
        color_cont_scale = px.colors.sequential.Bluered

    return px.bar(
        mean_yield_year,
        x='YEAR',
        y='YIELD',
        color=color_col,
        title=title,
        labels=labels_dict,
        color_continuous_scale=list(reversed(color_cont_scale))
    )


# Bar - Brand Yield per year
def brand_year(selected_crop, selected_brand):
    df = datasets[selected_crop]
    brand = df[df['BRAND'] == selected_brand]
    brand.loc[:, 'YEAR'] = brand['YEAR'].astype(str)
    return set_mean_yield_bar_graph(brand, selected_crop, 'Mean Brand Yield Per Year')


# Swarm - Yield per brand
def yield_brand(selected_crop, selected_year):
    df = datasets[selected_crop]
    yield_brand = df[df['YEAR'] == selected_year]
    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    swarm = px.strip(yield_brand, x='BRAND', y='YIELD', title='Yield per Brand', color='WATER_REGIME',
                     color_discrete_map=color_map, hover_data=sorted(
                         list(yield_brand.columns)),
                     labels={'BRAND': 'Brand', 'YIELD': 'Yield', 'WATER_REGIME': 'Water Regime'})
    return swarm


# Lollipop - Mean Yield per Location by Year
def mean_yield_county(selected_crop, year_value):
    df = datasets[selected_crop]
    mean_yield_county = df[df.YEAR == year_value].groupby('COUNTY').agg(
        {'YIELD': lambda x: round(x.mean(), 2)}).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=mean_yield_county["COUNTY"],
        y=mean_yield_county["YIELD"],
        mode='markers',
        marker=dict(
            color='darkblue',
            size=10
        )
    ))
    for i in range(0, len(mean_yield_county)):
        fig.add_shape(type='line',
                      x0=i, y0=0,
                      x1=i,
                      y1=mean_yield_county["YIELD"][i],
                      line=dict(color='darkblue', width=3))
    fig.update_layout(title_text="Mean Yield per County by Year")

    return fig


# Map - Total Yield per County by Year
def total_yield_county(selected_crop, year_value):
    df = datasets[selected_crop]
    df = df[df.YEAR == year_value].groupby(
        "COUNTY")["YIELD"].sum().reset_index()
    df.rename(columns={"COUNTY": "name"}, inplace=True)
    df['name'] = df['name'].apply(lambda x: x.capitalize())

    with open(config.data.geodata_path) as f:
        geodata = json.load(f)

    names_list = [feature['properties']['name']
                  for feature in geodata['features']]
    missing_names_df = pd.DataFrame(
        {'name': [name for name in names_list if name not in df['name'].values], 'YIELD': 0})
    total_yield_county = pd.concat([df, missing_names_df], ignore_index=True)

    fig = px.choropleth_mapbox(
        total_yield_county,
        geojson=geodata,
        featureidkey="properties.name",
        locations="name",
        color="YIELD",
        color_continuous_scale="Sunsetdark",
        zoom=5.5,  # type: ignore
        center={"lat": 38.5, "lon": -98.5},
        mapbox_style="carto-positron",
        title='Total Yield Per County by Year',
        labels={'name': 'County', 'YIELD': 'Yield'}
    )

    return fig


# Bar - Mean Yield per year
def yield_year(selected_crop):
    return set_mean_yield_bar_graph(datasets[selected_crop], selected_crop, 'Mean Yield per Year')


# Table data
def table(selected_crop):
    df = datasets[selected_crop]

    columns_to_select = ['YEAR', 'YIELD', 'COUNTY', 'BRAND', 'NAME']
    if 'PCODE' in df.columns:
        columns_to_select.append('PCODE')
    df = df[columns_to_select]

    df.loc[:, 'YIELD'] = df['YIELD'].round(2)
    df = df.sort_values('YEAR', ascending=False)

    return df.to_dict('records')


# Compare Yield Bar Graph
def compare_yield_bar(selected_crop, first_opt, second_opt, filter, legend_flag):
    df = datasets[selected_crop]
    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    col1, col2 = ('YEAR', 'NAME') if filter == 'genotype' else ('NAME', 'YEAR')
    df = df[df[col1] == first_opt]
    df = df[df[col2].isin(second_opt)].groupby(
        [col2, 'WATER_REGIME'])['YIELD'].mean().reset_index()
    fig = px.bar(df, x=col2, y='YIELD',
                 color_discrete_map=color_map,
                 color='WATER_REGIME', barmode='group',
                 labels={'NAME': 'Name', 'YIELD': 'Yield',
                         'WATER_REGIME': 'Water Regime', 'YEAR': 'Year'})
    fig.update_layout(showlegend=legend_flag)
    fig.update_layout(title={'text': f"{first_opt} Yield"})
    return fig


# Compare Yield Box graph
def compare_yield_box(selected_crop, first_opt, second_opt, filter, legend_flag):
    df = datasets[selected_crop]
    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    col1, col2 = ('YEAR', 'NAME') if filter == 'genotype' else ('NAME', 'YEAR')
    df = df[df[col1] == first_opt]
    df = df.loc[df[col2].isin(second_opt)]
    fig = px.box(
        df,
        x=col2,
        y='YIELD',
        color_discrete_map=color_map,
        color='WATER_REGIME',
        labels={'MOIST': 'Moist', 'YIELD': 'Yield',
                'WATER_REGIME': 'Water Regime', 'NAME': 'Name', 'DAYS': 'Days'},
    )
    fig.update_layout(showlegend=legend_flag)
    return fig


# Compare County Map
def compare_county_map(selected_crop, first_opt, second_opt, filter):
    col1, col2 = ('YEAR', 'NAME') if filter == 'genotype' else ('NAME', 'YEAR')
    df = datasets[selected_crop]
    df = df[df[col1] == first_opt]
    df = df[df[col2].isin(second_opt)].groupby(
        ['COUNTY'])['YIELD'].sum().reset_index()
    df["COUNTY"] = df["COUNTY"].apply(lambda x: x.capitalize())

    with open(config.data.geodata_path) as f:
        geodata = json.load(f)

    names_list = [feature['properties']['name']
                  for feature in geodata['features']]
    missing_names_df = pd.DataFrame(
        {'COUNTY': [name for name in names_list if name not in df['COUNTY'].values], 'YIELD': 0})
    total_yield_county = pd.concat([df, missing_names_df], ignore_index=True)

    fig = px.choropleth_mapbox(
        total_yield_county,
        geojson=geodata,
        featureidkey="properties.name",
        locations="COUNTY",
        color="YIELD",
        color_continuous_scale="Sunsetdark",
        zoom=5.5,  # type: ignore
        center={"lat": 38.5, "lon": -98.5},
        mapbox_style="carto-positron",
        title='Por nome significativo',
        labels={'name': 'County', 'YIELD': 'Yield'}
    )

    return fig
