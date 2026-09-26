import math

def circle_area(r):
    area = math.pi * r ** 2
    return area

radius =float(input("Enter radius: "))

result = circle_area(radius)

print(f"Area = {result:.2f}")
