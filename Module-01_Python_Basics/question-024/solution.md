m = int(input("Enter the number of rows = "))
n = int(input("Enter the number of columns = "))

for row in range(1, m+1):

    for column in range(1, n+1):

        print( row* column, end=" ")

    print()
