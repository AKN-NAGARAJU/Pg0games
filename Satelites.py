import pgzrun
import random
WIDTH=400
HEIGHT=400
current=0
total=8
salist=[]
co=[]
for i in range(total):
    s=Actor("sat")
    s.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
    salist.append(s)
def draw():
    screen.blit("gal",(0,0))
    for s in salist:
        s.draw()
        screen.draw.text(str(salist.index(s)),(s.x+20,s.y))
    for c in co:
        screen.draw.line(c[0],c[1],"white")
    
def on_mouse_down(pos):
    global current
    if current<total:
        if salist[current].collidepoint(pos):
            if current!=0:
                cpos=salist[current].pos
                lpos=salist[current-1].pos
                co.append([cpos,lpos])
                print(co)
            current=current+1





    






pgzrun.go()
        



    






