# kiểm tra số có phải là số nguyên tố hay k
def checkPrime(s):
    if s <= 0:
        print("dau khong phai so nguyen to ")
    else:
        for i in range(1 , s):
            if(s % 2)==0:
                print("day k phai so nguyen to")
                break
        else:
                print("%d la so nguyen to"%s)

checkPrime(402)