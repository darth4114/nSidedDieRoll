import die as d

print("Welcome to the Dice rolling app. You will be able to choose how many sides your dice have, and how many you are rolling.")

sides = d.ask_sides()
roll = d.ask_roll()

dice = d.Die(sides)

print(f"\nHere are the results from rolling {roll} {sides}-sided dice:")

for i in range(roll):
    print(dice.roll())
