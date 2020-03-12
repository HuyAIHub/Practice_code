 def isLucky(a):
    while (n > 0):
        temp = int(n % 10)
        n = int(n / 10)
        a.append(temp)
    print(a)
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        if i < len(a) / 2:
            sum1 = sum1 + a[i]
        else:
            sum2 += a[i]
    if (sum1 == sum2):
        print("haha you're corect")
    else:
        print("you're wrrong")


isLucky(n= 1221)