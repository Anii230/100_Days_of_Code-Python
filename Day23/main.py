print("\nLogin\n")

username = "Anoket"
userpass = "AnoketBhoi"


def login():
    while True:
        uname = input("Enter your username: ")
        upass = input("Enter your password: ")

        if uname == username and upass == userpass:
            print("\nWelcome Bhai\n")
            break
        else:
            print("\nWrong username or password\n")
            continue


login()
