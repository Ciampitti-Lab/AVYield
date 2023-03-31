library(dplyr)
library(readr)

maize <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Maize.csv")
maizeSites <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Maize_Sites.csv") 
soybean <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Soybean.csv")
soybeanSites <- readr::read_csv("data/Data_Comparison_MS_1991_2021_Soybean_Sites.csv")

# The function renderTable() uses xtable to create a html table,
# xtable only can deal with three different classes of columns: logical; character; and numeric
# so it is necessary that "Date" attributes are converted to characters.

convert_dates_to_char <- function(df) {
  df %>%
    mutate_if(~class(.) == "Date", as.character)
}

maizeSites <- convert_dates_to_char(maizeSites)
soybeanSites <- convert_dates_to_char(soybeanSites)


df_list = list(
  "Maize" = maize,
  "Maize Sites" = maizeSites,
  "Soybean" = soybean,
  "Soybean Sites" = soybeanSites
)