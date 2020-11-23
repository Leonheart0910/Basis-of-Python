

n=int(input())
F=int(n/5)
n%=5
T=0
while F>=0:
    if n%3==0:
        T=int(n/3)
        n=int(n%3)
        break
    F-=1
    n+=5
print((n==0) and (F+T) or -1)
#[백준 2839,파이썬] 설탕 배달



