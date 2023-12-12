import importlib
from projection_life import plot_projection_life

# Add the project directory to the Python path
import sys
sys.path.append("/home/alric/Code/42_datascience/p1")

# Import the module with the modified load function
load_csv_module = importlib.import_module("Day02.ex00.load_csv")

def main():
	try:
		# Load data
		life_expectancy_data = load_csv_module.load("/home/alric/Code/42_datascience/p1/Day02/life_expectancy_years.csv")
		income_data = load_csv_module.load("/home/alric/Code/42_datascience/p1/Day02/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		
		# Filter the data for the year 1900
		income_1900 = income_data[['country', '1900']]
		life_expectancy_1900 = life_expectancy_data[['country', '1900']]
		# Call the function to plot the projection for the year 1900
		plot_projection_life(income_1900, life_expectancy_1900)
	
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()
