# nếu là -1 thì giữ nguyên vị trí , còn là số khách thì sắp xếp tăng dần
def sortByHeight(a):
    c = sorted([i for i in a if i!=-1])
    for i in range(len(a)):
        if a[i]==-1: c.insert(i,-1)
    return c
# chưa hiểu này
