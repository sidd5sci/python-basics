import random
import math
from Tkinter import *
import time

PI = 3.14159

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
        return self.direction*(180/PI)
    
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
def polygonGenrator1(color="blue",polyRange=5):
    global HEIGHT,WIDTH
    polyType = int(random.uniform(3,polyRange))
    polygonVertex = list()

    for i in range(0,polyType):
        v = vertex()
        v.x = random.uniform(50,(WIDTH/2)-100)
        v.y = random.uniform((HEIGHT/2),(HEIGHT/2)+100)

        polygonVertex.append(v)

    for i in range(0,polyType):
        
        if i+1 < polyType:
            poly = canvas.create_line(polygonVertex[i].x,polygonVertex[i].y,polygonVertex[i+1].x,polygonVertex[i+1].y,fill = color);
    poly = canvas.create_line(polygonVertex[i].x,polygonVertex[i].y,polygonVertex[0].x,polygonVertex[0].y,fill = color);

def polygonGEnrator2(color="blue",polyType = 3,polygonCentre= vertex()):

    v = vector()
    v.asign(-(random.unifor(0,360)),random.uniform(10,50),"D")
    angle = 0.0
    for i in range(0,polyTYpe):
        temp = vertex()
        temp.x = polygonCentre.x + math.cos(v.direction)*v.magnitude
        temp.y = polygonCentre.y + math.sin(v.direction)*v.magnitude
        polygonVertex.append(temp)
        
        angle = random.uniform(0,360)
        if angle-v.getDirection() < 30 :
            angle = random.uniform(0,360)




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
    
v = vertex()
v.asign(300,200,0)
drawEquiTriangle("blue",v,0,100)



#polygonGenrator1()
root.mainloop()
