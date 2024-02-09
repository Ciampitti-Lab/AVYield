import pandas as pd
from config import config

canola = pd.read_csv(config.data.canola_path)
corn = pd.read_csv(config.data.corn_path)
sorghum = pd.read_csv(config.data.sorghum_path)
soybean = pd.read_csv(config.data.soybean_path)
sunflower = pd.read_csv(config.data.sunflower_path)
wheat = pd.read_csv(config.data.wheat_path)
county_data = pd.read_csv(config.data.county_path)

datasets = {
    "Canola": canola,
    "Corn": corn,
    "Sorghum": sorghum,
    "Soybean": soybean,
    "Sunflower": sunflower,
    "Wheat": wheat,
}
