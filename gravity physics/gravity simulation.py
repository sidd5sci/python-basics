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

# mass of triangle
mass = 50# kg
GForce = mass*g
vy = g*(ctime+1)

v = vertex()
v.asign(300,200,0)
velox,veloy,result = vector(),vector(),vector()
velox.asign(0,15.10,"D")
veloy.asign(90,100,"D")# rotation is anticlock wise
tempx = v.x
tempy = v.y

for i in range(0,100):
        
    drawEquiTriangle("blue",v,10,10)
    mag = math.sqrt((velox.magnitude*velox.magnitude)+(veloy.magnitude*veloy.magnitude))
    theta = math.atan(veloy.magnitude/velox.magnitude)*(180/PI)
    # convert to environent angles
    if velox.magnitude < 0 and veloy.magnitude >0:
        theta = -theta +90
    if velox.magnitude < 0 and veloy.magnitude <0:
        theta = theta +180
    if velox.magnitude > 0 and veloy.magnitude <0:
        theta = 360+theta
    
    result.asign(-theta,mag,"D")
    root.update()
    vy = vy+ g*ctime
    veloy.asign(90,-vy,"D")
    print (result.magnitude," | ",result.getDirection())
    v.x += math.cos(result.direction)*result.magnitude
    v.y += math.sin(result.direction)*result.magnitude
    canvas.delete(ALL)
    time.sleep(0.7)
    ctime+=0.1
    


root.mainloop()
