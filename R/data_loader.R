library(dplyr)
library(readr)

maize <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Maize.csv")
maizeSites <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Maize_Sites.csv") 
soybean <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Soybean.csv")
soybeanSites <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Soybean_Sites.csv")

df_list = list(
  "Maize" = maize,
  "Maize Sites" = maizeSites,
  "Soybean" = soybean,
  "Soybean Sites" = soybeanSites
)