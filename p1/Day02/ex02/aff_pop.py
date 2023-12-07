import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np

def aff_pop(data, country1, country2):
	"""Plot the population of two countries over time."""
	# Get the population of the two countries
	pop1 = data[data["country"] == country1]
	pop2 = data[data["country"] == country2]

	# Convert population values to numeric (remove 'M' and 'k')
	pop1_values = pd.to_numeric(pop1.iloc[:, 1:].replace({'M': 'e6', 'k': 'e3'}, regex=True).values.flatten(), errors='coerce')
	pop2_values = pd.to_numeric(pop2.iloc[:, 1:].replace({'M': 'e6', 'k': 'e3'}, regex=True).values.flatten(), errors='coerce')

	# Get years in the specified time range
	years = pop1.columns[1:].astype(int)
	mask = (years >= 1800) & (years <= 2050)

	# Plot the population of the two countries over the specified time range
	plt.plot(years[mask], pop1_values[mask], label=country1, color='green')
	plt.plot(years[mask], pop2_values[mask], label=country2, color='blue')

	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.title("Population Projection")
	plt.legend(loc='lower right')
	# Format y-axis labels in millions
	formatter = FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M')
	plt.gca().yaxis.set_major_formatter(formatter)
	plt.show()