arr1 = 0
arr2 = 0
a1 =[]
a2 = []

a = [50, 60, 60, 45, 70]
for i in range(len(a)):
    if i % 2== 0:
        arr1 += a[i]
    else:
        arr2 += a[i]
a1.append(arr1)
a1.append(arr2)
print(arr1)
print(arr2)
print(a1 + a2)