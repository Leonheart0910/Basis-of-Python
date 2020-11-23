from tkinter import *

root = Tk()
root.geometry("500x500+100+100")

cnt = 0

def gay():
    global cnt
    print(cnt)
    cnt += 1

gay()

frame = Frame(root)
frame.pack()

a = Button(frame, relief=RAISED,  text="ang", fg="red", command= gay)
a.pack(side = LEFT)
#command = "함수이름" 이면 함수의 코드를 이행한다ㅊ

root.mainloop()