print("\nGrade Calculator\n")

subject = input("Enter name of the subject: ")
maxMarks = float(input("Enter max marks you can get: "))
marks = float(input("Enter the marks you got: "))

print("\nYou recieved", marks, "out of", maxMarks, "in", subject, "\n")
percentage = round((marks / maxMarks) * 100, 2)
print("You percentage is", percentage, "%")

if percentage >= 90:
    print("You got A+ 🥳")
elif percentage >= 80 and percentage <= 89:
    print("You got A 🙌")
elif percentage >= 70 and percentage <= 79:
    print("You got B")
elif percentage >= 60 and percentage <= 69:
    print("You got C")
elif percentage >= 50 and percentage <= 59:
    print("You got D")
elif percentage <= 49:
    print("grade F 💀💀💀")
else:
    print("Invalid")
