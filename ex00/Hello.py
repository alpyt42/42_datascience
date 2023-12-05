ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

# Note : Les tuples sont immuables, on ne peut pas modifier un élément, vous doit creer un nouveau tuple
ft_tuple = (ft_tuple[0], "France!")

ft_set.discard("tutu!")
ft_set.add("Lyon!")

# Modifier la valeur associée à la clé "Hello" dans le dictionnaire
ft_dict["Hello"] = "42Lyon!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
