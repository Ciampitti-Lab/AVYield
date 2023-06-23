# Dashboard Project

## References

* [Bootswatch theme](https://bootswatch.com/lumen/)
* [Reference Project](https://github.com/fiakoenjiniring/rainfall/tree/main)
* [Reference site - 1](http://ramwheatdb.com/headtohead.php)
* [Reference site - 2](https://www.myfields.info/crop-data)
* [Geo Data](https://public.opendatasoft.com/explore/dataset/us-county-boundaries)

## Initial notes
Lots of work to do =/

## To-do

- [x] Add datasets from ignacio email.
- [x] Fix new datasets.
- [x] Pre-process the datasets.
- [x] Fix, LOC, WATER_REGIME and COUNTY fields
- [x] Pre-pre-process the datasets outside the app to maintain high performance. 
- [ ] Store only a fixed set of columns. Setup this columns in config.
- [ ] Add year selection and filter datasets initially.
- [x] Create home, about and data pages.
- [x] Collect Kansas geo data.
- [ ] Create pages layout for home, about and data.
- [ ] Change pre_processing.py to get the datasets from the documentation repo.
- [ ] CHECK UNITS IN THE xlsx FILES!
- [x] Fix harvest_date unit.
- [x] Figure site/loc acronyms: The location "code" is the 2-letter county abbreviation and "D" for dryland or "I" for irrigated for all crops. A "S" in wheat or corn is a soft test or a short season test and "C" and "O" are confectionary and oilseed respectively for sunflower. 

* Visualizations:
- [ ] Explore the datasets relation using as input: year, county, water regime and return: yield per genotype and brand.
- [ ] Water regime and yield.
- [ ] Add climate data.


## Project structure
- app.py
- assets
  - KSU-Crops-logo.png
  - styles.css
- callbacks
  - hf_callbacks.py
  - main_callbacks.py
- components
  - about.py
  - data.py
  - hf.py
  - home.py
- config.py
- config.yml
- data
  - data_exp.ipynb
  - datasets
    - corn.csv
    - county_data.csv
    - soybean.csv
    - sunflower.csv
    - wheat.csv
  - datasets_setup.py
  - outputs
  - pre_processing.py
  - raw
    - 1982-2020_corn.csv
    - 1982-2022_wheat.csv
    - 1991-2022_soybean.csv
    - 1998-2019_sunflower.csv
    - county_dict.csv
    - Data_Comparison_MS_1991_2021_Maize.csv
    - Data_Comparison_MS_1991_2021_Maize_Sites.csv
    - Data_Comparison_MS_1991_2021_Soybean.csv
    - Data_Comparison_MS_1991_2021_Soybean_Sites.csv
    - sunflower_locations.csv
    - us-county-boundaries.csv
  - visualization.py
- README.md
