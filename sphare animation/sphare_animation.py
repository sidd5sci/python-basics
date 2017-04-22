from visual import *



p = sphere(pos = vector(-10,0,0),color=color.red)

dt = 0.005
t= 0
p.velocity = vector(10,0,0)
while t<10:
    rate(10)
    p.pos += p.velocity*dt
    print(p.pos," | ",t)
    t+=dt
