import random
import math
from Tkinter import *
import time

PI = 3.14159
HEIGHT , WIDTH = 500,900
class vector:
    
    def __init__(self):
        
        self.direction = 0.0
        self.magnitude = 0.0
        
    def asign(self,drct,mag,angletype):

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
    def asign(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.z = Z




x = 0.0
y = 0.0

terrain = list()
start,end = -1,-1
def terrainGenrator(color,mag,startPos):
    global HEIGHT,WIDTH
    
    tempx = startPos.x
    tempy = startPos.y

    for i in range(0,1000):
        v = vector()
        angle = random.uniform(0,360)
        if( (angle > 0 and angle < 60) or (angle < 360 and angle > 290)):
            v.asign(angle,mag,"D")
            
        x = tempx
        y = tempy
        tempx += v.magnitude*math.cos(v.direction)
        tempy += v.magnitude*math.sin(v.direction)
            
        if tempx < 0 or tempx > WIDTH or tempy < 0 or tempy > HEIGHT :
                print("Collision :",tempx," | " ,tempy)
                color = "blue"
                tempx = x
                tempy = y
                
        else:
                
                terrain.append(v)
                
                
                                
def displayTerrian(color,mag,startPos):
    v  = vector()
    
    for i in range(0,len(terrain)):
        v = terrain.pop()
        tempx = startPos.x
        tempy = startPos.y
        startPos.x += v.magnitude*math.cos(v.direction)
        startPos.y += v.magnitude*math.sin(v.direction)
        
        arrow = canvas.create_line(tempx,tempy,startPos.x,startPos.y,fill=color)
        arrow = canvas.create_oval(startPos.x-3,startPos.y-3,startPos.x+3,startPos.y+3,fill=color)
        color = "#227f00"
def terrainGenrator1(mag):
    global HEIGHT,WIDTH,terrain
    flag = 0
    
    while(flag == 0):
        v = vector()
        angle = random.uniform(0,360)
        if( (angle > 0 and angle < 60) or (angle < 360 and angle > 290)):
            v.asign(angle,mag,"D")
            terrain.append(v)
            flag = 1
        
            
            
                   
           

def displayTerrian1(color,mag,startPos,endPos):
    v  = vector()
    global terrain
    
    for i in range(0,len(terrain)):
        v = terrain[i]
        tempx = startPos.x
        tempy = startPos.y
        startPos.x += v.magnitude*math.cos(v.direction)
        startPos.y += v.magnitude*math.sin(v.direction)
        if startPos.x > endPos.x:
            for j in range(0,len(terrain)-1):
                terrain[j] = terrain[j+1]
            break
            #print ("Removing first vector")
        else:
            arrow = canvas.create_line(tempx,tempy,startPos.x,startPos.y,fill=color)
            arrow = canvas.create_oval(startPos.x-3,startPos.y-3,startPos.x+3,startPos.y+3,fill=color)
            color = "#227f00"
            time.sleep(0.001)


root = Tk()
root.title("Terrain Genrator!")
canvas = Canvas(root,width= WIDTH,height=HEIGHT)
canvas.pack()


spos,epos = vertex(),vertex()

epos.asign(800,250,0)
for i in range(0,2000):
    spos.asign(100,250,0)
    canvas.delete(ALL)
    terrainGenrator1(10)
    displayTerrian1("green",10,spos,epos)
    root.update()


    
root.mainloop()
