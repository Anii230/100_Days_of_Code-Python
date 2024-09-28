print("\nPlease login to proceed\n")

name = input("Enter your name: ")
password = input("Enter your password: ")

if (name == "Anoket" and password == "2305"):
    print("Welcome bhoi!")
elif (name == "Selmon" and password == "bhoi"):
    print("Aare bhai aap?!")
elif (name == "Admin" and password == "pass@123"):
    print("Welcome 🙏")
else:
    print("Failed to authorize!")
