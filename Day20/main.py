print("\nList Generator\n")

StartNum = int(input("Enter starting number: "))
EndNum = int(input("Enter ending number: "))
Inc = int(input("Enter increment "))

for i in range(StartNum, EndNum, Inc):
    print(i)
