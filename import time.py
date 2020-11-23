import time
ctimestring =  time.ctime()
print(ctimestring)

print("수행시간 측정해보기")

start = time.clock()
s = 0
for x in range(10000) :
    for y in range(1000) :
        s += 1


end = time.clock( )
print("전체 걸린 시간(mili second)=", end-start)