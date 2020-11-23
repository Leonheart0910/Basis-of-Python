from tkinter import *

root = Tk()
root.geometry("300x300+100+100")

frame = Frame(root)
frame.pack(side = BOTTOM)

labela = Label(frame, text="yadong", fg="red").pack(padx= 10, pady= 20)
labelb = Label(frame, text="sex", fg="pink")
labelb.pack(side=RIGHT)

root.mainloop()