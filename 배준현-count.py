txt="""난 너를 믿었던 만큼 야 라고 해도오레오. 야이마
리아 그대여 오 나의 그대여 예예예 어디에 있나요. 그저
바라만 보내요. 용덕아 어디에 가는냐 바바리맨과 함께 가느냐
그대여 널 부르는 그 소리에 도라이냐!"""
lx=list(txt)
sx=set(lx)
print(sx)
mymax=0
mun=""
for i in sx:
    if i !=" " and i !='.':
        print(i, lx.count(i))#sx의 리스트를 뽑아 count를 하여 골라낸다.
        if lx.count(i) > mymax:
            mymax=lx.count(i)
            mun=i
print("가장많이 기록된 문자: ",mun , "=" , mymax)

