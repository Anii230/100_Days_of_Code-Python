print("\nMultiplication table\n")

num = int(input("Enter the table you want to take: "))
print()
counter = 0

for i in range (1,11):
    tab = i*num
    ans = int(input(f"{num} X {i} = "))
    if ans == tab:
        counter += 1
if counter == 10:
    print("\n Damn son, A perfect score 🥶")
else:
    print("\nNice, you got", counter, "out of 10")
