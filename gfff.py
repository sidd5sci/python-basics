from tkinter import*
import random
import time
root = Tk()
moot = Tk()
global x
x = 0
global y
y = - 100
def negative():
    global y
    root.after(1000,negative)
    y = -y
root.after(1000,negative)
def mouse(event):
    global bullet
    global coord0
    global coord1
    coord0 = canvas.coords(mainchar)[0]
    coord1 = canvas.coords(mainchar)[1]
    canvas.coords(bullet,coord0,coord1,coord0+50,coord1+50)  
def key(event):
    if event.char == "w":
        canvas.move(mainchar,0,-100)
    elif event.char == "s":
        canvas.move(mainchar,0,100)
canvas = Canvas(root,width=999,height=999)
canvas.bind("<Key>",key)
canvas.bind("<Button-1>",mouse)
canvas.focus_set()
canvas.pack()
mainchar = canvas.create_rectangle(500,400,600,500,fill="blue",outline="red")
global bullet
bullet = canvas.create_oval(0,0,0,0,fill="green")
bullet1 = canvas.create_oval(0,50,0,0,fill="green")
badguy = canvas.create_rectangle(700,600,800,700,fill="red",outline="blue")
canvas.move(mainchar,-400,0)
def movebullet():
    root.after(1,movebullet)
    canvas.move(bullet,1,0)
    coord0 = canvas.coords(bullet)[0]
    coord1 = canvas.coords(bullet)[1]
    coord2 = canvas.coords(bullet)[2]
    coord3 = canvas.coords(bullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3)== (2,4) or canvas.find_overlapping(coord0,coord1,coord2,coord3)== (2,3,4):
        root.destroy()
        label= Label(moot,text='You have won!',font=("none",50))
        label.pack()        
movebullet()
def movebullet11():
    root.after(1,movebullet11)
    canvas.move(bullet1,-2,0)
    coord0 = canvas.coords(bullet1)[0]
    coord1 = canvas.coords(bullet1)[1]
    coord2 = canvas.coords(bullet1)[2]
    coord3 = canvas.coords(bullet1)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) ==(1,3) or canvas.find_overlapping(coord0,coord1,coord2,coord3)== (1,2,3):
        root.destroy()
        label= Label(moot,text='You have lost!',font=("none",50))
        label.pack()
movebullet11()    
def movebullet1():
    coord0 = canvas.coords(badguy)[0]
    coord1 = canvas.coords(badguy)[1]
    canvas.coords(bullet1,coord0,coord1,coord0+50,coord1+50)
    root.after(700,movebullet1)
movebullet1()    
root.geometry('1000x1000')
def movebadguy():
    canvas.move(badguy,0,y)
for i in range(0,50):
    x = x + 200
    root.after(x,movebadguy)
root.mainloop()
