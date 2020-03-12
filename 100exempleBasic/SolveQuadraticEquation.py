#giải phương trình bậc 2
import cmath
a = float(input("enter the value of a :"))
b = float(input("enter the value of b :"))
c = float(input("enter the value of c :"))
denta = (b**2) - (4*a*c)
# find two solutions
solution1 = (-b - cmath.sqrt(denta))/(2*a)
solution2 = (-b + cmath.sqrt(denta))/(2*a)
print("the solution are {0} and {1}".format(solution1,solution2))


