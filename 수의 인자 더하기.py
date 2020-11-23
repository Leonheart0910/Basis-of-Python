def digit(n):
    if n < 10:
        return n
    else:
        n,rest = n//10, n%10
    return rest + digit(n)

print(digit(1000010101))


