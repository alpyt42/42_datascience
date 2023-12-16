import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex00.S1E9 import Character
from ex01.S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        self.eyes = color

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, color):
        self.hairs = color

    def get_hairs(self):
        return self.hairs
    
def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    
if __name__ == "__main__":
    main()