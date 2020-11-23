x = {}
x["umtiti"]=5678
x["messi"]=678
print(x.keys())

def putdict(d,x):
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1

    #return --> 딕셔너리가 변하기 때문에 필요x

m = {} ; word2 = "messi"; word3 = "messi"
putdict(m, word2)
putdict(m, word3)
print(m)# m 은 딕셔너리에 담긴 횟수를 의미합니다.


