import random

print("\nInfinity Dice\n")
sides = int(input("Enter number of sides: "))


def rollDice():
    print("You rolled", random.randint(1, sides))


rollDice()

while True:
    again = input("\nRoll again? y/n: ")
    if again == "y":
        rollDice()
    elif again == "n":
        print("Thnx for playing")
        break
    else:
        print("Wrong input")
