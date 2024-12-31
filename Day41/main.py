print("\nDictionary p2\n")
import os, time

url = input("Enter a url: ").strip().capitalize()
desc = input("Enter description: ").strip().capitalize()
rate = input("Rate it out of 5: ")

website = {"url": url, "description": desc, "rating": rate}
os.system("clear")
time.sleep(1)

for name, value in website.items():
    print(f"{name}: {value}")
