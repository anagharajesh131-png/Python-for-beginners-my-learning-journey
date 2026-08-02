temperature=float(input("Enter the temperaure in Kelvin ="))
if temperature < 273:
    print("solid state: ice")
elif temperature <= 373:
    print("liquid state: water")
else:
    print("gaseous state: vapour")
