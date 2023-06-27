import os
import pandas as pd

corn_path = "raw/1982-2020_corn.csv"
corn_save_path = "datasets/corn.csv"
soybean_path = "raw/1991-2022_soybean.csv"
soybean_save_path = "datasets/soybean.csv"
sunflower_path = "raw/1998-2019_sunflower.csv"
sunflower_save_path = "datasets/sunflower.csv"
wheat_path = "raw/1982-2022_wheat.csv"
wheat_save_path = "datasets/wheat.csv"

county_acronyms_path = "raw/county_dict.csv"
county_geodata_path = "raw/us-county-boundaries.csv"

save_paths = [corn_save_path, soybean_save_path,
              sunflower_save_path, wheat_save_path]


def convert_xlsx_to_csv(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file_name)
            csv_file_name = file_name.replace(".xlsx", ".csv")
            csv_file_path = os.path.join(folder_path, csv_file_name)
            df = pd.read_excel(file_path)
            df.to_csv(csv_file_path, index=False)
            print(f"Converted '{file_name}' to '{csv_file_name}'.")


def modify_corn_data(df):
    df['WATER_REGIME'] = df['WATER_REGIME'].astype(str).str[0]
    df['WATER_REGIME'] = df['WATER_REGIME'].replace(
        {'1': 'Dryland', '2': 'Irrigated'})
    df.to_csv(soybean_path, index=False)


def get_low_data_cols(df):
    # Return list of columns with usable data < 10%
    percent_usable_data = (len(df) - df.isna().sum()) / len(df) * 100
    return [index for index, value in percent_usable_data.items() if value < 10.00]


def drop_low_data_cols(df):
    low_cols = get_low_data_cols(df)
    if len(low_cols) > 0:
        df.drop(columns=low_cols, inplace=True)


def split_LOC(df, c_dict):
    df['COUNTY'] = df['LOC'].str[:2].map(
        c_dict
    ).fillna("Unknown")

    df['WATER_REGIME'] = df['LOC'].str[2].map(
        {'I': 'Irrigated',
         'i': 'Irrigated',
         'D': 'Dryland',
         'd': 'Dryland'
         }
    )
    return df


county_acronyms = pd.read_csv(county_acronyms_path)
county_geodata = pd.read_csv(county_geodata_path)
county_acronyms_dict = dict(
    zip(county_acronyms['ACRONYM'], county_acronyms['COUNTY']))


# Datasets assignment
corn = pd.read_csv(corn_path)
soybean = pd.read_csv(soybean_path)
sunflower = pd.read_csv(sunflower_path)
wheat = pd.read_csv(wheat_path)
datasets = {
    "Corn": corn,
    "Soybean": soybean,
    "Sunflower": sunflower,
    "Wheat": wheat
}

'''
Datasets changes and fixes:
* Filter the dataset by year initially? I think so.
    - Corn:
        * Change 1 to Dryland and 2 to Irrigated in WATER REGIME field. (Done)
        * Change BRAND and NAME missing values to "Unknown"? (For now I won't).
        * Drop columns with low usable data. (Done)
        * Map COUNTY in new column LOC. (Done)
    - Soybean:
        * Change BRAND and NAME missing values to "Unknown"? (For now I won't).
        * Drop columns with low usable data. (Done)
        * Split LOC in County, Water Regime. (Done)
    - Sunflower:
        * Change BRAND and NAME missing values to "Unknown"? (For now I won't).
        * Drop columns with low usable data. (Done)
        * Split LOC in County, Water Regime. (Done)
    - Wheat:
        * Change BRAND and NAME missing values to "Unknown"? (For now I won't).
        * Change MOIST missing values to 0? (For now I won't).
        * Drop columns with low usable data. (Done)
        * Split LOC in County, Water Regime. (Done)
'''
for (name, dataset), save_path in zip(datasets.items(), save_paths):
    # Drop low data cols
    drop_low_data_cols(dataset)

    if name == "Corn":
        # Corn: Map COUNTY in new column LOC.
        dataset['LOC'] = (dataset['COUNTY'].str.upper()).map(
            {value: key for key, value in county_acronyms_dict.items()})
    else:
        # Soybean, Sunflower, Wheat: Split LOC in County, Water Regime.
        dataset = split_LOC(dataset, county_acronyms_dict)

    # Save
    dataset.to_csv(save_path, index=False)


# County dataset
county_geodata.COUNTY = county_geodata['COUNTY'].str.upper()
county_data = pd.merge(county_geodata, county_acronyms, on='COUNTY')
county_data = county_data.sort_values(by='ACRONYM')
county_data = county_data.reset_index(drop=True)
county_data.to_csv("datasets/county_data.csv", index=False)



