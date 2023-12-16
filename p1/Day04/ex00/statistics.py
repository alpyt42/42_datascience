def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0 and len(kwargs) == 0:
        print("ERROR")
        return
    args = list(args)
    args.sort()
    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            print("mean: ", sum(args) / len(args))
        elif value == "median":
            if len(args) % 2 == 0:
                print("median: ", (args[len(args) // 2] + args[len(args) // 2 - 1]) / 2)
            else:
                print("median: ", args[len(args) // 2])
        elif value == "quartile":
            quartile = []
            if len(args) % 2 == 0:
                quartile_25 = (args[len(args) // 4] + args[len(args) // 4 - 1]) / 2
                quartile_75 = (args[len(args) // 2 + 1] + args[len(args) // 2]) / 2
                quartile.append(float(quartile_25))
                quartile.append(float(quartile_75))
                print("quartile: ", quartile)
            else:
                quartile_25 = args[len(args) // 4]
                quartile_75 = args[len(args) // 2 + 1]
                quartile.append(float(quartile_25))
                quartile.append(float(quartile_75))
                print("quartile: ", quartile)
        elif value == "std":
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print("std: ", variance ** 0.5)
        elif value == "var":
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print("var: ", variance)
    

def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    
if __name__ == "__main__":
    main()
