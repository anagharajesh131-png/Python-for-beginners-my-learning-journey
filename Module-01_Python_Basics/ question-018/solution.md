year = int(input("Enter year:"))
day = int(input("ENter the day:"))

if (year % 400 ==0) or (year % 4 == 0 and year % 100 != 0 ):
    print("Leap year")
    max_day = 366

else:
    print("Not a leap year")
    max_day = 365

if day >= 1 and day <= max_day:
    print("Valid day number")
else:
    print("Invalid day number")            
