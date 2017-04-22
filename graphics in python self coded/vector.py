import random
import math
from tkinter import *
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

array = []
for i in range(0,10)
    v = vector()
    v.copyVector(random.random(),10,"R")
    time.sleep(0.1)
    array.append(v)



root = Tk()
canvas = Canvas(root,width=500,height=500)



root.mainloop()

