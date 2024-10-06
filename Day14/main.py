from getpass import getpass

print("\nRock Paper Scissors\n")

p1 = input("Enter player 1 name: ")
p2 = input("Enter player 2 name: ")

print("\nRock: R, Paper: P, Scissors: S\n")

p1m = getpass(p1 + ", enter your choice: ")
p2m = getpass(p2 + ", enter your choice: ")

if p1m == "R":
    if p2m == "R":
        print(p1, "and", p2, "choose rock! its a tie")
    elif p2m == "P":
        print(p2m, "catches", p1m, p2, "wins!")
    elif p2m == "S":
        print(p1m, "crushes", p2m, p1, "wins!")
    else:
        print("Wrong Input")
elif p1m == "P" or p1m == "p":
    if p2m == "R" or p2m == "r":
        print(p1m, "catches", p2m, p1, "wins!")
    elif p2m == "P" or p2m == "p":
        print("Both choose paper! its a tie")
    elif p2m == "S" or p2m == "s":
        print(p2m, "cuts", p1m, p2, "wins!")
    else:
        print("Wrong Input")
elif p1m == "S" or p1m == "s":
    if p2m == "R" or p2m == "r":
        print(p2m, "crushes", p1m, p2, "wins!")
    elif p2m == "P" or p2m == "p":
        print(p1m, "cuts", p2m, p1, "wins!")
    elif p2m == "S":
        print("Both choose Scissors! its a tie")
    else:
        print("Wrong Input")
else:
    print("Wrong input")

print("\nThanks for playing!\n")
