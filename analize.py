import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
df = pd.read_csv('life-expectancy.csv')

# Filtering: Filter the data for a specific country
country_data = df.loc[df['Entity'] == 'Country']

# Sorting: Sort the data by year in ascending order
sorted_df = df.sort_values('Year')

# Aggregation: Calculate the average life expectancy for each entity
avg_life_expectancy = df.groupby('Entity')['Life expectancy (years)'].mean()

# Basic statistics
mean_life_expectancy = df['Life expectancy (years)'].mean()
median_life_expectancy = df['Life expectancy (years)'].median()
mode_life_expectancy = df['Life expectancy (years)'].mode()

# Find the country with the highest and lowest life expectancy
country_with_highest_life_expectancy = df.loc[df['Life expectancy (years)'].idxmax()]['Entity']
country_with_lowest_life_expectancy = df.loc[df['Life expectancy (years)'].idxmin()]['Entity']

# Get the number of unique entities (countries) in the data
num_countries = df['Entity'].nunique()

# Calculate the range of life expectancy values
life_expectancy_range = df['Life expectancy (years)'].max() - df['Life expectancy (years)'].min()

# Get the top 10 countries with the highest life expectancy
top_10_countries = df.groupby('Entity')['Life expectancy (years)'].mean().nlargest(10)

# Print the filtered data for the specific country
print("Filtered Data for the specific country:")
print(country_data)

# Print the sorted data by year
print("\nSorted Data by Year:")
print(sorted_df)

# Print the average life expectancy for each entity
print("\nAverage Life Expectancy by Entity:")
print(avg_life_expectancy)

# Print the mean, median, and mode of life expectancy
print("Mean life expectancy:", mean_life_expectancy)
print("Median life expectancy:", median_life_expectancy)
print("Mode(s) of life expectancy:")
print(mode_life_expectancy)

# Print the country with the highest and lowest life expectancy
print("Country with the highest life expectancy:", country_with_highest_life_expectancy)
print("Country with the lowest life expectancy:", country_with_lowest_life_expectancy)

# Print the number of unique countries
print("Number of Countries:", num_countries)

# Print the range of life expectancy values
print("Range of Life Expectancy:", life_expectancy_range)

# Print the top 10 countries with the highest life expectancy
print("Top 10 Countries with Highest Life Expectancy:")
print(top_10_countries)

# Line plot
plt.plot(df['Year'], df['Life expectancy (years)'])
plt.xlabel('Year')
plt.ylabel('Life expectancy (years)')
plt.title('Life Expectancy Over the Years')
plt.show()

# Bar chart for top 10 countries with the highest life expectancy
plt.bar(top_10_countries.index, top_10_countries.values)
plt.xlabel('Country')
plt.ylabel('Life Expectancy (years)')
plt.title('Top 10 Countries with Highest Life Expectancy')
plt.xticks(rotation=90)
plt.show()

# Pie chart for the distribution of life expectancy across entities
plt.pie(avg_life_expectancy, labels=avg_life_expectancy.index, autopct='%1.1f%%')
plt.title('Distribution of Life Expectancy by Entity')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# Box plot for the distribution of life expectancy across years
plt.boxplot(df['Life expectancy (years)'], vert=False)
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Year')
plt.title('Distribution of Life Expectancy Across Years')
plt.show()

# Scatter plot for life expectancy vs. GDP per capita
plt.scatter(df['GDP per capita'], df['Life expectancy (years)'])
plt.xlabel('GDP per capita')
plt.ylabel('Life expectancy (years)')
plt.title('Life Expectancy vs. GDP per Capita')
plt.show()


