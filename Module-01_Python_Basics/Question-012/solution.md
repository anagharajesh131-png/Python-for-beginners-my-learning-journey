header=["Name", "Age", "Place"]
rows=[
    ["Anagha", "20", "Chennai"],
    ["Sanju", "22", "Delhi"],
    ["Devi", "27", "Pune"]
]
print("-" * 35)

for item in header:
    print(f"{item:<10}", end="")
print()

print("-" * 35)

for row in rows:
    for item in row:
        print(f"{item:<10}", end="")
    print()

print("-" *35)
