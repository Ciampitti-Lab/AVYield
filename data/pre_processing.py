import os
import pandas as pd
from config import config


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
    df.to_csv(config.data.soybean_path, index=False)


def get_low_data_cols(df):
    # Return list of columns with usable data < 10%
    percent_usable_data = (len(df) - df.isna().sum()) / len(df) * 100
    return [index for index, value in percent_usable_data.items() if value < 10.00]


def drop_low_data_cols(df):
    low_cols = get_low_data_cols(df)
    if len(low_cols) > 0:
        df.drop(columns=low_cols, inplace=True)


# Datasets assignment
corn = pd.read_csv(config.data.corn_path)
soybean = pd.read_csv(config.data.soybean_path)
sunflower = pd.read_csv(config.data.sunflower_path)
wheat = pd.read_csv(config.data.wheat_path)
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
        * Change 1 to Dryland and 2 to Irrigated in WATER REGIME field.
        * Change BRAND and NAME missing values to "Unknown"? For now I won't.
        * Drop columns with low usable data.
    - Soybean:
        * Change BRAND and NAME missing values to "Unknown"? For now I won't.
        * Drop columns with low usable data.
    - Sunflower:
        * Change BRAND and NAME missing values to "Unknown"? For now I won't.
        * Drop columns with low usable data.
    - Wheat:
        * Change BRAND and NAME missing values to "Unknown"? For now I won't.
        * Change MOIST missing values to 0? For now I won't.
        * Drop columns with low usable data.
'''
for _, dataset in datasets.items():
    drop_low_data_cols(dataset)
