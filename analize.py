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

# Line plot
plt.plot(df['Year'], df['Life expectancy (years)'])
plt.xlabel('Year')
plt.ylabel('Life expectancy (years)')
plt.title('Life Expectancy Over the Years')
plt.show()
