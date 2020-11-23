def merong():
    pass

print("그냥 불러옵니다" , merong())

def listsum(this, start, end):
    s = 0
    for i in range(start , end):
        s += this[i]
    return(s)

mylist = [3,5,6,8,9,10,-22,5,8]

print("리스트 list의 전체 합은 %s " % listsum( mylist,2,5))
