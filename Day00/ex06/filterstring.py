from ft_filter import ft_filter
import sys


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        assert isinstance(sys.argv[1], str), "AssertionError: the arguments are bad"
        assert sys.argv[2].isdigit(), "AssertionError: the arguments are bad"

        textsplit = sys.argv[1].split()
        nb = int(sys.argv[2])
        result = ft_filter(lambda x: len(x) > nb, textsplit)
        print(result)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()