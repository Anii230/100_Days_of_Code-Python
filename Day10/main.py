print("\nBill Splitter\n")

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))

tip = input("Would you like to leave a tip? Y or N: ")
if tip == "Y" or tip == "y":
    inptip = int(input("How much % you like to tip? 10%, 15%, 10% or 20%? "))
    inptip = inptip/100*myBill+myBill
    answer = inptip / numberOfPeople
    FinalBill = round(answer, 2)
    print("You all owe", FinalBill)
elif tip == "N" or tip == "n":
    answer = myBill/numberOfPeople
    FinalBill = round(answer, 2)
    print("You all owe", FinalBill)
else:
    print("Wrong input, defaults to 'No'")
    answer = myBill/numberOfPeople
    FinalBill = round(answer, 2)
    print("You all owe", FinalBill)
