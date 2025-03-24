import pgzrun
WIDTH=1000
HEIGHT=550

galliga=Actor("galliga")
galliga.pos=(WIDTH/2,HEIGHT-100)
nemesis_group=[]
x=30
y=30
for i in range(3): 
    row=[] 
    for i in range(7):
        nemesis=Actor("nemesis")
        nemesis.pos=(x,y)
        row.append(nemesis)
        x=x+80
    nemesis_group.append(row)
    x=30
    y=y+60
print(nemesis_group)

def draw():
    screen.fill("midnightblue")
    galliga.draw()
    for row in nemesis_group:
        for nemesis in row:
            nemesis.draw()
            


def update():
    pass




pgzrun.go()