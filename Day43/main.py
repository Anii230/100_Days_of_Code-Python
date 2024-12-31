import random

print("\nBINGO card generator\n")

bingo = []


def ran():
    num = random.randint(1, 90)
    return num


def prettyPrint():
    for row in bingo:
        print(row)


numbers = []

for i in range(8):
    numbers.append(ran())

numbers.sort()

bingo = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], "BINGO", numbers[4]],
    [numbers[5], numbers[6], numbers[7]],
]

prettyPrint()
