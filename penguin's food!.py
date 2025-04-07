import pgzrun
import random

WIDTH=400
HEIGHT=400
Title="PENGUIN NEEDS ITS FOOD"
a=Actor("penguin")
b=Actor("pizza")
a.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
b.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
msg="HELP LITTLE PENGUIN JERRIMIMA EAT ITS FOOD!!!"
def draw():
    screen.fill("blue")
    a.draw()
    b.draw()
    screen.draw.text(msg,(20,20),fontsize=20,color="white")

def on_mouse_down(pos): 
    global msg
    print (pos)
    if b.collidepoint(pos): # this is used to show that when the mouse collides or touches b(pizza) its position will be randomized
        b.pos=(random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40))
        msg="HURRAY!GET MOREEEE FOOOOD, KEEP IT UPPP!!"

    else:
        msg="AHHHHHH, I WILL DIEEEEEE, I WILL SUEEEE UUUU!!"

pgzrun.go()



