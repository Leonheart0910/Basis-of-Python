

from tkinter import *
root = Tk()

root.title(" 자유곡선 만들기")
cw = 500                                        # canvas width.
ch = 500                                        # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.pack()               # show canvas on a grid item


Q=[320, 300, 100, 60, 320, 60, 100, 250, 200, 320, 350, 200]


canvas_1.create_line(Q, smooth='true', dash=(7), width=2)

root.mainloop()
