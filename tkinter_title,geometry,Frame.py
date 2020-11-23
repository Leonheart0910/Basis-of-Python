from tkinter import *

root = tkinter.Tk()
root.title("practice")
root.geometry("400x300+500+10")

root2 = Tk()
root2.geometry("600x100+600+200")
root2.title(123)

a = Frame(root, bg = "tan")
a.place(height=100, width=50, x=20, y=100)

b = Frame(root2, bg = "green")
b.place(height=20, width=100, x=100, y=30)

root.mainloop()