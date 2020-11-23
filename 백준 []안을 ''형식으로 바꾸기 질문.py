import sys
n = sys.stdin.readline()
ml = list(n) ; ml.pop(-1)
p = (len(ml)//10) + 1
for i in range(k):
    q = ml[10*i:10*(i+1)] #[a:b]기호 주의!
    print(q)
#리스트의 [a,b,c]들을 abc로 출력되게 학 싶을때
#어떤 함수를 써야 하는가?

# n ==> OneTwoThreeFourFiveSixSevenEightNineTen 입력한다