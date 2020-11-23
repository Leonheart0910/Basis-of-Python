# !/usr/bin/python3
from tkinter import * #---> tkinter에서 제공되는 모듈을 . 생략 가능하다
import tkinter

price = 0
title="A Crazy Summer-Night"

root = Tk() # tkinter.Tk() ---> 를 Tk() 만 표현함
root.title(title);

def soju() :
    global price
    price += 3000
    print("%d원" % price)

def beer() :
    global price
    price += 4000
    print("%d원" % price)

def men():
    global price
    price += 2500
    print("%d원" % price)

# relief = { RAISED, SUNKEN, RIDGE, GROOVE }
# command 는 이 작업을 수행합니다.
#bd 는 boundary ==> relief시 얼마나 튀어나와있는가 설정
w = tkinter.Button(text = '소주', bd=5, relief=GROOVE,  command=soju, bg="orange")#groove 파임
Q = tkinter.Button(text = '맥주', bd=5, relief=RAISED, fg="blue", command=beer)# raised 튀어나옴
T = Button(text = '라면', bd=5, relief=GROOVE, bg="tan", command=men)
soju1 = Label(root, text=": 3000원", fg="blue")
beer2 = Label(root, text=": 4000원", fg="black")
men3 = Label(root, text=": 2500원", fg="red")

w.place(x=30,y= 20) # x, y 좌표를 찍어줌
Q.place(x=30,y= 80)
T.place(x=30,y= 140)
soju1.place(x=90,y=20)
beer2.place(x=90,y=80)
men3.place(x=90,y=140)
#bg는 배경색 fg는 글자색

root.mainloop()
