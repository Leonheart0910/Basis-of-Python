from tkinter import *

#tkinter 의 명령어는 대부분 대문자인 것을 유의

root = Tk()
root.title("연습용")
root.configure(bg = "darkcyan") #tk창의 전체 바탕이 이 색으로 칠해진다.

labela = Label(root, text="nameA", fg="white", bg="black")
entrya = Entry(root)
labelb = Label(root, text="  age  ", fg="blue", bg="khaki")
entryb = Entry(root)
labela.grid(row=100, column=100)
entrya.grid(row=100,column=200)
labelb.grid(row=200,column=100)
entryb.grid(row=200,column=200)

root.mainloop()