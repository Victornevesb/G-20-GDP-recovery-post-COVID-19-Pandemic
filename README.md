# G-20-GDP-recovery-post-COVID-19-Pandemic
This is the Final Project for a Data Science Bootcamp at Concordia University. It is an EDA Project analyzing various GDP databases from G-20 countries and their recovery from the COVID-19 Pandemic recession

## Project Overview

This project analyzes the GDP resilience of G-20 countries in the aftermath of the COVID-19 pandemic. The analysis examines various economic indicators, including population, GDP per capita, Human Development Index (HDI), and a custom Resilience Index from 2014 to 2023. Visualizations and machine learning models are used to evaluate trends and make predictions.

## Key Features

- **Population Analysis:** Includes population data for G-20 countries in 2023, visualized using choropleth maps.
- **Human Development Index (HDI):** Examines HDI trends from 2014 to 2023, with detailed visualizations of the 2020 HDI distribution across G-20 countries.
- **GDP Analysis:** GDP data analysis includes GDP per capita trends and nominal GDP resilience across G-20 nations.
- **Resilience Index:** Custom index created to assess the resilience of G-20 countries based on economic indicators post-COVID-19.
- **Machine Learning:** Uses linear regression to predict economic resilience post-COVID-19 based on various features like GDP, population, and HDI.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install required dependencies**:
    Ensure you have Python 3.7+ and install the required Python libraries using:
    ```bash
    pip install -r requirements.txt
    ```

## Dependencies

The project utilizes a variety of Python libraries for data manipulation, visualization, and machine learning:

- `pandas`: Data manipulation and analysis.
- `matplotlib`: Plotting basic graphs.
- `numpy`: Numerical computations.
- `geopandas`: Geospatial data handling.
- `plotly`: Interactive visualizations, including choropleth maps.
- `seaborn`: Advanced data visualization.
- `dash`: Web-based dashboard creation for interactive visualizations.
- `scikit-learn`: Machine learning models for regression and performance metrics.

Ensure all these libraries are installed by running the command above.

## Data Sources

The following datasets are used for analysis in this project:

- **Population Data**: `Population - G20/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv`
- **Human Development Index (HDI) Data**: `Annual HDI - G20/Human Development Index.csv`
- **GDP Data**: Time-series GDP data from 2014 to 2023.

## Usage

1. **Data Preparation:**
    The project uses CSV files for population, GDP, and HDI data for G-20 countries. Ensure that the datasets are placed in the correct directories. Example files include:
    - `Population - G20/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv`
    - `Annual HDI - G20/Human Development Index.csv`

2. **Running the Notebook:**
    Open and execute the Jupyter notebook `Final Project.ipynb` to reproduce the analysis and visualizations.

3. **World Maps Visualizations:**
    - **Population in 2023:** A choropleth map showing the population distribution across G-20 countries for the year 2023.
    - **Human Development Index (HDI):** A world map showing HDI values across G-20 countries, focusing on the year 2020.

4. **Resilience Index:**
    A custom Resilience Index is calculated to measure the economic recovery of G-20 nations after the pandemic. The index takes into account GDP growth rates, population, and HDI data. This index is visualized through various graphs to show which countries have rebounded more effectively post-pandemic.

5. **Visualizations:**
    - Choropleth maps for population and HDI.
    - GDP per Capita across G-20 countries.
    - Resilience Index charts showing the recovery trajectory.

6. **Linear Regression Model:**
    The notebook implements linear regression to predict post-COVID-19 GDP resilience using features like GDP, population, and HDI. Model performance is evaluated using metrics like Mean Squared Error (MSE) and R-squared.

## Example Output

Sample visualizations and insights are provided directly within the notebook, including:
- G-20 Countries Population in 2023.
- Human Development Index (HDI) for 2020.
- GDP per Capita trends across G-20 countries.


