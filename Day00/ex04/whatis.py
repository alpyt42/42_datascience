import sys

def check_odd_even(argument):
	try:
		num = int(argument)
		if num % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except ValueError:
		raise AssertionError("AssertionError: argument is not an integer")

if len(sys.argv) > 2:
	print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
	try:
		check_odd_even(sys.argv[1])
	except AssertionError as e:
		print(e)
