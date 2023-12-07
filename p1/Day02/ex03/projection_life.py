import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

def convert_population_string(population_str):
	"""
	Convert population strings with 'M' or 'k' suffix to numeric values.
	Replace errors with NaN.
	"""
	try:
		if 'M' in population_str:
			return float(population_str.replace('M', '')) * 1e6
		elif 'k' in population_str:
			return float(population_str.replace('k', '')) * 1e3
		else:
			return float(population_str)
	except (ValueError, TypeError):
		# If conversion fails, return NaN
		return np.nan

def plot_projection_life(year_data, life_data, gdp_data, population_data, year=1900):
	# Filter data for the year 1900
	year_1900_life = life_data[year_data == year]
	year_1900_gdp = gdp_data[year_data == year]
	# Filter data for the year 1900 and remove NaN values
	year_1900_population = population_data[year_data == year].apply(convert_population_string).dropna()

	# Create scatter plot
	plt.figure(figsize=(12, 8))
	sns.scatterplot(x=year_1900_gdp, y=year_1900_life, size=year_1900_population, sizes=(50, 500), label=f'Year {year}')

	# Set plot labels and title
	plt.xlabel('Gross National Product (GNP)')
	plt.ylabel('Life Expectancy (years)')
	plt.title(f'Projection of Life Expectancy in relation to GNP ({year} - All Countries)')

	# Add legend
	plt.legend()

	# Display the plot
	plt.show()