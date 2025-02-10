import random

class Character:
    #class attributes 
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Flying", "Invisibility", "Super strength"]
    height = ["Short", "Medium", "Tall"]

    #Construtor 
    def__init__(self) : 
        self.generate_character()

    def generate_character(self):
        self.hair_color = random.choice(Character.hair_colors)
        self.sizes = random.choice(Character.sizes)
        self.special_powers = random.choice(Character.special_powers)
        self.height = random.choice(Character.height)
        self.description = (
            f"Your charactr has {self.hair_color} hair, "
            f"is {self.sizes} in size, has the power of {self.special_powers}, "
            f"and is {self.height}"
        )

    def__str__(self) :
        return self.description

Char1 = Character()
Char2 = Character()
print(Char1)
print(Char2)
