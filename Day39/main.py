print("\nCars Hangman\n")

import random, os, time

list = ["mercedes", "audi", "bugatti", "lamborgini", "moddisircar"]
lettersPicked = []
lives = 6

word = random.choice(list)

while True:
    time.sleep(1)
    os.system("clear")

    letter = input("\nEnter a letter: ")
    if letter in lettersPicked:
        print("You already guessed that!")
        continue

    lettersPicked.append(letter)

    if letter in word:
        print("You found a letter")
    else:
        print("Not in the word")
        lives -= 1

    allLetters = True
    for i in word:
        if i in lettersPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print(f"You won with {lives} left")
        break

    if lives <= 0:
        print(f"You ran out of lives! the word was {word}")
        break
    else:
        print(f"{lives} left")
