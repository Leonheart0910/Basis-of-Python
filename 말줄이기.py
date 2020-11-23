def acro_1(w):
    n = len(w)
    if n <= 3 : return(w)
    mid = int(n/2)
    a = w[0]+w[mid]+w[-1]
    return(a)

print(acro_1("우리나라 만세 요"))

#-----------end of acro_1( ) ---------------

def acro_2(L): #L=[a,b]
    first=L[0]
    secound=L[1]
    if len(secound) == 1:
        secound = secound*2
    a = first[0] , secound[0], secound[-1]
    return(a)

print(acro_2("어디로 가야 하오"))

#----------end of acro_2( )---------------

def acro_3(L): #L=[a,b]
    first=L[0]
    secound=L[1]
    third=L[2]
    a= first[0] + secound[0] + third[0]
    return(a)

#----------end of acro_3( )---------------

def acro_4(L): #L=[a,b]
    first=L[0]
    secound=L[1]
    third=L[2]
    forth=L[-1]
    a= first[0] + secound[0] + third[0] + forth[-1]
    return(a)

#----------end of acro_4( )---------------

q = input("type korean phrase:")
lq=q.split()
if len(lq) == 1 :
    w = acro_1(lq[0])
if len(lq) == 2 :
    w = acro_2(lq)
if len(lq) == 3 :
    w = acro_3(lq)
if len(lq) >= 4 :
    w = acro_4(lq)

print(w)

n = input("type english phrase:")
lq=n.split()
if len(lq) == 1 :
    w = acro_1(lq[0].capitalize())
if len(lq) == 2 :
    w = acro_2(lq.capitalize())
if len(lq) == 3 :
    w = acro_3(lq.capitalize())
if len(lq) >= 4 :
    w = acro_4(lq.capitalize())

print(w)
