from tkinter import *
root = Tk()
root.title("Bill")

price = 0; mj = 0; sj = 0; sd = 0
menu = ""

frame = Frame(root)
frame.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=RIGHT)

def maxju():
    global price, mj, sj, sd
    mj += 1
    price += 4000
    print("%d 원" % price)
    print("맥주 %d 개" % mj, "소주 %d" % sj, "사이다 %d" % sd)

def soju():
    global price, mj, sj, sd
    sj += 1
    price += 3000
    print("%d 원" % price)
    print("맥주 %d 개" % mj, "소주 %d" % sj, "사이다 %d" % sd)

def soda():
    global price, mj, sj, sd
    sd += 1
    price += 2000
    print("%d 원" % price)
    print("맥주 %d 개" % mj, "소주 %d" % sj, "사이다 %d" % sd)

maxjubutton = Button(frame, text= "맥   주", command= maxju, fg= "white", bg= "orange")
sojubutton = Button(frame, text= "소   주", command= soju, fg= "white", bg= "green")
sodabutton = Button(frame, text= "사이다", command= soda, fg= "white", bg= "lightgreen")

maxjubutton.pack(side=TOP, pady= 5)
sojubutton.pack(side=TOP, pady= 5)
sodabutton.pack(side=TOP, pady= 5)

maxjul = Label(frame2, text= ": 4000원", bg = "white").pack(side=TOP, padx= 10, pady= 10)
sojul = Label(frame2, text= ": 3000원", bg = "white").pack(side=TOP, padx= 10, pady= 10)
sodal = Label(frame2, text= ": 2000원", bg = "white").pack(side=TOP, padx= 10, pady= 10)

root.mainloop()