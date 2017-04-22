import random
import math
from Tkinter import *
import time

PI = 3.14159
g = 9.87 #m/s2
ctime = 0.0
class vector:
    
    def __init__(self):
        
        self.direction = 0.0
        self.magnitude = 0.0
        
    def asign(self,drct,mag,angletype):

        if(angletype == 'R'):
            self.direction = -drct
        elif(angletype == 'D'):
            self.direction = -(PI/180)*drct
        self.magnitude = mag
        
    def getDirection(self):
        return -self.direction*(180/PI)
    
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
    def random(self,irange,frange):
        self.x = random.uniform(irange,frange)
        self.y = random.uniform(irange,frange)
        self.z = random.uniform(irange,frange)
class edge :
    def __init__(self):
        self.initVertex = vertex()
        self.finalVertex = vertex()
    def asignVertex(self,vi= vertex(),vf= vertex()):
        self.initVertex = vi
        self.finalVertex = vf
    def asignVertex(self,xi,yi,zi,xf,yf,zf):
        self.initVertex.x = xi
        self.initVertex.y = yi
        self.initVertex.z = zi
        self.finalVertex.x = xf
        self.finalVertex.y = yf
        self.finalVertex.z = zf

WIDTH =900
HEIGHT = 400

root = Tk()
root.title("Trapped Fly!")
canvas = Canvas(root,width= WIDTH,height=HEIGHT)
canvas.pack()

#for i in range(0,100):



def drawEquiTriangle(color, polygonCentre,z_axisRotation,mag):
    v1,v2,v3 = vector(),vector(),vector()

    v1.asign(90+z_axisRotation,mag,"D")
    v2.asign(90+120+z_axisRotation,mag,"D")
    v3.asign(90+240+z_axisRotation,mag,"D")

    ver1,ver2 = vertex(),vertex()

    ver1.x = polygonCentre.x + math.cos(v1.direction)*v1.magnitude
    ver1.y = polygonCentre.y + math.sin(v1.direction)*v1.magnitude

    ver2.x = polygonCentre.x + math.cos(v2.direction)*v2.magnitude
    ver2.y = polygonCentre.y + math.sin(v2.direction)*v2.magnitude

    poly = canvas.create_line(ver1.x,ver1.y,ver2.x,ver2.y,fill = color);
    
    ver1.x = polygonCentre.x + math.cos(v3.direction)*v3.magnitude
    ver1.y = polygonCentre.y + math.sin(v3.direction)*v3.magnitude

    poly = canvas.create_line(ver2.x,ver2.y,ver1.x,ver1.y,fill = color);
    
    ver2.x = polygonCentre.x + math.cos(v1.direction)*v1.magnitude
    ver2.y = polygonCentre.y + math.sin(v1.direction)*v1.magnitude
    
    poly = canvas.create_line(ver2.x,ver2.y,ver1.x,ver1.y,fill = color);

# mass of projectile
mass = 50.0# kg
v = vertex()
v.asign(300,200,0)
velox,veloy,velo,result = vector(),vector(),vector(),vector()
color ="red"
def inputs():
    global v,velo,mass,ctime
    posx = float(input("Enter the x position of projectile:"))
    posy = float(input("Enter the x position of projectile:"))
    v.x = posx
    v.y = posy
    mass = float(input("Enter the mass of projectile:"))
    velo.magnitude = float(input("Enter the magnitude of initial velocity of projectile:"))
    velo.direction = -float(input("Enter the direction of initial velocity of projectile (angle in degree)"))*(PI/180)
    print (velo.getDirection())
    #color = input("Enter the color of projectile:")
    ctime = 0.01
def drawEnvt():
    ground = canvas.create_rectangle(v.x-30,v.y+30,v.x+30,v.y+60,fill="green")
    
def projectile():
    global color,v,mass,g,velo,velox,veloy,ctime
    for i in range(0,200):
        projectile = canvas.create_oval(v.x-30,v.y-30,v.x+30,v.y+30,fill=color)
        vx = velo.magnitude*math.cos(velo.direction)
        vy = velo.magnitude*math.sin(velo.direction) -g*ctime
        print velo.direction
        v.x += vx
        v.y += vy
        velo.magnitude = math.sqrt(vx*vx + vy*vy)
        velo.direction = -(vy/vx)
        root.update()
        
    
    
inputs()
drawEnvt()
projectile()

root.mainloop()
