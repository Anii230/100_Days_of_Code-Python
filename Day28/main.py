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


print("\033[32m", "\n(Epic?) Character Battle\n", "\033[0m")

charName1 = input("Enter the name of first character: ")
charType1 = input("Select the type: Human, Elf, Wizard, Orc, Something else: ")
print("\nCharacter created!\n")
print(charName1, "\nType:", charType1)
char1hp = HealthStat()
char1stg = StrengthStat()
print("Health: ", char1hp, "\nStrength: ", char1stg)

print("\n----------------------------VS----------------------------\n")

charName2 = input("Enter name for second character: ")
charType2 = input("Select the type: Human, Elf, Wizard, Orc, Something else: ")
print("\nCharacter created!\n")
print(charName2, "\nType:", charType2)
char2hp = HealthStat()
char2stg = StrengthStat()
print("Health: ", char2hp, "\nStrength: ", char2stg)

print("\nSimulating battle....")
time.sleep(2)
os.system("clear")
time.sleep(1)


round = 1

while True:
    print(charName1, "VS", charName2)
    print("Round", round, "....Fight!")

    char1Roll = dice(6)
    char2Roll = dice(6)

    damage = abs(char1stg - char2stg) + 1

    if char1Roll > char2Roll:
        print(
            "\n", charName1, "rolled", char1Roll, "and", charName2, "rolled", char2Roll
        )
        print("\n", charName1, "wins round", round)
        char2hp -= damage
        print(
            charName2,
            "takes a hit of,",
            damage,
            "points adjusting to the damage with no clear change in momentum.\n",
        )

        print(charName1)
        print("Health: ", char1hp, "\nStrength: ", char1stg)
        print()
        print(charName2)
        print("Health: ", char2hp, "\nStrength: ", char2stg)
        print()
        round += 1
        time.sleep(1)
        os.system("clear")

        if char2hp < 0:
            print(charName1)
            print("Health: ", char1hp, "\nStrength: ", char1stg)
            print()
            print(charName2)
            print("Health: ", char2hp, "\nStrength: ", char2stg)
            print()

            print(charName2, "succumbs to the final blow, their journey ends here.")
            print(
                "After",
                round - 1,
                "intense rounds,",
                charName1,
                "emerges victorious, standing tall as the battle comes to an end.",
            )
            break
        else:
            continue

    elif char2Roll > char1Roll:
        print(
            "\n", charName1, "rolled", char1Roll, "and", charName2, "rolled", char2Roll
        )
        print("\n", charName2, "wins round", round)
        char1hp -= damage
        print(
            charName1,
            "takes a hit of,",
            damage,
            "points adjusting to the damage with no clear change in momentum.\n",
        )

        print(charName1)
        print("Health: ", char1hp, "\nStrength: ", char1stg)
        print()
        print(charName2)
        print("Health: ", char2hp, "\nStrength: ", char2stg)
        print()
        round += 1
        time.sleep(1)
        os.system("clear")

        if char1hp < 0:
            print(charName1)
            print("Health: ", char1hp, "\nStrength: ", char1stg)
            print()
            print(charName2)
            print("Health: ", char2hp, "\nStrength: ", char2stg)
            print()

            print(charName1, "succumbs to the final blow, their journey ends here.")
            print(
                "After",
                round - 1,
                "intense rounds,",
                charName2,
                "emerges victorious, standing tall as the battle comes to an end.",
            )
            break
        else:
            continue
