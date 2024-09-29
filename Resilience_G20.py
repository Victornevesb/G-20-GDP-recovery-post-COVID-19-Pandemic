import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go

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
        color_continuous_scale=px.colors.sequential.Rainbow,
        title='G20 Countries Population in 2023'
    )

    # Adjust the layout of the figure
    fig.update_layout(
        width=1000,  # Set the width of the plot
        height=600   # Set the height of the plot
    )

    # Display the map
    st.plotly_chart(fig)

    
    
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

    # Choropleth map for the most recent GDP growth (2023)
    latest_growth_data = growth_data_g20[['Country Name', '2023']].copy()
    latest_growth_data.columns = ['Country Name', 'GDP Growth 2023']  # Rename for clarity

    # Plot the choropleth map using Plotly Express
    fig_growth_map = px.choropleth(
        latest_growth_data,
        locations='Country Name',
        locationmode='country names',
        color='GDP Growth 2023',
        hover_name='Country Name',
        color_continuous_scale=px.colors.sequential.Blues,
        title='GDP Growth for G20 Countries in 2023'
    )

    # Adjust the layout of the figure
    fig_growth_map.update_layout(
        width=1000,  # Set the width of the plot
        height=600,  # Set the height of the plot
    )
    # Display the choropleth map in Streamlit
    st.plotly_chart(fig_growth_map)

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

    confirmed_melted = covid_confirmed_data.reset_index().melt(id_vars='Country/Region', var_name='Date', value_name='Cases')
    deaths_melted = covid_deaths_data.reset_index().melt(id_vars='Country/Region', var_name='Date', value_name='Deaths')

    # Plot for Confirmed Cases
    fig_cases = px.line(
        confirmed_melted,
        x='Date',
        y='Cases',
        color='Country/Region',
        title='COVID-19 Confirmed Cases in G20 Countries',
        labels={
            'Cases': 'Number of Cases',
            'Date': 'Date',
            'Country/Region': 'Country'
        }
    )

    # Update layout for the cases plot
    fig_cases.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Cases',
        width=1000,
        height=600,
        legend_title="Country/Region",
        legend=dict(x=1, y=1)
    )

    # Display the cases plot
    st.plotly_chart(fig_cases)

    # Plot for Deaths
    fig_deaths = px.line(
        deaths_melted,
        x='Date',
        y='Deaths',
        color='Country/Region',
        title='COVID-19 Deaths in G20 Countries',
        labels={
            'Deaths': 'Number of Deaths',
            'Date': 'Date',
            'Country/Region': 'Country'
        }
    )

    # Update layout for the deaths plot
    fig_deaths.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Deaths',
        width=1000,
        height=600,
        legend_title="Country/Region",
        legend=dict(x=1, y=1)
    )

    # Display the deaths plot
    st.plotly_chart(fig_deaths)

        
# Section: Resilience Index
elif section == 'Resilience Index':
    st.header("Resilience Index for G20 Countries")

    # Display Resilience Data
    st.dataframe(resilience_data)

    # Define the data
    data1 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [10, 20, 20, 20, 80, 50, 30, 40, 20, 40, 30, 50, 20, 20, 20, 10, 10, 90, 10]
    }

    data2 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [80, 50, 40, 50, 60, 40, 30, 40, 50, 60, 40, 10, 20, 80, 60, 60, 90, 60, 10]
    }

    data3 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [20, 50, 90, 20, 20, 10, 20, 20, 30, 80, 80, 10, 20, 0, 60, 10, 100, 30, 90]
    }

    data4 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [20, 30, 20, 30, 100, 40, 30, 40, 30, 100, 40, 40, 40, 40, 30, 20, 20, 30, 20]
    }

    data5 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [40, 60, 40, 40, 100, 40, 40, 40, 60, 80, 40, 60, 60, 40, 40, 80, 40, 40, 40]
    }

    data6 = {
        'Country Name': ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'France', 'United Kingdom', 
                         'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 
                         'Turkey', 'United States', 'South Africa'],
        'Grade': [20, 60, 40, 40, 100, 40, 40, 90, 40, 80, 40, 60, 60, 40, 40, 80, 40, 40, 40]
    }

    # Convert data to DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4)
    df5 = pd.DataFrame(data5)
    df6 = pd.DataFrame(data6)

    # Merging the dataframes on 'Country Name'
    merged_df = df1.merge(df2, on='Country Name', suffixes=('_1', '_2')).merge(df3, on='Country Name') \
        .merge(df4, on='Country Name', suffixes=('_3', '_4')).merge(df5, on='Country Name', suffixes=('_5', '_6')) \
        .merge(df6, on='Country Name', suffixes=('_7', '_8'))

    # Renaming the columns correctly
    grade_columns_map = {
    'Grade_1': "Nominal GDP",
    'Grade_2': "GDP per capita",
    'Grade_3': "GDP Growth",
    'Grade_4': "GDP Expenses",
    'Grade_5': "COVID Cases",
    'Grade_6': "COVID Deaths"
    }

    # Rename the columns in the dataframe
    merged_df.rename(columns=grade_columns_map, inplace=True)

# Add Total Grade using the new column names
    merged_df['Total Grade'] = merged_df[list(grade_columns_map.values())].sum(axis=1)

# Streamlit App Layout
    st.title("Country Grade Dashboard")

# Sidebar for Navigation
    st.sidebar.title("Select Country and Grade")

# Dropdown for selecting country
    selected_country = st.sidebar.selectbox("Select Country", merged_df['Country Name'].unique())

# Slider for selecting grade datasets
    selected_grade = st.sidebar.slider("Select Number of Grades", 1, 6, 6)

# Get the subset of the column names based on the number of grades selected
    selected_grade_columns = list(grade_columns_map.values())[:selected_grade]

# Display Grade trends
    st.subheader(f"Grades Trend for {selected_country}")
    country_data = merged_df[merged_df['Country Name'] == selected_country]
    grades = country_data[selected_grade_columns].values.flatten()

    trace = go.Scatter(
        x=selected_grade_columns,
        y=grades,
        mode='lines+markers',
        name=selected_country
    )

    fig_grade_trend = {
        'data': [trace],
        'layout': go.Layout(
            title=f'Grades Trend for {selected_country}',
            xaxis={'title': 'Grade Dataset'},
            yaxis={'title': 'Grade'},
            hovermode='closest'
        )
    }

    st.plotly_chart(fig_grade_trend)

# Display Total Grade comparison
    st.subheader("Total Resilience Comparison Across Countries")
    total_grades = merged_df[['Country Name'] + selected_grade_columns]
    total_grades['Total'] = total_grades[selected_grade_columns].sum(axis=1)
    total_grades = total_grades.sort_values(by='Total', ascending=False)

    trace_total = go.Bar(
        x=total_grades['Country Name'],
        y=total_grades['Total'],
        name='Total Grade Comparison'
    )

    fig_total_grade = {
        'data': [trace_total],
        'layout': go.Layout(
            title='Total Resilience Comparison Across Countries',
            xaxis={'title': 'Country'},
            yaxis={'title': 'Total Grade'},
            hovermode='closest'
        )
    }

    st.plotly_chart(fig_total_grade)
    
    
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
