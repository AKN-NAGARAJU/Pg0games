import pgzrun
import random

WIDTH=400
HEIGHT=400
b=Actor("bee.coding")
f=Actor("flowerwithbee.coding")
#b.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
f.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))       
def draw():
    screen.blit("bcgrnd.coding1",(0,0))
    b.draw()
    f.draw()

#def on_key_down(key):
    #if key==keys.RIGHT:
       # b.x=b.x+5
    #this is a one click key movement. The next one is a hold down movement making it more leisure for customers.

def update():
    if keyboard.right:
        b.x=b.x+2
                                                       #using two ifs create the bee to go diagonally smoothly
                                                       ####check the code for a better understanding
                                                       ########it is really good
    elif keyboard.left:
        b.x=b.x-2
    
    if keyboard.down:
        b.y=b.y+2
    
    elif keyboard.up:
        b.y=b.y-2

    if b.colliderect(f):
        f.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))








pgzrun.go()