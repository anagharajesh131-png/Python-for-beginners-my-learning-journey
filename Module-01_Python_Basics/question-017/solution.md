voltage=float(input("Enter the volvage = "))
if voltage >= 0 and voltage <= 1:
    print("Use range: 0 to 1")
elif voltage >= 1 and voltage <= 10:
     print("Use range: 1 to 10")
elif voltage >= 10 and voltage <= 100:
     print("Use range: 10 to 100")

else:
     print("OUT OF RANGE")
     
