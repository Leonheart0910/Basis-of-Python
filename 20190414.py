a = int(input())
b = int(input())
c = int(input())

if b**b - 4*a*c > 0:
    print("실근")
elif b**b - 4*a*c == 0:
    print ("중근")
else :
    print("허근")
