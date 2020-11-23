DNA="agtggtc"
#    0123456
print(DNA[1:4])#[1:4]4를 넘지않는 수까지이다 <4 의 의미
print(DNA[4:7])

N=len(DNA)
for i in range(N):
    for j in range(i+1,N+1):
        print("i,j=",i,j-1,"=>",DNA[i:j])

