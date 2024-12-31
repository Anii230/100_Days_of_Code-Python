print("\nDictionary\n")
import time, os

name = input("Enter your name: ").strip().capitalize()
dob = input("Enter date of birth: ").strip()
email = input("Enter email address: ")
address = input("Enter your current address: ")

contact = {"name": name, "dob": dob, "email": email, "address": address}
os.system("clear")
time.sleep(1)

print(f"Name: {contact['name']}")
print(f"Date of Birth: {contact['dob']}")
print(f"Email: {contact['email']}")
print(f"Address: {contact['address']}")

