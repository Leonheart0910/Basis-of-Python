강민호= "hhoohhhhooohhh"
#double loop사용 =for loop 안에 for loop이 하나 더있음을 나타냄
n=(len(강민호))
for x in range(n):
    for y in range(x,n):
        print(x,y,강민호[x:y+1])
        #range(x+1,n), 없을때와 [x+1 : y]와 위의 차이