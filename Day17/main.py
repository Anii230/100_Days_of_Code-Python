from getpass import getpass

print("\nRock Paper Scissors\n")

p1 = input("Enter player 1 name: ")
p2 = input("Enter player 2 name: ")

p1Score = 0
p2Score = 0

print("\nRock: R, Paper: P, Scissors: S\n")

while True:
    p1m = getpass(p1 + ", enter your choice: ")
    p2m = getpass(p2 + ", enter your choice: ")

    if p1m == "R":
        if p2m == "R":
            print(p1, "and", p2, "choose rock! its a tie\n")
        elif p2m == "P":
            print(p2m, "catches", p1m, p2, "wins!\n")
            p2Score += 1
        elif p2m == "S":
            print(p1m, "crushes", p2m, p1, "wins!\n")
            p1Score += 1
        else:
            print("Wrong Input")
    elif p1m == "P" or p1m == "p":
        if p2m == "R" or p2m == "r":
            print(p1m, "catches", p2m, p1, "wins!\n")
            p1Score += 1
        elif p2m == "P" or p2m == "p":
            print("Both choose paper! its a tie\n")
        elif p2m == "S" or p2m == "s":
            print(p2m, "cuts", p1m, p2, "wins!\n")
            p2Score += 1
        else:
            print("Wrong Input")
    elif p1m == "S" or p1m == "s":
        if p2m == "R" or p2m == "r":
            print(p2m, "crushes", p1m, p2, "wins!\n")
            p2Score += 1
        elif p2m == "P" or p2m == "p":
            print(p1m, "cuts", p2m, p1, "wins!\n")
            p1Score += 1
        elif p2m == "S":
            print("Both choose Scissors! its a tie\n")
        else:
            print("Wrong Input\n")
    else:
        print("Wrong input")

    print(p1, "has", p1Score, "points")
    print(p2, "has", p2Score, "points\n")

    if p1Score == 3:
        print(p1, "Wins!")
        print("\nThanks for playing!\n")
        exit()
    elif p2Score == 3:
        print(p2, "Wins!")
        print("\nThanks for playing!\n")
        exit()
    else:
        continue
