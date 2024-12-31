print("\nMokeBeast\n")
import os, time

beastName = input("Enter your beast's name: ").strip().capitalize()
beastType = input(f"Enter {beastName}'s type: ").strip().capitalize()
beastSmove = input(f"Enter {beastName}'s special move: ").strip().capitalize()
beastHP = input("Enter max HP: ")
beastMP = input("Enter max MP:")

mokedex = {
    "name": beastName,
    "type": beastType,
    "move": beastSmove,
    "hp": beastHP,
    "mp": beastMP,
}
os.system("clear")
time.sleep(1)

if mokedex["type"] == "Earth":
    print("\033[32m", end="")
elif mokedex["type"] == "Air":
    print("\033[37m", end="")
elif mokedex["type"] == "Fire":
    print("\033[31m", end="")
elif mokedex["type"] == "Water":
    print("\033[34m", end="")
else:
    print("\033[33m", end="")

for name, value in mokedex.items():
    print(f"{name}: {value}")
