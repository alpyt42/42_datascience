from typing import Any

def callLimit(limit: int):
    """
    Un décorateur pour limiter le nombre de fois qu'une fonction peut être appelée.

    Args:
    limit (int): Le nombre maximal d'appels autorisés pour la fonction décorée.
    """
    def callLimiter(function):
        """
        Une fonction décoratrice qui enveloppe la fonction donnée et limite son nombre d'appels.

        Args:
        function (): La fonction à limiter.
        """
        count = 0  # Compteur pour suivre le nombre d'appels

        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            La fonction interne qui est appelée à la place de la fonction originale.
            Elle vérifie le compteur avant d'appeler la fonction originale.

            Args:
            *args: Arguments positionnels pour la fonction décorée.
            **kwds: Arguments nommés pour la fonction décorée.

            Returns:
            Any: Le résultat de la fonction décorée, si le nombre d'appels est inférieur à la limite.
            """
            nonlocal count  # Référence la variable 'count' du scope parent
            if count < limit:
                count += 1  # Incrémente le compteur
                return function(*args, **kwds)  # Appelle la fonction originale
            else:
                print(f"Error: {function} call too many times")

        return limit_function  # Retourne la fonction limitée

    return callLimiter  # Retourne le décorateur

def main():
    @callLimit(3)  # Décore la fonction 'f' pour limiter son appel à 3 fois
    def f():
        print("f()")

    @callLimit(1)  # Décore la fonction 'g' pour limiter son appel à 1 fois
    def g():
        print("g()")

    for i in range(3):  # Boucle pour tester les limites des fonctions
        f()
        g()

if __name__ == "__main__":
    main()
