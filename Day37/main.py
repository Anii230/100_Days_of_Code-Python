print("\nStar Wars Name Generator\n")

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
mname = input("Enter your mother's maiden name: ")
city = input("Enter the city where you were born: ")

print(
    "\033[0;31m",
    f"\nDear {fname[:3]}{lname[:3].lower()} {mname[:2]}{city[:-3].lower()}, May the force be with you!",
)
