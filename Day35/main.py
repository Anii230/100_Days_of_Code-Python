print("\033[0;35m", "\nTO-DO List But Better!\n", "\033[0m")

ToDoList = []


def viewList():
    print()
    for items in ToDoList:
        print("\033[0;36m", items, "\033[0m")
    print()


def clearList():
    global ToDoList
    verify = input("Are you sure you want to clear the whole list? ")
    if verify == "yes":
        ToDoList = []
        print("List Cleared Successfully\n")
    elif verify == "no":
        print("Operation Cancelled!\n")


def addItem():
    items = input("What do you want to add? ")
    if items not in ToDoList:
        ToDoList.append(items)
        print("\033[0;32m", f"{items} added successfully!\n", "\033[0m")
    else:
        print(f"{items} already present in the list!\n")


def removeItem():
    items = input("What item do you want to remove? ")
    if items in ToDoList:
        verify = input(f"Are you sure you want to remove {items}? ")
        if verify == "yes":
            ToDoList.remove(items)
            print("\033[0;31m", f"{items} removed successfully\n", "\033[0m")
        elif verify == "no":
            print("Operation Cancelled\n")
        else:
            print("\033[1;33m", f"{items} not found in ToDoList\n", "\033[0m")


def editItem():
    edit = input("What do you want to edit? ")
    if edit not in ToDoList:
        print(f"{edit} not found")
    else:
        print("Item Found!")
        newItem = input("Enter new item: ")
        for i in range(0, len(ToDoList)):
            if ToDoList[i] == edit:
                ToDoList[i] = newItem
                print("Edited Successfully!\n")


while True:
    action = input("Add (a), View (v), Edit (e), Remove (r), Clear(c), or exit (ex): ")

    if action == "a":
        addItem()

    elif action == "r":
        removeItem()

    elif action == "v":
        viewList()

    elif action == "e":
        editItem()

    elif action == "c":
        clearList()

    elif action == "ex":
        break
