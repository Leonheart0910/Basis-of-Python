infile = open("price.txt" , "r")
outfile = open("total.txt" , "w")

a = infile.readline()
a = float(a)

if a>0:

    print(a)



a = infile.readline()
a = float(a)

if a>0:

    print(a)






infile.close()
outfile.close()
