print ("\033[33m", """\nHello there! Please answer the following questions to get a short adventure story :)""")
print("\033[36m",)
name = input("Enter your name: ")
frnd = input("Enter your friend's name: ")
place = input("Enter a place you want to visit: ")
number = input("Enter your favourite number: ")
band = input("Enter your favourite band: ")

print ("\033[35m", "\nBizzare Adeventure of", name, "and", frnd)

print("\033[32m", "\nOne day,", name, "and", frnd, "decided to enter a lucky draw for", band + ". The band was performing at", place, "and the flight charge as well as stay was covered in the draw. Apparantly,", name, "and", frnd, "\033[31m", "lost!\nThey were", number, "off from the winning number!" )

