def acro_1(w):

    n = len(w)

    if n <=3 :
        return(w)

    mid = int(len(w)/2)
    a = w[0]+w[mid]+w[-1]
    return(a)
#-----end of acro_1()------

def acro_2(L):# L=[a,b]
    first = L[0]
    second = L[1]
    if len(second)==1 :
        second = second*2
    z = first[0]+second[0]+second[-1]
    return(z)
#-----end of acro_2()------

Q = input("type korean phrase:")
LQ = Q.split()
if len(LQ) == 1 :
    w = acro_1(LQ[0])
if len(LQ) == 2 :
    r = acro_2(LQ)

r = acro_1(w)
print(r)

f = acro_2(r)
print(f)
