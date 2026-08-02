voltage=float(input("voltage="))
current=float(input("current="))
time=float(input("time="))
power=voltage*current
energy=power*time
print(f"power={power} watts")
print(f"energy={energy} wh")
kwh=energy/1000
print(f"energy={kwh} kwh")
