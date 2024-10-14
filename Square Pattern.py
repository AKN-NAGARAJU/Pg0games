import pgzrun
import random
WIDTH=400
HEIGHT=400



def draw():
    screen.fill("black")
    side=10
    for i in range(40):
        sq1=Rect(200,200,side,side)
        sq1.center=(200,200)
        screen.draw.rect(sq1,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        side+=10




pgzrun.go()