# in tất cả các số nguyên tố trong khoảng
start = int(input("enter value start number :"))
end = int(input("enter value end number :"))

for i in range(start,end+1):

        for j in range(2,i):
            if (i%j)==0:

                break
        else:
            print(i)
