for w in range(1,100,10):
    print("call" , w)

for i , w in enumerate(range(1,100,10)):
    print("call" , i , w)


ml = list("나는 니가 좋아")
man = " " #문자열에서 변수를 설정 문자입력 가능해짐
ppe=list("aeiou ")
for i ,q in enumerate(ml):
    if q not in ppe :
         man = man + q
print("man=",man)

#" "과' '의 차이 문자열안에 문자열을 묶을때의 차이
# 거의 차이가 없다 " 과 ' 는 기능은 같음---> 공백