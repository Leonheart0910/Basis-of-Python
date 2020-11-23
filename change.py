infile = open("change.inp" , "r")
outfile = open("change.out" , "w")
rate = infile.readline()
rate = float(rate)
won = infile.readline()
won = float(won)

euro = float(won/rate)
if euro<100 :
    euro = euro - 1

H = int(euro // 100)
euro = int(euro - H*100)
F = int(euro//50)
euro = int(euro - F*50)
T = int(euro // 10)
euro = int(euro - T*10)
U = int(euro // 1)

print(H , file=outfile)

infile.close()
outfile.close()



