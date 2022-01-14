#Dice rolling app requiring user input to start
import random

min = 1
max = 6

computer_die = random.randint(min, max)
user_die = random.randint(min, max)

new_roll = input("Type 'roll' to throw the dice.\n")

if new_roll == "roll":
    print("You Rolled...")
    print(user_die);
    print("The Computer Rolled...")
    print(computer_die)

    if user_die > computer_die:
        print("\n YOU WIN!")
    else:
        print("\n You Lose :(")