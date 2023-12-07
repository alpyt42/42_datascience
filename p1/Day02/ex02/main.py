import importlib
from aff_pop import aff_pop

# Add the project directory to the Python path
import sys
sys.path.append("/home/alric/Code/42_datascience/p1")

# Import the module with the modified load function
load_csv_module = importlib.import_module("Day02.ex00.load_csv")

def main():
	try:
		# Access the modified load function from the imported module
		data = load_csv_module.load("/home/alric/Code/42_datascience/p1/Day02/population_total.csv")
		print(data)
		aff_pop(data, "France", "Belgium")
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()
