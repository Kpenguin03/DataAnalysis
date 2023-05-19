import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
df = pd.read_csv('life-expectancy.csv')

# Basic statistics
print("Mean life expectancy:", df['Life expectancy (years)'].mean())
print("Median life expectancy:", df['Life expectancy (years)'].median())
print("Mode of life expectancy:")
print(df['Life expectancy (years)'].mode())

# Line plot
plt.plot(df['Year'], df['Life expectancy (years)'])
plt.xlabel('Year')
plt.ylabel('Life expectancy (years)')
plt.title('Life Expectancy Over the Years')
plt.show()
