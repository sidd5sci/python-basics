from Tkinter import *
import time
import random


root = Tk()

#Initilisation o modes
WIDTH = 800
HEIGHT = 600

color = ["red","green","blue","yello" ]
vx = 0.05
vy = 0.05
snake = []
fruitEat = False
fruitx = random.uniform(0,WIDTH)
fruity = random.uniform(0,HEIGHT)
fruitcolor = "red"
def key(event):
    if event.char == "w":
        canvas.move(head,0,-vy)
    if event.char == "s":
        canvas.move(head,0,vy)
    if event.char == "a":
        canvas.move(head,-vx,0)
    if event.char == "d":
        canvas.move(head,vx,0)



canvas = Canvas(root ,width=WIDTH,height=HEIGHT)
canvas.bind("<Key>",key)
canvas.focus_set()
canvas.pack()

head = canvas.create_rectangle(10,10,20,20,fill="green")
fruit = canvas.create_oval(40,40,60,60,fill=fruitcolor)
while True:
    canvas.move(head,vx,vy)
    root.update()
    pos = canvas.coords(head)
    fpos = canvas.coords(fruit)
    for i in range(0,snake.length)
    
    if pos[3] > HEIGHT or pos[1] < 0 or pos[2] > WIDTH or pos[0] < 0:
       vx = vy =0 #gameOver
    if pos[3] == fpos[]and pos[2] == fpos[]and pos[1] == fpos[] and pos[0]== fpos[]
root.mainloop()
