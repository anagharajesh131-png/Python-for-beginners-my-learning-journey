a=float(input("Enter side a="))
b=float(input("Enter side b="))
c=float(input("Enter side c="))
if a + b > c and a + c > b and b + c > a:
    if a==b and b==c:
       print("Triangle is equilateral")
    elif a==b or a==c or b==c:
        print("Triangle is Iscosceles")

    else:
        print("Triangle is Scalene")
else:
    print("Triangle is not valid")
