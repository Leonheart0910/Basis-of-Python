
# 이 프로그램은 수강생이 작접 작성한 프로그램입니다.

from tkinter import *
import math

root = Tk()

width = 360
height = 300

vcenter = height/2
hcenter = width/2

y_amplitude = 70 #원의 반지름을 의미함


canvas = Canvas(root, width=width, height=height, bg='light blue')
canvas.pack(side='left')

p=vcenter
q=vcenter

for t in range(1500):
    y_amplitude -= 0.03
    x = 2*math.cos((2*math.pi*t)/180)*y_amplitude + vcenter+30
    y = 2*math.sin((2*math.pi*t)/180)*y_amplitude + vcenter
    sinLine = canvas.create_line(x, y, p, q, fill='red')
    p = x
    q = y


canvas.create_line(hcenter, 0, hcenter, height)
canvas.create_line(0, vcenter, width, vcenter)

root.mainloop()