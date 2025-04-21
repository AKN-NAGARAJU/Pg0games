import pgzrun
WIDTH=1000
HEIGHT=550
score=0
direction=1
bullets=[]
galliga=Actor("galliga")
galliga.pos=(WIDTH/2,HEIGHT-100)
nemesis_group=[]
gameover=False
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
    screen.draw.text(str(score),(0,0))
    galliga.draw()
     
    if gameover==True:
        screen.draw.text("GAME OVER",(0,200  ))     

    else:
        for row in nemesis_group:
            for nemesis in row:
                nemesis.draw()
        for b in bullets:
            b.draw() 

def update(): 
    #pass # because we didnt have anything to put we put that.
    global score,direction,gameover
#check for enemys
    enemies=False
    for row in nemesis_group:
        if len(row)>=0:
            enemies=True
    if enemies==False:
        gameover=True
    


    if keyboard.left and galliga.x>=0:
        galliga.x=galliga.x-2
    elif keyboard.right and galliga.x<=WIDTH:
        galliga.x=galliga.x+2
    #this is the code to help us move the bullet up_shoot
    for b in bullets:
        if b.y>0:
            b.y=b.y-10
        else:
            bullets.remove(b)
    
    #moving the nemesis left,right,up,down
    movedown=False
    if enemies==True:
        if nemesis_group[0][-1].x>=WIDTH or nemesis_group[0][0].x<=0:
            direction=direction*-1
            movedown=True
    for row in nemesis_group:
        for n in row:  
            n.x=n.x+2*direction  
            if movedown:
                n.y=n.y+68
    
    #collision of bullet and enemy
    for row in nemesis_group:
        for n in row:
            for b in bullets:
                if n.colliderect(b):
                    row.remove(n)
                    bullets.remove(b)
                    score=score+1
    #collision of galliga and enemy
    for row in nemesis_group:
        for n in row:
            if galliga.colliderect(n):
                gameover=True
    
            

def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.pos=galliga.pos
        bullets.append(bullet)






pgzrun.go()
