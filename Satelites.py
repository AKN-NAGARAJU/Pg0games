import pgzrun
import random
import time
WIDTH=400
HEIGHT=400
startime=0
totaltime=0
current=0
total=8
salist=[]
co=[]
TITLE="Satelite Malfunction"
for i in range(total):
    s=Actor("sat")
    s.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
    salist.append(s) 
startime=time.time()
def draw():
    screen.blit("gal",(0,0))
    for s in salist:
        s.draw()
        screen.draw.text(str(salist.index(s)),(s.x+20,s.y))
    for c in co:
        screen.draw.line(c[0],c[1],"white")
    screen.draw.text(str(totaltime),(20,20))
    
def on_mouse_down(pos):
    global current,co
    if current<total:
        if salist[current].collidepoint(pos):
            if current!=0:
                cpos=salist[current].pos
                lpos=salist[current-1].pos
                co.append([cpos,lpos])
                print(co)
            current=current+1
        else:
            current=0
            co=[]

def update():
    global totaltime
    if current<total:
        totaltime=round(time.time()-startime)
    




    






pgzrun.go()