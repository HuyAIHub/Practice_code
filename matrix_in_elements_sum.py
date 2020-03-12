# cho bạn 1 ma trận ! hãy tính tổng các số của ma trận
# điều kiện  , tính theo cột : các ô được tính sum là phải nằm trên ô 0
def matrix(s):
# matrix = [[1,2,0,1],
#           [2,0,3,2],
#           [0,2,4,3]]
    sum = 0
    for j in range(len(s[0])):
        for i in range(len(s)):
            if s[i][j]!=0:
                sum += s[i][j]
            else:
                break
    print(sum)

matrix(s=[[1,2,0,1],
           [2,0,3,2],
           [0,2,4,3]])