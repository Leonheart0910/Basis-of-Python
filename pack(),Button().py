from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

buttona = Button(frame, text="sony", fg="red", bg="black")
buttona.pack( side = LEFT)

buttonb = Button(frame, text="kane",fg="blue",bg="black")
buttonb.pack(side = LEFT)

buttonc = Button(frame, text="yangmina", fg="aqua", bg="black")
buttonc.pack(side = LEFT)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

buttond = Button(bottomframe, text="yorente", fg="pink", bg="black")
buttond.pack()
root.mainloop()