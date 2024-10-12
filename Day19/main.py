loan = 6942
apr = 0.05
for i in range(12):
    loan += loan * apr
    print("your loan for year", i + 1, "is", round(loan, 2))
