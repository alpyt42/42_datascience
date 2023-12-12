import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex00.S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('Baratheon', 'brown', 'dark')"

    def __repr__(self):
        return f"Vector: ('Baratheon', 'brown', 'dark')"
    
    def die(self):
        """Override the die method for Baratheon family."""
        super().die()

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('Lannister', 'blue', 'light')"

    def __repr__(self):
        return f"Vector: ('Lannister', 'blue', 'light')"
    
    def die(self):
        """Override the die method for Lannister family."""	
        return super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
    
    
def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.__repr__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
    except Exception as e:
        print(e)
    return
    
if __name__ == "__main__":
    main()
