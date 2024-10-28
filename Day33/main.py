print("\033[0;35m", "\nTO-DO List\n", "\033[0m")

ToDoList = []


def viewList():
    print()
    for items in ToDoList:
        print("\033[0;36m", items, "\033[0m")
    print()


while True:
    action = input("Add (a), View (v), Remove (r), or exit (e): ")

    if action == "a":
        items = input("\nWhat should be added? ")
        ToDoList.append(items)
        print("\033[0;32m", f"{items} added successfully!\n", "\033[0m")

    elif action == "r":
        items = input("\nWhat should be removed? ")
        if items in ToDoList:
            ToDoList.remove(items)
            print("\033[0;31m", f"{items} removed successfully\n", "\033[0m")
        else:
            print("\033[1;33m", f"{items} not found in ToDoList\n", "\033[0m")

    elif action == "v":
        viewList()

    elif action == "e":
        break
