import random

class Dice:
    def roll(self):
        number1=random.randint(1,6)
        number2=random.randint(1,6)
        my_Dice_tuple=(number1,number2)
        return my_Dice_tuple