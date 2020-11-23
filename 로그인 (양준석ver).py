from tkinter import *
import sys

count = 0

def get_text():
    global count
    global master
    myid = e1.get()
    myps = e2.get()

    if len(myps) < 10 :
        print("10자리 이하의 password는 불가합니다.")
    elif myps == "12345678910":
        print("Login ID: %s  \nPassword : %s"  % ( myid, myps ))
    else:
        Label(master, text= "wrong passwd left : " + str(5 - count)).grid(row=500, column=200)
        count += 1

    if count == 6:
        Label(master, text= "Quit process left : " + str(5 - count)).grid(row=500, column=200)
        sys.exit(0)
        master.quit()

    e1.delete(0,END)
    e2.delete(0,END)

master = Tk()

Label(master, text= "소환사의 협곡", font=("맑은 고딕", 20)).grid(row=00, column=200)

Label(master, text= "Login : ").grid(row=100, column=100)
Label(master, text= "Passward : ").grid(row=200, column=100)

e1 = Entry(master)
e1.focus_set()            # 입력 커서를 이쪽으로  이것이 없으면 커서는 아무데나
e1.insert(10, "ID")
e1.grid(row=100, column=200)
e2 = Entry(master, show="*")
e2.focus_set()            # 입력 커서를 이쪽으로  이것이 없으면 커서는 아무데나
e2.insert(10, "passwd")
e2.grid(row=200, column=200)

Button(master, text= '중지', command=master.quit).grid(row=300, column=100, sticky=W, pady=4)
Button(master, text= 'Show', command=get_text, bg='orange',  fg="blue").grid(row=300, column=200, sticky=W, pady=4)

mainloop( )
