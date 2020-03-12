# tính diện tích tam giác : tổng 3 cạnh chia 2
a = float(input("enter the value of a :"))
b = float(input("enter the value of b :"))
c = float(input("enter the value of c :"))

s = (a + b + c)/2 # đây là chu vi
print("the valude of perimeter: {}".format(s)) # perimeter is : chu vi
A = (s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle is %0.2f" %A)