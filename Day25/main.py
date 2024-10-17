import random

print("\nCharacter generator")
# sides = int(input("Enter number of sides: "))


def rollDice(sides):
    roll = random.randint(1, sides)
    return roll


def charHealth():
    # char = input("What's the name of your character: ")
    roll6 = rollDice(6)
    roll8 = rollDice(8)
    hp = roll6 * roll8
    return hp


hasChar = "y"

while hasChar == "y":
    char = input("\nEnter the name of your character: ")
    hp = str(charHealth())
    print("\033[32m", char, "has a health stat of", hp, "\033[0m")
    hasChar = input("\nDo you want to create a new character? ")
