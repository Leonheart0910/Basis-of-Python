


a=0   # a 라는 변수에 값을 정해주어야 한다
a= a + 10 # a 라는 변수에 값을 정해주어야 한다
int(a) #a 를 문자열에서 정수로 변환
print(a)

cnt=0
i=0
s="hooohhhohh"
ls = list(s) #stepwise refine
print(ls, "\n" , len(ls))

for w in ls :
    print(w , end = " ")#print는 한줄쓰고 건너띄기 때문에
    #end= 을 사용하여 건너띈 다음 열을 붙여씀
    if(w =='h') : #h는 문자열이기 때문에 'h'사용
        print("맞춤")
        cnt=int(cnt+1)
    else :
        print("헛방")
        cnt=int(cnt-1)
print(cnt)