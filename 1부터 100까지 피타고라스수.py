import math
start=int(input("범위를정하시오"))#미만()
cnt=0
for x in range(1,start+1):
    for y in range(1,start+1):
        s=math.sqrt(x*x+y*y)
        if(int(s)==s): #소수점이 붙지않는 정수로 나누어 떨어질때 가정.
            print(x,y,s)
            cnt = cnt+1
print(cnt)
