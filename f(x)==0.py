def f(x):
    val = x**3 - 4*x**2 - 7*x - 1
    return( val)

xl = 5.29
xr = 5.39
while((xr - xl) > 0.000001):
    mid = (xl+xr)/2
    vmid = f(mid)
    print("f(mid)=", mid, f(mid))
    if vmid > 0:
        xr = mid
    else:
        xl = mid

