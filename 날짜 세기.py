def day(p):               #역슬레쉬는 줄 바꾸어줌
    t = [ " sun","mon","thu","wed"\
    "tue","fri","sat"]
    m = [31,28,31,30,31,30,31,30,31,30,31,30]
    month = p[0]
    day = p[1]

m = [31,28,31,30,31,30,30,31,30,31,31,31]

s = 0
total = []

for i,w in enumerate(m):
    total.append(s)
    s += w
    print(i+1, w, s)
print(total)

def count(dal, nal):
    return(total[dal - 1]+nal)#dal에 -1 이유는 1월부터 시작하기 때문

print(count(12,31))