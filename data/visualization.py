from pandas.core.common import count_not_none
from data.pre_processing import datasets
import plotly.express as px
import pandas as pd


conversion_rates = {  # From bu/ac
    "bu-ac": {
        "Canola": 1,
        "Corn": 1,
        "Wheat": 1,
        "Sorghum": 1,
        "Soybean": 1,
        "Sunflower": 1,
    },
    "mg-ha": {
        "Canola": 0.0560,
        "Corn": 0.0628,
        "Wheat": 0.0673,
        "Sorghum": 0.0628,
        "Soybean": 0.0673,
        "Sunflower": 0.0336,
    },
}


# General methods
def get_dataset(selected_crop):
    return datasets[selected_crop]


# Table data
def table(selected_crop):
    df = datasets[selected_crop]

    columns_to_select = ["YEAR", "YIELD", "COUNTY_CITY", "BRAND", "NAME"]
    if "PCODE" in df.columns:
        columns_to_select.append("PCODE")
    df = df[columns_to_select]

    df = df.sort_values("YEAR", ascending=False)

    return df.to_dict("records")


def load_dataset(selected_crop, c_data, custom_crop_value, state):
    if selected_crop != "Custom":
        if c_data is not None and selected_crop == custom_crop_value:
            c_data.NAME = "[USER] " + c_data.NAME
            df = (datasets[selected_crop]).copy(deep=True)
            df = pd.concat([df, c_data], ignore_index=True)
            df.sort_values(by=["YEAR"])
            df = df[df.STATE == state]
        else:
            df = (datasets[selected_crop]).copy(deep=True)
            df = df[df.STATE == state]
        c_unit = selected_crop
    else:
        df = c_data.copy(deep=True)
        df = df[df.STATE == state]
        c_unit = custom_crop_value
    return df, c_unit


# Compare Yield Bar Graph
def compare_yield_bar(
    selected_crop,
    first_opt,
    second_opt,
    state,
    unit,
    filter,
    legend_flag,
    c_data,
    custom_crop_value,
):
    df, c_unit = load_dataset(selected_crop, c_data, custom_crop_value, state)
    conv_rate = conversion_rates.get(unit, {}).get(c_unit, None)

    unit_str = unit.replace("-", "/").replace("m", "M")
    df.YIELD = df.YIELD * conv_rate

    color_map = {"Irrigated": "darkblue", "Dryland": "orange"}
    col1, col2 = ("YEAR", "NAME") if filter == "genotype" else ("NAME", "YEAR")
    df = df[df[col1] == first_opt]
    df = (
        df[df[col2].isin(second_opt)]
        .groupby([col2, "WATER_REGIME"])["YIELD"]
        .mean()
        .reset_index()
    )
    df = df.sort_values(
        by=col2, key=lambda x: x.map(dict(zip(second_opt, range(len(second_opt)))))
    )

    if filter == "year":
        df.YEAR = df.YEAR.astype(str)

    fig = px.bar(
        df,
        x=col2,
        y="YIELD",
        color_discrete_map=color_map,
        color="WATER_REGIME",
        barmode="group",
        labels={
            "NAME": "Genotype",
            "YIELD": f"Yield ({unit_str})",
            "WATER_REGIME": "Water Regime",
            "YEAR": "Year",
        },
    )
    fig.update_layout(showlegend=legend_flag)
    fig.update_layout(
        title={
            "text": f"{first_opt} Average Yield for the Selected {filter.capitalize()}(s)"
        },
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# Compare Yield Box graph
def compare_yield_box(
    selected_crop,
    first_opt,
    second_opt,
    state,
    unit,
    filter,
    legend_flag,
    c_data,
    custom_crop_value,
):
    df, c_unit = load_dataset(selected_crop, c_data, custom_crop_value, state)
    conv_rate = conversion_rates.get(unit, {}).get(c_unit, None)

    unit_str = unit.replace("-", "/").replace("m", "M")
    df.YIELD = df.YIELD * conv_rate
    color_map = {"Irrigated": "darkblue", "Dryland": "orange"}
    col1, col2 = ("YEAR", "NAME") if filter == "genotype" else ("NAME", "YEAR")
    df = df[df[col1] == first_opt]
    df = df.loc[df[col2].isin(second_opt)]
    df = df.sort_values(
        by=col2, key=lambda x: x.map(dict(zip(second_opt, range(len(second_opt)))))
    )

    df.YEAR = df.YEAR.astype(str)

    fig = px.box(
        df,
        x=col2,
        y="YIELD",
        color_discrete_map=color_map,
        color="WATER_REGIME",
        labels={
            "MOIST": "Moist",
            "YIELD": f"Yield ({unit_str})",
            "WATER_REGIME": "Water Regime",
            "NAME": "Genotype",
            "DAYS": "Days",
            "YEAR": "Year",
        },
    )

    fig.update_layout(showlegend=legend_flag)
    fig.update_layout(
        title={
            "text": f"{first_opt} Yield Distribution Box Plot for the Selected {filter.capitalize()}(s)"
        },
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# Compare County/City Bar
def compare_county_yield_bar_graph(
    selected_crop, first_opt, second_opt, state, unit, filter, c_data, custom_crop_value
):
    df, c_unit = load_dataset(selected_crop, c_data, custom_crop_value, state)
    conv_rate = conversion_rates.get(unit, {}).get(c_unit, None)

    unit_str = unit.replace("-", "/").replace("m", "M")
    df.YIELD = df.YIELD * conv_rate  # type: ignore
    color_map = {"Irrigated": "darkblue", "Dryland": "orange"}
    col1, col2 = ("YEAR", "NAME") if filter == "genotype" else ("NAME", "YEAR")
    df = df[df[col1] == first_opt]
    avg_yield_county = df.groupby("COUNTY_CITY")["YIELD"].mean()
    avg_yield_county = pd.DataFrame(avg_yield_county).reset_index()
    avg_yield_county.columns = ["COUNTY_CITY", "avg"]

    df = (
        df[df[col2].isin(second_opt)]
        .groupby([col2, "WATER_REGIME", "COUNTY_CITY"])["YIELD"]
        .mean()
        .reset_index()
    )

    df = df.sort_values(
        by=col2, key=lambda x: x.map(dict(zip(second_opt, range(len(second_opt)))))
    )
    fig = px.bar(
        df,
        x="COUNTY_CITY",
        y="YIELD",
        color_discrete_map=color_map,
        facet_col=col2,
        color="WATER_REGIME",
        barmode="group",
        labels={
            "NAME": "Name",
            "YIELD": f"Yield ({unit_str})",
            "WATER_REGIME": "Water Regime",
            "YEAR": "Year",
            "COUNTY_CITY": "County/City",
        },
    )

    # Add a line trace for each county's average yield
    avg_yield_county.rename(
        columns={"avg": "Average Yield", "COUNTY_CITY": "County/City"}, inplace=True
    )
    for i, county in enumerate(df["COUNTY_CITY"].unique()):
        curr = avg_yield_county[avg_yield_county["County/City"] == county]
        fig.add_trace(
            px.scatter(
                curr,
                x="County/City",
                y="Average Yield",
                color_discrete_sequence=["#6A41D5"],
            ).data[0],
            row="all",
            col="all",
        )
        fig.add_shape(
            type="line",
            x0=i - 0.3,
            x1=i + 0.3,
            y0=curr["Average Yield"].min(),
            y1=curr["Average Yield"].min(),
            row="all",
            col="all",
            line=dict(color="#6A41D5", width=3, dash="dashdot"),
        )

    # Setting the cosmetics
    fig.for_each_annotation(lambda a: a.update(text=a.text.replace("Name=", "")))
    fig.for_each_xaxis(lambda x: x.update({"title": ""}))
    fig.update_layout(
        title={
            "text": f"{first_opt} Yield Distribution by County/City for the Selected {filter.capitalize()}(s)"
        },
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig
