import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

def aff_pop(data, country1, country2):
	"""Plot the population of two countries over time."""
	# Get the population of the two countries
	pop1 = data[data["country"] == country1]
	pop2 = data[data["country"] == country2]

	# Convert population values to numeric (remove 'M' and 'k')
	pop1_values = pd.to_numeric(pop1.iloc[:, 1:].replace({'M': 'e6', 'k': 'e3'}, regex=True).values.flatten(), errors='coerce')
	pop2_values = pd.to_numeric(pop2.iloc[:, 1:].replace({'M': 'e6', 'k': 'e3'}, regex=True).values.flatten(), errors='coerce')

	# Plot the population of the two countries over time
	years = pop1.columns[1:].astype(int)
	plt.plot(years, pop1_values, label=country1, color='green')
	plt.plot(years, pop2_values, label=country2, color='blue')

	# Set x-axis ticks to show every 40th year
	plt.xticks(years[::40])

	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.title("Population Projection")
	plt.legend(loc='lower right')
	# Format y-axis labels in millions
	formatter = FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M')
	plt.gca().yaxis.set_major_formatter(formatter)
	plt.show()