sum=0
cnt=0
a=open("shooting.inp","r")
b=open("shooting.out","w")
w=a.readline()
ls=list(w)
for i in ls:
    if(i =='h'):
        cnt=int(cnt+1)
        sum=int(sum+cnt)
    elif(i=='o'):
        cnt=0
        sum=sum-1
print(sum,file=b)
a.close()
b.close()

