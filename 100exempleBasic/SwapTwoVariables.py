# python program to swapping two varibales
x = input("enter value x :")
y = input("enter value y :")

# creat a temporary variable and swap the values
temp = x
x = y
y = temp
#other case : x,y = y,x
print("the value of x after swapping : {}".format(x))
print("the value of y after swapping : {}".format(y))
print("the result of temp : {}".format(temp))