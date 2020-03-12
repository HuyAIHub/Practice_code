#Định nghĩa một class có ít nhất 2 method:
'''
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

printString: in chuỗi vừa nhập sang chữ hoa.

Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM
'''
class InputString(object):
    def __int__(self):
        self.s = ""
    def getString(self):
        self.s = input("mời bạn nhập vào 1 chuỗi:")
    def printString(self):
        print(self.s.upper())

strObj = InputString()
strObj.getString()
strObj.printString()