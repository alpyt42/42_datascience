import matplotlib.pyplot as plt

def aff_life(data, country):
	# Print the list of column names
	print("Column Names:", data.columns)

	# Select France in Data
	france = data[data["country"] == country]
	print(france)

	# Plot Life expectancy over the years, only every 40th year
	plt.plot(france.columns[1:], france.iloc[0, 1:])

	# Set x-axis ticks to show every 40th year
	plt.xticks(france.columns[1::40])

	plt.xlabel("Year")
	plt.ylabel("Life Expectancy")
	plt.title("Life Expectancy Over the Years in France")
	plt.show()