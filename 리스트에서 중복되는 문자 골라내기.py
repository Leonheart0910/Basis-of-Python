a=list("communication")
a.sort()
print(a)
b=[]
for i in range(len(a)-1):#len(a)는 12인데 -1을 하지않으면 a의 13자리는 없으므로
    print(a[i],a[i+1])
    if a[i]==a[i+1]:
        b.append(a[i]) #append뒤 ()중요!
print("b=",b)
