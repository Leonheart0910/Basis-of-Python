def z(a,b):
    a += b
    print("in z() , " , x, y)

x, y = 20, 30
z(x,y)
print("in main(), " , x, y)
