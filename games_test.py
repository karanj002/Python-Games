import turtle
import random
import time

#screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#register images
turtle.register_shape("player_right.gif")
turtle.register_shape("enemy_left.gif")

#border
mypen=turtle.Turtle()
mypen.penup()
mypen.color('yellow')
mypen.setposition(-365,-265)
mypen.pendown()
mypen.left(90)
mypen.forward(550)
mypen.setposition(-365,-265)
mypen.right(90)
for p in range (3):
    mypen.pendown()
    mypen.forward(750)
    mypen.left(90)
    mypen.penup()
    mypen.forward(550)
    mypen.left(90)
mypen.hideturtle()

#player
player=turtle.Turtle()
player.shape('player_right.gif')
player.penup()
player.color('white')
player.setposition(-355,0)
player.speed(0)

#variables
ammos=[]
ammissiles=[]
ammqty=0
missqty=0
limit=0
misslimit=0
run=True
missrun=True
score=0
message=('you have exhausted your ammo')
life=5

#pen
pen=turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.setposition(-50,265)
pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))

#fire
fire=turtle.Turtle()
fire.color('red')
fire.shape('square')
fire.penup()
fire.shapesize(stretch_wid=-0.2,stretch_len=-0.2)
fire.speed(0)
fire.setposition(-375,100)

#missile
missile=turtle.Turtle()
missile.color('red')
missile.shape('square')
missile.penup()
missile.shapesize(stretch_wid=-0.1,stretch_len=-0.4)
missile.speed(0)
missile.setposition(-375,150)

#create multiple goals
maxgoals=4
goals=[]

for coun in range (maxgoals+1):
    goals.append(turtle.Turtle())
    goals[coun].color("red")
    goals[coun].shape("enemy_left.gif")
    goals[coun].penup()
    goal_xcor=random.randint(385,450)
    goal_ycor=random.randint(-245,245)
    goals[coun].setposition(goal_xcor,goal_ycor)
    goals[coun].speed(0)
    goals[coun].left(180)

#speed variables
speed=0.3
missilespeed=0.3
burstspeed=0.3

#functions
def player_up():
    a=player.ycor()
    a +=15
    player.sety(a)

def player_down():
    a=player.ycor()
    a -=15
    player.sety(a)

def player_forward():
    f=player.xcor()
    f +=15
    player.setx(f)

def player_behind():
    f=player.xcor()
    f -=15
    player.setx(f)

def shoot():
    y=player.ycor()
    x=player.xcor()
    fire.goto(x,y)
    global ammqty
    ammqty+=1

def launch():
    ly=player.ycor()
    lx=player.xcor()
    missile.goto(lx,ly)
    global missqty
    missqty+=1

#bindings
wn.listen()
wn.onkeypress(player_up,"Up")
wn.onkeypress(player_down,"Down")
wn.onkeypress(player_forward,"Right")
wn.onkeypress(player_behind,"Left")
wn.onkeypress(shoot,"f")
wn.onkeypress(launch,"q")

while True:
    wn.update()
    fire.forward(speed)
    missile.forward(missilespeed)

    #ammo showpiece
    if fire.xcor() <-365 and fire.xcor() >-400:
        speed=0
    if missile.xcor() < -365 and missile.xcor() >-400:
        missilespeed=0

    #run ammo
    if run==True:
        if ammqty>0:
            #increase ammo
            ammo=turtle.Turtle()
            ammo.speed(0)
            ammo.shape("square")
            ammo.shapesize(stretch_wid=0.2,stretch_len=0.2)
            ammo.color("red")
            ammo.penup()
            px=player.xcor()
            py=player.ycor()
            ammo.goto(px,py)
            ammos.append(ammo)
            ammqty=0
            limit+=1
    #run missile
    if missrun==True:
        if missqty>0:
            #increase missile
            ammissile=turtle.Turtle()
            ammissile.speed(0)
            ammissile.shape('square')
            ammissile.shapesize(stretch_wid=0.2,stretch_len=0.3)
            ammissile.color('red')
            ammissile.penup()
            px=player.xcor()
            py=player.ycor()
            ammissile.goto(px,py)
            ammissiles.append(ammissile)
            missqty=0
            misslimit+=1

    #limit the ammo
    if limit>15:
        run=False
    if misslimit>15:
        missrun=False

    #fire ahead
    if fire.xcor()>-365:
        speed=0.5
    if missile.xcor()>-365:
        missilespeed=0.5

    #move the goals
    for m in range(coun+1):
        goals[m].forward(0.3)

    #len of ammos
    ammo_length=len(ammos)
    missamm_length=len(ammissiles)
    
    #ammo ahead
    for amm in range(0,ammo_length):
        ammos[amm].forward(speed)
        
        #ammo and goal hit check
        for gol in range(coun+1):
            if (ammos[amm].xcor()<goals[gol].xcor()+10 and ammos[amm].xcor()>goals[gol].xcor()-10) and (ammos[amm].ycor()<goals[gol].ycor()+10 and ammos[amm].ycor()>goals[gol].ycor()-10):
                goals[gol].goto(random.randint(385,450),random.randint(-245,245))
                score+=1
                pen.clear()
                pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))
            #hit check
            elif (fire.ycor()<goals[gol].ycor()+10 and fire.ycor()>goals[gol].ycor()-10) and (fire.xcor() < goals[gol].xcor()+10 and fire.xcor()>goals[gol].xcor()-10):
                goals[gol].goto(0,0)
                goals[gol].goto(random.randint(385,450),random.randint(-245,245))
                score+=1
                pen.clear()
                pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))

    #missamm ahead
    for misamm in range(0,missamm_length):
        ammissiles[misamm].forward(missilespeed)

        #missileamm and goal hit check
        for gool in range(coun+1):
            if (ammissiles[misamm].xcor()<goals[gool].xcor()+10 and ammissiles[misamm].xcor()>goals[gool].xcor()-10) and (ammissiles[misamm].ycor()<goals[gool].ycor()+10 and ammissiles[misamm].ycor()>goals[gool].ycor()-10):
                goals[gool].goto(random.randint(385,450),random.randint(-245,245))
                score+=1
                pen.clear()
                pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))
            #hit check
            elif (missile.ycor()<goals[gool].ycor()+10 and missile.ycor()>goals[gool].ycor()-10) and (missile.xcor() < goals[gool].xcor()+10 and missile.xcor()>goals[gool].xcor()-10):
                goals[gool].goto(0,0)
                goals[gool].goto(random.randint(385,450),random.randint(-245,245))
                score+=1
                pen.clear()
                pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))

    #boundary checking
    for gol in range(coun+1):
        if goals[gol].xcor()<-365:
            goals[gol].goto(random.randint(385,450),random.randint(-245,245))
            life-=1
            pen.clear()
            pen.write("score : {}   life : {}".format(score,life),font=("Agencyfb",15,"normal"))
    #player boundary checking
    if player.ycor()>275:
        py=player.ycor()
        py-=15
        player.sety(py)
    if player.ycor()<-265:
        py=player.ycor()
        py+=15
        player.sety(py)

    #end game
    if life<1:
        pen.setposition(-60,0)
        pen.write("Game over",font=("Agencyfb",30))
        break
else:
    exit


        
        

    
