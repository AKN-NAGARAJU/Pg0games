import pgzrun
import random
WIDTH=400
HEIGHT=400
salist=[]
for i in range(8):
    s=Actor("sat")
    s.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
    salist.append(s)
def draw():
    screen.blit("gal",(0,0))
    for s in salist:
        s.draw()
        



    






pgzrun.go()