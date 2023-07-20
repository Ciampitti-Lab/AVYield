# Dashboard Project

## References

* [Bootswatch theme](https://bootswatch.com/lumen/)
* [Reference Project](https://github.com/fiakoenjiniring/rainfall/tree/main)
* [Reference site - 1](http://ramwheatdb.com/headtohead.php)
* [Reference site - 2](https://www.myfields.info/crop-data)
* [Geo Data](https://public.opendatasoft.com/explore/dataset/us-county-boundaries)
* https://analytics.iasoybeans.com/cool-apps/ISOFAST/

## Initial Notes
* Scrape almost every vis.
* Focus on genotypes.
  * genotype yield by year.
  * compare yield from 2 genotypes.
  * check data from counties and try something. 
* Process corn dataset to deleted metrics in genotype NAME.
* Drop duplicate rows in the datasets.

## To-do
### Data Engineering
- [x] Add new datasets.
- [x] Collect Kansas geo data.
- [x] Pre-process the datasets.
- [x] Pre-pre-process the datasets outside the main app to maintain high performance. 
- [x] Fix new datasets.
- [x] Fix, LOC, WATER_REGIME and COUNTY fields.
- [x] Fix harvest_date unit.
- [x] Figure site/loc acronyms: The location "code" is the 2-letter county abbreviation and "D" for dryland or "I" for irrigated for all crops. A "S" in wheat or corn is a soft test or a short season test and "C" and "O" are confectionary and oilseed respectively for sunflower. 
- [ ] Change all string cols to uppercase in the datasets.
- [ ] Store only a fixed set of columns. Setup this columns in config.
- [ ] Change datasets_setup.py to get the datasets from the documentation repo.
### Front-end
- [x] Create home, compare, about and data pages.
- [x] Create pages layout for home, compare, about and data.
- [ ] Change pages layout using dbc and finish front-end.
- [x] Data page functionality: Download filtered datasets by year.
- [ ] Change compare page to open a tab based on the search.

### Data Analysis
- [x] Implement exclusive visualizations for each dataset to account for data mismatching.
- [ ] Add units (see in the xlsx files).
- [x] Mean Brand Yield per Year:
  - [x] Better default dropdown selection;
- [x] Yield per brand:
  - [x] Add Year selector;
  - [x] Better default dropdown selection;
  - [ ] Set better hover options;
- [x] Mean Yield per year:
- [ ] Add climate data:
  - [ ] Yield - temperature (add water regime and use parallel coordinates?);