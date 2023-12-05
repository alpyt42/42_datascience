import sys


NESTED_MORSE = {
	" ": "/",
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	"0": "-----"
}

def main():
	try:
		assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
		assert isinstance(sys.argv[1], str), "AssertionError: the arguments are bad"
		if any(char.upper() not in NESTED_MORSE.keys() and char != ' ' for char in sys.argv[1]):
			raise AssertionError("AssertionError: the arguments are bad")
		
		morse_code = " ".join(NESTED_MORSE[char.upper()] for char in sys.argv[1])
		print(morse_code)
	except AssertionError as e:
		print(e)

if __name__ == "__main__":
	main();
