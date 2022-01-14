#Dice rolling app requiring user input to start
import random

min = 1
max = 6

new_roll = input("Type ROLL to throw the dice.\n")

if new_roll == "ROLL":
    print("You Rolled...\n")
    print(random.randint(min, max));

