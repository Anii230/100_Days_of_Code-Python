print("\nAnother List\n")
names = []


def viewList():
    print()
    for fullName in names:
        print(fullName)
        print()


while True:
    firstName = input("Enter your First Name: ").strip().capitalize()
    lastName = input("Enter your Last Name: ").strip().capitalize()
    fullName = f"{firstName} {lastName}"
    if fullName not in names:
        names.append(fullName)
        print()
    else:
        print("Name already exists")
        viewList()
