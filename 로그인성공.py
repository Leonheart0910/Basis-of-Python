
from tkinter import *
import sys

Id = "lamfo007"
Ps = "sd0008"
cnt = 0

def show_entry_fields():
    global cnt
    myid = e1.get()
    mypa = e2.get()
    if myid == Id and mypa == Ps :
        print("들어올땐 마음대로지만 나갈때 아니란다.")
        return
    else :
        print("로그인에 실패하였습니다.")
        cnt += 1
    if cnt == 5:
        print("5회 로그인 실패시 로그인을 할 수 없습니다.")
        sys.exit(True)

master = Tk()
Label(master, text="welcome to gay bar",font = ("맑은고딕",20)).grid(row=0)
Label(master, text="login ID").grid(row=1)
Label(master, text="password").grid(row=2)

e1 = Entry(master)
e2 = Entry(master, show="*")
#e1.insert(10,"A. Miller")
#e2.insert(10, u"김달수")

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Button(master, text= '중지', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text= 'Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
