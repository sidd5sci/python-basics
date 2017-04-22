import random
import math
from Tkinter import *
import time

PI = 3.14159

class vector:
    
    def __init__(self):
        
        self.direction = 0.0
        self.magnitude = 0.0
        
    def copyVector(self,drct,mag,angletype):

        if(angletype == 'R'):
            self.direction = drct
        elif(angletype == 'D'):
            self.direction = (PI/180)*drct
        self.magnitude = mag
        
    def getDirection(self):
        return self.direction
    
    def getMagnitude(self):
        return self.magnitude

   
class vertex:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        positionVector = vector()
    def addVertex(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.z = Z


dna =[]
pos = vertex()
pos.addVertex(100,250,0)
x = 0.0
y = 0.0
root = Tk()
root.title("Trapped Fly!")
canvas = Canvas(root,width= 500,height=500)
canvas.pack()
mag =50.0
tempx = pos.x
tempy = pos.y
color = "red"
#for i in range(0,100):

        
for i in range(0,1000):
        v = vector()
        v.copyVector(random.uniform(0,360),mag,"D")
        time.sleep(0.1)
        #dna.append(v)
        x = tempx
        y = tempy
        tempx += v.magnitude*math.cos(v.direction)
        tempy += v.magnitude*math.sin(v.direction)
        
        if tempx < 10 or tempx > 490 or tempy < 10 or tempy >490 :
            print("Collision :",tempx," | " ,tempy)
            color = "blue"
            tempx = x
            tempy = y
            
        else:
            canvas.delete(ALL)
            pos.x += v.magnitude*math.cos(v.direction)
            pos.y += v.magnitude*math.sin(v.direction)
            tempx = pos.x
            tempy = pos.y
            arrow = canvas.create_line(x,y,pos.x,pos.y,fill=color)
            arrow = canvas.create_oval(pos.x-3,pos.y-3,pos.x+3,pos.y+3,fill=color)
            color = "red"
            root.update()

root.mainloop()
