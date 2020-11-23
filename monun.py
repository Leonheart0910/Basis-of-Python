from tkinter import *
root = Tk()
root.title("Monun.py")

N = int(input())
M = int(input())

def monun(N,M):

    MM = 20*M ; NN = 20*N
    mon = Canvas(root, width= NN, height= MM, background="white")

    for i in range(N + 1):
        mon.create_line( 20 * i,0 , 20*i , NN, width=3, fill='black')
    for i in range(M + 1):
        mon.create_line( 0,20 * i ,MM, 20*i, width=3, fill='black')


    mon.place(x=0,y=0)

monun(N,M)

root.mainloop()