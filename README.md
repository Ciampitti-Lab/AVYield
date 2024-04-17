# Dashboard Project

## References

- [Bootswatch theme](https://bootswatch.com/lumen/)
- [Reference Project](https://github.com/fiakoenjiniring/rainfall/tree/main)
- [Reference site - 1](http://ramwheatdb.com/headtohead.php)
- [Reference site - 2](https://www.myfields.info/crop-data)
- [Reference app](https://analytics.iasoybeans.com/cool-apps/ISOFAST/)
- [Geo Data](https://public.opendatasoft.com/explore/dataset/us-county-boundaries)

## Bugs

- [x] Custom Data is probably broken. FIXED
- [x] The lazy state dropdown implemenation causes a bug when: FIXED
  - Select a crop in kansas.
  - Change to crop to canola.
  - doesn't seem to break anything though.

## First meeting with jane

### Front-end

- [x] add Center for sorghum improvement logo.
- [x] hide some useless columns and make a user friendly standard.
- [x] Add Lucas as a contributor.
- [x] Fix Carlos pictures.
- [ ] Better modal design (custom data)
- [x] Change the picture getter.
- [ ] Add visual clue to indicate that the first dropdown is "fixed" while the second isn't; on analysis page.
- [x] Home page refactor.

### Features

- [x] add an avg line from the county
  - [x] make it use the max yield to determine line and dot size.
- [ ] docs on data page.
- [ ] annual trend.

### Database

- [x] Remove duplicates/make the entries on NAME and BRAND standard.
- [x] round everything to no decimal places
- [x] st county: stanton to stafford.
- [x] Fix FN - Finney, PH Phillips, Greeley GR

* Add canola data:
  - [x] Add State filter.
  - [x] Pre process all the data.
  - [x] Add data.
  - [x] THE YIELD IS IS lb/acre - convert it to bu/acre and add option to change. THE CURRENT CONVERSION AND UNIT IS WRONG!
  - [x] for some reason some entries filtering by year messes up the y axis a little, check on that later.

#### Corn

- [x] check for zero values.
  - Couldn't find any.
- [x] LSD 2023.

#### Sorghum

- [x] in remove entries with TANT in LOC
- [x] Fix PCODES in early years.

#### Soybean

#### Sunflower

- Data from 2020-2023 is missing this information
- Should we really display this information?
  - [x] confectionary/oil seed - in LOC last letter.

#### Wheat

- [x] Add 1982-1993.

* Should we really display this information?

- [x] Remove entries with NC, EC, NWD, SWD, IRR, SC NE, SE in LOC.\
- [x] Remove entries with MEAN on NAME.

## To-do

### Data Engineering

- [x] Add new datasets.
- [x] Collect Kansas geo data.
- [x] Pre-process the datasets.
- [x] Pre-pre-process the datasets outside the main app to maintain high performance.
- [x] Process corn and wheat dataset to deleted metrics in genotype NAME.
- [x] Drop duplicate rows in the datasets.
- [x] Make this combination unique [YEAR, NAME, COUNTY, WATER_REGIME].
- [x] Fix new datasets.
- [x] Fix, LOC, WATER_REGIME and COUNTY fields.
- [x] Fix harvest_date unit.
- [x] Figure site/loc acronyms: The location "code" is the 2-letter county abbreviation and "D" for dryland or "I" for irrigated for all crops. A "S" in wheat or corn is a soft test or a short season test and "C" and "O" are confectionary and oilseed respectively for sunflower.

### Front-end

- [x] Create home, compare, about and data pages.
- [x] Create pages layout for home, compare, about and data.
- [x] Change pages layout using dbc
- [x] Data page functionality: Download filtered datasets by year.
- [x] Leave home page to introduce the app.
- [x] Leave about page to display infos and paper.
- [x] Make compare into main view page.
- [x] Change header to a sidebar?.

* Front-end.
  - [x] Header and Sidebar.
  - [x] Compare Page.
  - [x] Home Page.
  - [x] Data Page.
  - [x] About Page.

### Data Analysis

- [x] fix hovers, round hovers and add units in titles and hovers.
- [x] Add units (see in the xlsx files) (add to graph title).
- [x] Add option to change units.
- [x] Fix unit selector not clearing options store and list.
- [x] US customary units: bu/ac and lb/ac --- Metric: Mg/ha, kg/ha --- [Conversion Rates](https://www.extension.iastate.edu/agdm/wholefarm/html/c6-80.html).
- [x] add a max amount that the user can input.
- [x] change clear genotypes btn, input year dropdown, crops dropdown to clear the graphs
- [x] fix bar and box vis, the analysis and display of information is not matching and something is going on there.

* Add county filter in compare?
  - [x] I was thinking in making a separate view for the counties, leave 1 for the avg of all of them, another representing them in a box plot so the user can check by themselves, and lastly one to show each county individually.

- [x] add a filter for genotype with diff years.
  - Should the user input the years or just throw all of them?

## fix errors

- [x] Genotypes string in selected list
- [x] Change map to avg instead of sum. Change title
- [x] Remove counties without data in the map
- [x] Convert units and keep selected list. don't clear it
- [x] data already added bug.
- [x] check data filtering process if is still right with newer version of pandas.
- [x] remove 2 units
- [x] better front
  - [x] remove hardcode on last update compare page.
  - [x] fix compare dropdown width
- [x] cleanup
- [x] launch a little prototype
