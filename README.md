# Dashboard Project

## References

* [Bootswatch theme](https://bootswatch.com/lumen/)
* [Reference Project](https://github.com/fiakoenjiniring/rainfall/tree/main)
* [Reference site - 1](http://ramwheatdb.com/headtohead.php)
* [Reference site - 2](https://www.myfields.info/crop-data)

## Initial notes
Lots of work to do =/

## To-do

- [x] Add datasets from ignacio email.
- [x] Fix new datasets.
- [x] Pre-process the datasets.
- [ ] Store only a fixed set of columns?
- [ ] Add year selection and filter datasets initially.
    * Be careful with performance here. If the app needs to pre-process the datasets every time the page updates we could have some performance issues.
- [x] Create home, about and data pages.
- [ ] Create pages layout for home, about and data.
- [ ] Change pre_processing.py to get the datasets from the documentation repo.
- [ ] CHECK UNITS IN THE xlsx FILES!
- [x] Fix harvest_date unit.
- [x] Figure site/loc acronyms: The location "code" is the 2-letter county abbreviation and "D" for dryland or "I" for irrigated for all crops. A "S" in wheat or corn is a soft test or a short season test and "C" and "O" are confectionary and oilseed respectively for sunflower. 

* Visualizations:
- [ ] Explore the datasets relation using as input: year, county, water regime and return: genotype and brand.
- [ ] Water regime and productivity.
- [ ] Add climate data.


## Project structure
├── app.py
├── assets
│   ├── KSU-Crops-logo.png
│   └── styles.css
├── callbacks
│   ├── hf_callbacks.py
│   ├── main_callbacks.py
│   └── __pycache__
│       ├── hf_callback.cpython-39.pyc
│       ├── hf_callbacks.cpython-39.pyc
│       ├── hf_func.cpython-39.pyc
│       └── main_callbacks.cpython-39.pyc
├── components
│   ├── about.py
│   ├── data.py
│   ├── hf.py
│   ├── home.py
│   └── __pycache__
│       ├── about.cpython-39.pyc
│       ├── About.cpython-39.pyc
│       ├── data.cpython-39.pyc
│       ├── hf.cpython-39.pyc
│       └── home.cpython-39.pyc
├── config.py
├── config.yml
├── data
│   ├── data_exp.ipynb
│   ├── datasets
│   │   ├── 1982-2020_corn.csv
│   │   ├── 1982-2022_wheat.csv
│   │   ├── 1991-2022_soybean.csv
│   │   ├── 1998-2019_sunflower.csv
│   │   ├── Data_Comparison_MS_1991_2021_Maize.csv
│   │   ├── Data_Comparison_MS_1991_2021_Maize_Sites.csv
│   │   ├── Data_Comparison_MS_1991_2021_Soybean.csv
│   │   ├── Data_Comparison_MS_1991_2021_Soybean_Sites.csv
│   │   └── sunflower_locations_dict.csv
│   ├── outputs
│   ├── pre_processing.py
│   ├── __pycache__
│   │   ├── pre_processing.cpython-39.pyc
│   │   └── visualization.cpython-39.pyc
│   └── visualization.py
├── __pycache__
│   ├── app.cpython-39.pyc
│   └── config.cpython-39.pyc
└── README.md
