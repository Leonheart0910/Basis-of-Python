def inonout(b,e,q):
    if q == b or q == e:
        return("on")
    if q < b or q > e :
        return("out")
    if b < q < e :
        return("in")

r = inonout(3,10,8)
print(r)