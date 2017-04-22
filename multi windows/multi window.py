from visual import *

dt = 0.1

windows = []

for i in range(3):
    windows.append(display(x = 0,y = 30 + 250*i,width = 600, height = 220))

windows[0].title = "start"
windows[1].title = "start"
windows[2].title = "start"


bands = [ curve( x = arange(-50,50), display=windows[0], color=color.red, k = 6., mass = 2.0),
          curve( x = arange(-50,50), display=windows[1], color=color.yellow, k = 6., mass = 1.0),
          curve( x = arange(-50,50), display=windows[2], color=color.green, k = 6., mass = 0.5),
        ]
