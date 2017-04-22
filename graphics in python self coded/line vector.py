import vector
from tkinter import *
import math

root = Tk()

root.title("Line vector")

canvas = Canvas(root,width=500,height=400,background="gray")
width = 500
height =400

x = width/2
y = height/2

v1 = vector()
v1.copyVector(30,30,'D')

x1 = x+(v1.getMagnitude()*math.cos(v1.getDirection()))
y1 = y+(v1.getMagnitude()*math.sin(v1.getDirection()))
canvas.pack()

canvas.create_line(x,y,x1,y1)

canvas.delete(ALL)
root.mainloop()
