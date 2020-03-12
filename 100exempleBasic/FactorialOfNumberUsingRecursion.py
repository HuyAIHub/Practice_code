# tính giai thừa sử dụng hàm đệ quy
def Recursion_factorial(n):
    if n == 1:
        return 1
    elif n <=0:
        print("sorry,can't calculate this number")
    else:
        return (n*Recursion_factorial(n-1))
num = int(input("enter the value num :"))
print("the factorial of num is :","the factorial of num is :","the factorial of num is :","the factorial of num is :", Recursion_factorial(num),sep="---")