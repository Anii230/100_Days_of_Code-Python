import random, os, time

def dice(sides):
    roll = random.randint(1, sides)
    return roll

def HealthStat():
    hp = (dice(6) * dice(12) / 2) + 10
    return hp

def StrengthStat():
    stg = (dice(6) * dice(8) / 2) + 12
    return stg

while True:
    print("\nCharacter Builder\n")
    charName = input("Enter the name of your character: ")
    charType = input("Select the type: Human, Elf, Wizard, Orc, Something else: ")
    print("\nCharacter created!\n")
    print(charName, "\nType:", charType)
    print("Health: ", HealthStat())
    print("Strangth: ", StrengthStat())
    print("\nMay the force be with you!\n")

    newChar = input("Create a new character? y/n: ")
    if newChar == "y":
        time.sleep(1)
        os.system("clear")
        continue
    elif newChar == "n":
        break
    else:
        print("Invalid")
