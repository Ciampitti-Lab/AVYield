import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("datasets/corn.csv")
# df = pd.read_csv("datasets/test.csv")


def brand_trendline(df):
    mostFreqBrands = df.BRAND.value_counts().head(3).index.tolist()
    _df = (
        df[df["BRAND"].isin(mostFreqBrands)]
        .groupby(["YEAR", "BRAND"])["YIELD"]
        .mean()
        .reset_index()
    )

    fig = px.scatter(
        _df,
        x="YEAR",
        y="YIELD",
        facet_col="BRAND",
        trendline="rolling",
        trendline_options=dict(window=3),
        title="Yearly Yield Trend",
    )

    # fig = px.scatter(_df, x='YEAR', y='YIELD', color='BRAND', trendline='rolling', trendline_options=dict(window=5), title='Yearly Yield Trend')
    # fig.update_traces(showlegend=True)

    fig.data = [t for t in fig.data if t.mode == "lines"]
    fig.for_each_annotation(lambda a: a.update(text=a.text.replace("BRAND=", "")))

    fig.show()


# brand_trendline(df)

"""
Env mean:
    year x county_city = E x_Mean

Questions:
    - Do I need to plot the env_mean attributes (year, county_city)?
    - Is the current implementation correct?
    - What is the user input? Brand?
"""


def env_mean(df):
    _df = df.copy()
    _df["ENV_MEAN"] = _df.groupby(["YEAR", "COUNTY_CITY"])["YIELD"].transform("mean")
    _df = (
        _df[df["BRAND"].isin(["DEKALB", "FRONTIER", "PIONEER"])]
        .groupby(["BRAND", "ENV_MEAN", "WATER_REGIME"])["YIELD"]
        .mean()
        .reset_index()
    )

    fig = px.scatter(
        _df,
        x="ENV_MEAN",
        y="YIELD",
        color="WATER_REGIME",
        facet_col="BRAND",
        title="Brand Yield x Env Mean thoughout the years",
    )

    fig.add_shape(
        type="line",
        x0=min(_df["ENV_MEAN"]),
        x1=max(_df["ENV_MEAN"]),
        y0=min(_df["ENV_MEAN"]),
        y1=max(_df["ENV_MEAN"]),
        line=dict(color="black", width=2, dash="dash"),  
        row="all",
        col="all",
    )

    fig.update_traces(marker={"size": 10})
    fig.for_each_annotation(lambda a: a.update(text=a.text.replace("Name=", "")))

    fig.show()


env_mean(df)
