from Tkinter import *

root = Tk()




root.title("Path finder")
xv = 0.009
yv = 0.009
def key(event):
    if event.char == "w":
        canvas.move(ball,0,-100)
    elif event.char == "s":
        canvas.move(ball,0,100)

def mouse(event):
    global bullet
    global coord0
    global coord1
    coord0 = canvas.coords(mainchar)[0]
    coord1 = canvas.coords(mainchar)[1]
    canvas.coords(bullet,coord0,coord1,coord0+50,coord1+50)
    
canvas = Canvas(root,width=500,height=400)   
canvas.bind("<Key>",key)
canvas.bind("<Button-1>",mouse)
canvas.focus_set()
canvas.pack()
#canvas.create_line(0,0,500,400)


ball = canvas.create_oval(40,40,60,60,fill="red")

while True:
     canvas.move(ball,xv,yv)
     root.update()
     pos = canvas.coords(ball)
     if pos[3] >= 400 or pos[1] <= 0:#bottom,top
          yv = -yv
     if pos[2] >= 500 or pos[0] <= 0:#right,left
          xv = -xv
root.mainloop()
