from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class for game characters."""
    
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to set character's alive status to False."""
        self.is_alive = False

class Stark(Character):
    """Class for characters of the Stark family."""

    def die(self):
        """Override the die method for Stark family."""
        super().die()

def main():
    try:
        Jon = Character("Jon") # TypeError: Can't instantiate abstract class Character with abstract methods die
    except TypeError as e:
        print(e)
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main();