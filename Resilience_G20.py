import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load all the pickle files for each dataset
with open('g20_population_data.pkl', 'rb') as f:
    g20_population_data = pickle.load(f)

with open('growth_data_g20.pkl', 'rb') as f:
    growth_data = pickle.load(f)
    growth_data_g20 = growth_data['growth_data_g20']
    growth_data_filtered = growth_data['growth_data_filtered']

with open('covid_data_g20.pkl', 'rb') as f:
    covid_confirmed_data = pickle.load(f)

with open('covid_deaths_g20.pkl', 'rb') as f:
    covid_deaths_data = pickle.load(f)

with open('resilience_data_g20.pkl', 'rb') as f:
    resilience_data = pickle.load(f)

with open('g20_gdp_data.pkl', 'rb') as f:
    gdp_data = pickle.load(f)

# Streamlit App Layout
st.title("G20 Countries Dashboard")

# Sidebar for Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Select Section", ['Population Data', 'GDP Growth Data', 'GDP Data', 'COVID-19 Data', 'Resilience Index'])

# Section: Population Data
if section == 'Population Data':
    st.header("G20 Population Data (2023)")
    st.write("This section displays the population data for G20 countries.")
    st.dataframe(g20_population_data)

    # Population data for 2023
    population_data_2023 = {
        'Country Name': [
            'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France',
            'United Kingdom', 'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 
            'Mexico', 'Russia', 'Saudi Arabia', 'Turkey', 'United States', 'South Africa'
        ],
        '2023 Population': [
            46654581, 26638544, 216422446, 40097761, 1410710000, 84482267, 68170228,
            68350000, 277534122, 1428627663, 58761146, 124516650, 51712619, 
            128455567, 143826130, 36947025, 85326000, 334914895, 60414495
        ]
    }

    # Convert the dictionary into a DataFrame
    population_df_2023 = pd.DataFrame(population_data_2023)

    # Plot the choropleth map using Plotly Express
    fig = px.choropleth(
        population_df_2023,
        locations='Country Name',
        locationmode='country names',
        color='2023 Population',
        hover_name='Country Name',
        color_continuous_scale=px.colors.sequential.Plasma,
        title='G20 Countries Population in 2023'
    )

    # Adjust the layout of the figure
    fig.update_layout(
        width=1000,  # Set the width of the plot
        height=600   # Set the height of the plot
    )

    # Display the map
    fig.show()

    
# Section: GDP Growth Data
elif section == 'GDP Growth Data':
    st.header("G20 GDP Growth Data (2014-2023)")
    st.write("This section shows the GDP growth data for G20 countries.")
    st.dataframe(growth_data_g20)

    # GDP Growth Line Chart
    years = list(range(2014, 2024))
    x_ticks_positions = list(range(len(years)))  # Positions for 10 years (0 to 9)
    x_ticks_labels = [str(year) for year in years]  # Labels from 2014 to 2023

    plt.figure(figsize=(12, 6))
    for country in growth_data_g20['Country Name']:
        plt.plot(
            x_ticks_positions,
            growth_data_g20[growth_data_g20['Country Name'] == country][[str(year) for year in years]].values.flatten(),
            label=country
        )

    plt.xticks(x_ticks_positions, x_ticks_labels)
    plt.axvline(x=6, color='red', linestyle='--', label='Beginning of Pandemic (2020)')
    plt.text(6, plt.ylim()[1] * 0.9, 'Beginning of Pandemic', color='red', ha='center')
    plt.title('GDP Growth for G20 Countries (2014-2023)')
    plt.xlabel('Year')
    plt.ylabel('GDP Growth (% per year)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    st.pyplot(plt)

# Section: GDP Data

elif section == 'GDP Data':
    st.header("G20 GDP Data (in USD Trillions)")
    st.write("This section displays the GDP data for G20 countries in USD trillions.")

    g20_countries = [
        'Argentina', 'Australia', 'Brazil', 'Canada', 'France', 'China', 'Germany', 
        'India', 'Indonesia', 'Italy', 'Japan', 'Mexico', 'Russia', 'Saudi Arabia', 
        'South Africa', 'South Korea', 'Turkey', 'United Kingdom', 'United States'
    ]

    # Create a DataFrame for G20 countries to ensure all are present
    g20_df = pd.DataFrame({'Country Name': g20_countries})

    # Merge the GDP data with the G20 countries list, using a left join to include all countries
    gdp_data_full = g20_df.merge(gdp_data, on='Country Name', how='left')

    # Fill missing GDP data with 0 or NaN as appropriate
    gdp_years = [col for col in gdp_data.columns if '(GDP in USD Trillions)' in col]
    gdp_data_full[gdp_years[-1]] = gdp_data_full[gdp_years[-1]].fillna(0)

    # Display the GDP data in a dataframe
    st.dataframe(gdp_data_full)
    
    # Plot the choropleth map using Plotly Express
    gdp_years = [col for col in gdp_data_full.columns if '(GDP in USD Trillions)' in col]
    fig = px.choropleth(
        gdp_data_full,
        locations='Country Name',
        locationmode='country names',
        color=gdp_years[-1],  # Use the most recent year for coloring
        hover_name='Country Name',
        color_continuous_scale=px.colors.sequential.Rainbow,
        title=f'G20 Countries GDP in {gdp_years[-1]}'
    )

    # Adjust the layout of the figure
    fig.update_layout(
        width=1000,  # Set the width of the plot
        height=600   # Set the height of the plot
    )
  # Display the map in Streamlit
    st.plotly_chart(fig)

# Section: COVID-19 Data
elif section == 'COVID-19 Data':
    st.header("COVID-19 Cases & Deaths Data for G20 Countries")

    # Confirmed Cases Data
    st.subheader("Confirmed COVID-19 Cases")
    st.dataframe(covid_confirmed_data)

    # Deaths Data
    st.subheader("COVID-19 Deaths Data")
    st.dataframe(covid_deaths_data)

    # Check for the available columns
    st.write("Confirmed Data Columns: ", covid_confirmed_data.columns)
    st.write("Deaths Data Columns: ", covid_deaths_data.columns)


  

# Section: Resilience Index
elif section == 'Resilience Index':
    st.header("Resilience Index for G20 Countries")

    # Display Resilience Data
    st.dataframe(resilience_data)

    # Heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(resilience_data.set_index('Country Name').T, annot=False, cmap='coolwarm', cbar_kws={'label': 'Grade'})
    plt.title('Resilience Grades for G20 Countries')
    plt.xlabel('Country')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

    # Choropleth Map for Resilience
    fig = px.choropleth(
        resilience_data,
        locations="Country Name",
        locationmode="country names",
        color="Total Grade",
        hover_name="Country Name",
        color_continuous_scale=px.colors.sequential.Magma,
        title="Resilience Index by Country"
    )
    st.plotly_chart(fig)
