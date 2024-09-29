
# G-20-GDP-Recovery-Post-COVID-19-Pandemic

This is the Final Project for a Data Science Bootcamp at Concordia University. It is an EDA (Exploratory Data Analysis) project analyzing various GDP databases from G-20 countries and their recovery from the COVID-19 Pandemic recession.

## Project Overview
This project analyzes the GDP resilience of G-20 countries in the aftermath of the COVID-19 pandemic. The analysis focuses on GDP data, including GDP Growth, GDP per capita, and nominal GDP trends from 2014 to 2023. Visualizations, including choropleth maps, are used to evaluate these trends and understand the economic recovery across nations.

## Key Features
- **GDP Analysis**: Detailed exploration of GDP Growth, GDP per capita, and nominal GDP resilience across G-20 nations.
- **Choropleth Maps**: Visualization of various GDP indicators using choropleth maps to illustrate how countries have fared post-pandemic.
- **Data Source**: GDP data is sourced from the World Bank, ensuring up-to-date and reliable information.
- **Machine Learning**: A linear regression model is used to predict GDP recovery trends based on various economic indicators.

## Installation
Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

Install required dependencies. Ensure you have Python 3.7+ and install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

## Dependencies
The project utilizes the following Python libraries for data manipulation, visualization, and machine learning:

- `pandas`: Data manipulation and analysis.
- `matplotlib`: Plotting basic graphs.
- `numpy`: Numerical computations.
- `geopandas`: Geospatial data handling.
- `plotly`: Interactive visualizations, including choropleth maps.
- `seaborn`: Advanced data visualization.
- `dash`: Web-based dashboard creation for interactive visualizations.
- `scikit-learn`: Machine learning models for regression and performance metrics.

## Data Sources
The GDP data for this project is sourced from the **World Bank** via the following dataset:

- **GDP Data**: Time-series GDP data for G-20 countries from 2014 to 2023, accessible from the World Bank at [https://data.worldbank.org/](https://data.worldbank.org/).

## Usage
### Data Preparation
The project uses CSV files for GDP data for G-20 countries. Ensure that the datasets are placed in the correct directories. Example file:

- **GDP Data**: G-20/WorldBank_GDP_Data.csv

### Running the Notebook
Open and execute the Jupyter notebook `Final Project.ipynb` to reproduce the analysis and visualizations.

## Visualizations
- **Choropleth Maps**: World maps visualizing GDP growth, GDP per capita, and nominal GDP across G-20 countries.
- **GDP per Capita**: Visualizations showing GDP per capita trends across G-20 countries from 2014 to 2023.
- **Nominal GDP**: Charts illustrating the overall nominal GDP resilience across G-20 nations post-pandemic.

## Machine Learning Model
A linear regression model is implemented in the notebook to predict post-COVID-19 GDP resilience using features like GDP growth, GDP per capita, and population. Model performance is evaluated using metrics such as Mean Squared Error (MSE) and R-squared.

## Example Output
Sample visualizations and insights include:

- G-20 Countries' GDP Growth.
- GDP per Capita trends from 2014 to 2023.
- Nominal GDP recovery post-COVID-19.
