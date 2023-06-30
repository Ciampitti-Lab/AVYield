from data.pre_processing import datasets
import plotly.express as px
import pandas as pd
import numpy as np


def print_data(selected_crop):
    print("Selected crop: ", selected_crop)
    print(datasets[selected_crop].head())


def get_year_interval(selected_crop):
    dataset = datasets[selected_crop]
    return [{'label': str(year), 'value': year} for year in dataset['YEAR'].unique()]


def yield_brand(selected_crop, selected_year):
    df = datasets[selected_crop]
    yield_brand = df[df['YEAR'] == selected_year]
    color_map = {'Irrigated': 'darkblue', 'Dryland': 'orange'}
    swarm = px.strip(yield_brand, x='BRAND', y='YIELD', title='Yield per Brand', color='WATER_REGIME',
                     color_discrete_map=color_map, hover_data=sorted(list(yield_brand.columns)))
    return swarm


def yield_year(selected_crop):
    df = datasets[selected_crop]
    if selected_crop == "Corn" or selected_crop == "Wheat":
        median_yield_year = df.groupby('YEAR').agg(
            {'YIELD': 'median', 'MOIST': 'median'}).reset_index()
        color_col = 'MOIST'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year', 'MOIST': 'Moist'}
        color_cont_scale = px.colors.sequential.Aggrnyl
    else:
        median_yield_year = df.groupby('YEAR')['YIELD'].median().reset_index()
        color_col = 'YIELD'
        labels_dict = {'YIELD': 'Yield', 'YEAR': 'Year'}
        color_cont_scale = px.colors.sequential.Bluered

    year_yield_bar = px.bar(
        median_yield_year,
        x='YEAR',
        y='YIELD',
        color=color_col,
        title='Yield per Year',
        labels=labels_dict,
        color_continuous_scale=list(reversed(color_cont_scale))
    )
    return year_yield_bar
