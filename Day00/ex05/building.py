import sys


def main():
    assert len(sys.argv) <= 2, "AssertionError: too many arguments"
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in "#$%&'()*+,-./:;<=>?@":
            punctuation_count += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
