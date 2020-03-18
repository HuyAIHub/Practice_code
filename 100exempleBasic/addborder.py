def addBorder(picture):
    height = len(picture)+2
    width = len(picture[0])+2
    #shape là 1 comprehension , nếu mà list thì sẽ dùng dấu [] bao quanh, còn là set {} ,...
    # cú pháp : || f(x) for x interable if condition
    shape = [ '*' * width if i == 0 or i == height-1 else '*' +picture[i-1]+ '*' for i in range(height)]
    return print(shape)
addBorder(["wzy**"])
