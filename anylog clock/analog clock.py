import random
import math
from Tkinter import *
import time

PI = 3.14159
root = Tk()
root.title("Analog Clock")
class vector:
    
    def __init__(self):
        
        self.direction = 0.0
        self.magnitude = 0.0
        
    def assign(self,drct,mag,angletype):

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
    def assign(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.z = Z



class needles:
    def __init__(self):
        self.v = vector()
        self.angle = -60.0
        self.tempx,self.tempy =0.0,0.0
        self.x,self.y,self.x1,self.y1 = 250,250,250,250
        self.mag = 200
    def draw(self,mag):
            self.initilise(mag)
            self.draw_clock()
            self.s_needle = canvas.create_line(self.x,self.y,self.x1,self.y1,fill="#fff")
            
            
    def move(self):
            self.angle += 5;
            
            
    def initilise(self,mag):
        self.mag = mag
        self.v.assign(self.angle,self.mag,"D")
        self.tempx = self.v.magnitude*math.cos(self.v.direction)
        self.tempy = self.v.magnitude*math.sin(self.v.direction)
        self.x1 = 250 + self.tempx
        self.y1 = 250 + self.tempy
    def update(self):
        canvas.delete(self.s_needle)
        self.draw(self.mag)
    def draw_clock(self):
       circle1 =canvas.create_oval(10,10,490,490,fill="#005588")
       circle2 =canvas.create_oval(50,50,450,450,fill="#000")
       circle3 =canvas.create_oval(240,240,260,260,fill="#552211")
       num1 = canvas.create_text(350,50,text="1")
       num2 = canvas.create_text(440,130,text="2")
       num3 = canvas.create_text(470,250,text="3")
       num4 = canvas.create_text(440,370,text="4")
       num5 = canvas.create_text(350,450,text="5")
       num6 = canvas.create_text(250,470,text="6")
       num7 = canvas.create_text(150,450,text="7")
       num8 = canvas.create_text(60,370,text="8")
       num9 = canvas.create_text(30,250,text="9")
       num10 = canvas.create_text(60,130,text="10")
       num11= canvas.create_text(150,50,text="11")
       num12 = canvas.create_text(250,30,text="12")
#====================================================================
#
#====================================================================
canvas = Canvas(root,width=500,height=500)
canvas.pack()


needle = needles()
needle_minut = needles()
while True:
    
    needle.draw(200)
    needle.move()
    needle.update()
    root.update()



root.mainloop()
