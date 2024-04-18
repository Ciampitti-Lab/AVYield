import io
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv("datasets/corn.csv")
# df = pd.read_csv("datasets/test.csv")


# What are the inputs?
# - Crop
# - State
# - County_City
# - Year
def year_bar(df):
    _df = df[(df["YEAR"].isin([2023])) & (df["COUNTY_CITY"] == "RILEY")].groupby(
        ["NAME", "WATER_REGIME", "COUNTY_CITY"]
    )["YIELD"].mean().reset_index()
    fig = px.bar(_df, x="YIELD", y="NAME", color="WATER_REGIME",
                 barmode = "group",
                 title = "Yearly Yield Trend")

    fig.show()


year_bar(df)


def year_trend(df):
    df["YEAR"] = df["YEAR"].astype(str)
    years = ["2017", "2018", "2019", "2022", "2023"]
    _df = df[df["YEAR"].isin(years)].groupby([
        "NAME", "YEAR"])["YIELD"].mean().reset_index()

    fig = px.line(_df, x="YEAR", y="YIELD", color="NAME", markers=True,
                  category_orders = {"YEAR": years},
                  title = "Yearly Yield Trend")
    fig.show()


# year_trend(df)


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
    fig.for_each_annotation(lambda a: a.update(
        text=a.text.replace("BRAND=", "")))

    fig.show()


# brand_trendline(df)

def show_on_plt(fig):
    img_bytes = fig.to_image(format="png")
    img = mpimg.imread(io.BytesIO(img_bytes), format='PNG')
    plt.figure(figsize=(10, 8))
    plt.imshow(img)
    plt.show()


"""
Will be scrapping this visualization for a while. It's not very useful and
we are already providing that kind of info on the first graph.

Env mean:
    year x county_city = E x_Mean

Questions:
    - Do I need to plot the env_mean attributes (year, county_city)?
    - Is the current implementation correct?
    - What is the user input? Brand?
    -
"""


def env_mean(df):
    _df = df.copy()
    _df["ENV_MEAN"] = _df.groupby(["YEAR", "COUNTY_CITY"])[
        "YIELD"].transform("mean")
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
    fig.for_each_annotation(lambda a: a.update(
        text=a.text.replace("Name=", "")))
    fig.show()
    # show_on_plt(fig)


# env_mean(df)
