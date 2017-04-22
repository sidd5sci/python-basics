import math
import time
import random

PI = 3.14159
#======================================
class vector:
    
    def __init__(self):
        
        self.directionX = 0.0
        self.directiinY = 0.0
        self.directionZ = 0.0
        self.magnitude = 0.0
        
    
    def copyVector(self,angleX,angleY,angleZ,mag,angletype):

        if(angletype == 'R'):
            self.directionX = angleX
            self.directionY = angleY
            self.directionZ = angleZ
        elif(angletype == 'D'):
            self.directionX = (PI/180)* angleX
            self.directionY = (PI/180)* angleY
            self.directionZ = (PI/180)* angleZ
        self.magnitude = mag
        
        
        
    def getDirectionX(self):
        return self.directionX
    def getDirectionY(self):
        return self.directionY
    def getDirectionZ(self):
        return self.directionZ
    
    def getMagnitude(self):
        return self.magnitude

#================================   
class vertex:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.positionVector = vector()
        self.positionVector = copyVector(60,60,60,0,"D")
    def addVertex(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.z = Z

        mag = math.sqrt((X*X)+(Y*Y)+(Z*Z))
    
        vx = X/mag
        vy = Y/mag
        vz = Z/mag
        
        angleX = math.acos(vx)
        angleY = math.acos(vy)
        angleZ = math.acos(vz)
        self.positionVector.copyVector(angleX,angleY,angleZ,mag,"D")
#==============================
def drawVector_3D(vertex):
    