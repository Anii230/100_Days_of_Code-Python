import random

print("\nGuess the number\n")

counter = 0
number = random.randint(1, 1000000)

while True:
    num = int(input("Enter a number between 0 and 1,000,000: "))
    if num < 0:
        print("Damm son..")
        break
    elif num == number:
        counter += 1
        print("you guessed it right🥳!")
        print("you took", counter, "attempts to guess!")
        break
    elif num > number:
        print("too high\n")
        counter += 1
    elif num < number:
        print("too low\n")
        counter += 1
    else:
        print("invalid")
        break

    if counter == 10:
        print("You took too long to guess! The number was", number)
        break
