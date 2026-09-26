n = int(input("Enter the number of rows: "))

for row in range(1,n+1):
    for star in range(row):
        print("*", end ="")
    print()
