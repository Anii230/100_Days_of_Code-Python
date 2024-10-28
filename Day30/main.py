print("\nDaily log (kinda?)\n")

for i in range(1, 31):
    day = input(f"Day {i}: ")
    text = f"You thought Day{i} was"
    print(f"{text:^35}")
    print(f"{day:^35}\n")
