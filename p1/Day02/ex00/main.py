from load_csv import load


def main():
	try:
		print(load("p1/Day02/life_expectancy_years.csv"))
	except Exception as e:
		print(e)
	return 0

if __name__ == "__main__":
	main()