power=float(input("power in watts="))
hours=float(input("hours="))
cost=float(input("cost="))
kW=power/1000
daily_energy=kW*hours
monthly_energy=daily_energy*30
monthly_cost=monthly_energy*cost
print(f"monthly_energy={monthly_energy:.2f}kWh")
print(f"monthly_cost={monthly_cost:.2f}rupees")      
