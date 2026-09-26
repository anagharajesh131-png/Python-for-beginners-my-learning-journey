n = int(input("Enter the number of measurements = "))

total = 0
count = 0

for i in range(n):
    measurement = float(input("Enter Measurement: "))

    if measurement >= 0:
        total = total + measurement
        count = count + 1

if count > 0:
    average = total / count
else:
    average = 0

print(f"Sum = {total}")
print(f"Average = {average}")
print(f"Valid measurements = {count}")
