def change(a,b):

    temp = []

    temp = a
    a = b
    b = temp

    return (a , b)

a = [1,2,3]
b = [4,5,6]
print(change(a,b))