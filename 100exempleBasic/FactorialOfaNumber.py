# tìm giai thừa của 1 số
x = int(input("enter a number :"))
factorial = 1
if x < 0 :
    print("sorry, the factorial does not exist for negative numbers")
elif x == 0:
    print("the factorial is zero")
else:
    for i in range(1, x +1):
        factorial *=i
    print("the value of factorial is : {}".format(factorial))