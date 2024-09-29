print("Are you a real fan?\n")

band = input("Select a band- A7X and Muse: ")

if band == "A7X":
    print("\nGreat choice, here's the first question")
    b1a1 = input("What's the name of the 3rd song of thier 2nd album?? ")
    if b1a1 != "blinded in chains":
        print("Poser!")
    else:
        print("\nGood, here's the second question")
        b1q2 = input("What's the stage name of their lead guitarist? ")
        if b1q2 != "syn" and b1q2 != "synyster gates" and b1q2 != "gates":
            print("Poser!")
        else:
            print("\nGreat, now here's the last question")
            b1q3 = input("Name a song related to necrophelia: ")
            if b1q3 != "a little piece of heaven":
                print("Poser")
            else:
                print("\nok you pass!")

elif band == "Muse":
    print("\nGreat pick! Here's the first question")
    b2q1 = input("What's the 5th studio album called? ")
    if b2q1 != "the resistance" and b2q1 != "resistance":
        print("Poser")
    else:
        print("\nNice, here's the second question")
        b2q2 = input("What's the song with the best riff? ")
        if b2q2 != "plug in baby":
            print("poser")
        else:
            print("\nGreat now here's the last question")
            b2q3 = input("What song did they perform at the closing ceremony of the olympics 2013? ")
            if b2q3 != "survival":
                print("Poser")
            else:
                print("\nok you pass")
else:
    print("no questions")
