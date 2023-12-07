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
		life_data = load_csv_module.load("/home/alric/Code/42_datascience/p1/Day02/life_expectancy_years.csv")
		income_data = load_csv_module.load("/home/alric/Code/42_datascience/p1/Day02/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		
		# Assume the year data is present in the CSV file, adjust if necessary
		year_data = income_data.columns[1:].astype(int)
		print(year_data)
		print()
		print(life_data)
		print()
		print(income_data)
		print()
		# Call the function to plot the projection for the year 1900
		plot_projection_life(year_data, life_data, income_data.iloc[:, 1:], income_data.iloc[:, 1:])
	
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()
