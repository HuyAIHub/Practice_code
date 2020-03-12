#Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng, phân tách
# bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
x=int(input("Nhập số cần tính giai thừa:"))
def fact(x):
    if x == 0:
      return 1
    return x * fact(x - 1)
print (fact(x))
