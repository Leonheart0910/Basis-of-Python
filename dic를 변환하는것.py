saturi = {"개쉬운":"연습용"}
saturi["빡대갈"] = "바보"
saturi["컴시입"]="컴퓨터 시스템 입문"
ls = list(saturi)

t = """ 이것은 개쉬운  컴시입
우리가 빡대갈 ...
"""
s=" "
lt = t.split()
for w in lt:
    if w in saturi.keys():
        print(saturi[w])
    else:
        print(w)
