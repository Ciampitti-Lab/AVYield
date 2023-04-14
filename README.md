# Dashboard Project

## Initial notes

* global.R references: [[1]](https://mraess.rbind.io/2018/07/the-awesomeness-that-is-the-global-r-file-or-how-to-clean-up-your-shiny-app/) [[2]](https://shiny.rstudio.com/articles/scoping.html)
* examples: [[1]](https://github.com/rstudio/shiny-examples/tree/main/086-bus-dashboard) [[2]](https://github.com/rstudio/shiny-examples/tree/main/087-crandash) [[3]](https://github.com/Public-Health-Scotland/scotpho-profiles-tool) [[4]](https://github.com/rstudio/shiny-examples/tree/main/063-superzip-example) [[multiple]](https://www.r-bloggers.com/2022/03/r-shiny-in-life-sciences-top-7-dashboard-examples/)
* docs: [[1]](https://rstudio.github.io/shinydashboard/get_started.html)

## To-do

* [ ] Change data_loader to get the datasets from the documentation repo.
* [x] check if maize or soybean datasets is selected and add an option to show less data in the table section. (Changed table render to fix this)
* [x] Sort sites datasets by planting_date and year.
* [ ] Explore the datasets relation using as input: year, county, water regime and return: genotype and brand.
* [ ] Water regime and produtivity.
* [x] Fix harvest_date unit.
* [x] Figure site acronyms.
