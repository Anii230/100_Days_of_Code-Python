print("\nseconds in a year\n")

DaysInCurrentYear = int(input("How many days in this year? "))

DaysInYear = 365
DaysInLeapYear = 366
HoursInDay = 24
MinuteInHour = 60
SecondsInMinute = 60

NormalYear = DaysInYear * HoursInDay * MinuteInHour * SecondsInMinute
LeapYear = DaysInLeapYear * HoursInDay * MinuteInHour * SecondsInMinute

if DaysInCurrentYear == 365:
    print("Number of seconds in this year is ", NormalYear)
elif DaysInCurrentYear == 366:
    print("Number of seconds in leap year is ", LeapYear)
else:
    print("Invalid Input")
