#Viết chương trình chấp nhận một chuỗi số,
#phân tách bằng dấu phẩy từ giao diện điều khiển,
#tạo ra một danh sách và một tuple chứa mọi số.
values = input("nhập giá trị :")
l = values.split(",")
t = tuple(l)
print(l)
print(t)