import pandas as pd
from config import config

corn = pd.read_csv(config.data.corn_path)
soybean = pd.read_csv(config.data.soybean_path)
sunflower = pd.read_csv(config.data.sunflower_path)
wheat = pd.read_csv(config.data.wheat_path)
county_data = pd.read_csv(config.data.county_path)
datasets = {
    "Corn": corn,
    "Soybean": soybean,
    "Sunflower": sunflower,
    "Wheat": wheat, 
}
