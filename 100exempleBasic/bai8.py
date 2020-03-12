#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
#Gợi ý:
#Khi định nghĩa tham số instance, cần thêm nó vào __init__
#Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.
class Person:
    # định nghĩa lớp "name"
    name = "Person"
def __init__(self,name = None):
#self.name là biến instance
    self.name = name
huy = person("huy")
print("%s name is %s"%(Person.name,huy.name))
nico = person()
nico.name = "Nico"
print("%s name is %s" % (Person.name , nico.name))
