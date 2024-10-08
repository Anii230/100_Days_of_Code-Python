print("\nGuess the lyrics")

counter = 1
while True:
    print("\nThere's only one ____ left!")
    lyric1 = input("Enter your guess: ")
    if lyric1 == "beer" or lyric1 == "Beer":
        break
    else:
        print("Wrong! try again")
        counter = counter + 1
print("You took", counter, "attempts to guess")
