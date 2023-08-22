import pandas as pd
from config import config

corn = pd.read_csv(config.data.corn_path)
soybean = pd.read_csv(config.data.soybean_path)
sunflower = pd.read_csv(config.data.sunflower_path)
wheat = pd.read_csv(config.data.wheat_path)
county_data = pd.read_csv(config.data.county_path)


def drop_duplicates_by_year(df):
    grouped = df.groupby("YEAR")
    non_duplicate_df = pd.DataFrame(columns=df.columns)

    for year, group in grouped:
        duplicate_rows = group[group.duplicated(
            subset=['NAME', 'COUNTY', 'WATER_REGIME'], keep=False)]
        non_duplicate_rows = group.drop(duplicate_rows.index)
        non_duplicate_df = pd.concat([non_duplicate_df, non_duplicate_rows])

    non_duplicate_df.reset_index(drop=True, inplace=True)
    return non_duplicate_df


# Corn
corn.YEAR = corn.YEAR.astype(int)

corn = corn.drop_duplicates()
corn.dropna(subset=["NAME"], inplace=True)
corn = drop_duplicates_by_year(corn)

brand_elements = ["MAT CHK", "MATURITY CHECK",
                  "zMATURITY CHECK", "-MATURITY CHECK"]
name_elements = ["MEAN", "CV", "LSD", "Average",
                 "CV (%)", "LSD (0.5)", "MATURITY SHORT", "MATURITY MID", "MATURITY FULL", "GRAND MEAN"]
corn = corn[~corn['BRAND'].isin(brand_elements)]
corn = corn[~corn['NAME'].isin(name_elements)]
corn.reset_index(drop=True, inplace=True)

# Soybean
soybean = soybean.drop_duplicates()
soybean.dropna(subset=["NAME"], inplace=True)
soybean = drop_duplicates_by_year(soybean)

# Sunflower
sunflower = sunflower.drop_duplicates()
sunflower.dropna(subset=["NAME"], inplace=True)
sunflower = drop_duplicates_by_year(sunflower)

# Wheat
wheat = wheat.drop_duplicates()
wheat.dropna(subset=["NAME"], inplace=True)
wheat = drop_duplicates_by_year(wheat)

wheat = wheat[~wheat['NAME'].isin(["AVERAGE", "GRAND MEAN"])]
wheat.reset_index(drop=True, inplace=True)


datasets = {
    "Corn": corn,
    "Soybean": soybean,
    "Sunflower": sunflower,
    "Wheat": wheat,
}
