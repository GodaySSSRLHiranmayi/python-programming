print("Input lengths of triangle:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x==y==z:
    print("Triangle is equilateeral")
elif x==y or y==z or z==x:
	print("Triangle is isosceles triangle")
else:
	print("Triangle is Scalene triangle")
