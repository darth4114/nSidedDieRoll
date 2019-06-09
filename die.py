import random as r


class Die():
    '''
    Generate an n sided die to roll
    '''

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return r.randint(1, self.sides)


def ask_sides():

    while True:
        sides = int(input("How many sides is your die? "))

        if sides < 4:
            print("Sorry, you cannot have a die of less than 4 sides\nPlease try again.")
            continue
        else:
            print("You have chosen a {sides}-sided die")
            break

    return sides


def ask_roll():

    while True:
        try:
            ans = int(input("\nHow many die do you want to roll? "))
        except ValueError:
            print("\nSorry, I didn't understand you")
            continue
        else:
            break

    return ans
