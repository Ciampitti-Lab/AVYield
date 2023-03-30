tp1 <- tabPanel(
    title = "Tab 1",
    includeCSS("www/styles.css"),
    div(
        h2("Test 1")
    ),
    fluidRow(
        box(plotOutput("plot1", height = 250)),
        box(
            title = "Controls",
            sliderInput("slider", "Number of observations:", 1, 100, 50)
        )
    ),
    value = "tab1"
)
tp2 <- tabPanel(
    title = "Tab 2",
    div(
        h2("Test 2")
    ),
    value = "tab2"
)



navbarPage(
    title = "Maize and Soybean dashboard",
    tp1,
    tp2,
)
