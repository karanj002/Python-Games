#to be defined later
import turtle
import random
import time

#screen
screen=turtle.Screen()
screen.title("stharanzn game")
screen.bgcolor("black")
screen.setup(width=700 , height=700)
screen.tracer(5)

#player
player=turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.speed(0)

#border
border=turtle.Turtle()
border.penup()
border.color('red')
border.goto(-325,-325)
border.pendown()
for side in range(1,5):
    border.forward(650)
    border.left(90)
border.hideturtle()

#create multiple bombs
maxbombs=4
bomb=[]

for count in range (maxbombs+1):
    bomb.append(turtle.Turtle())
    bomb[count].color("red")
    bomb[count].shape("circle")
    bomb[count].penup()
    bomb[count].setposition(random.randint(-325,325),random.randint(-325,325))
    bomb[count].speed(0)

#pen
pen=turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.setposition(0,325)
pen.write("Score : 0 ", align="center", font=("Agencyfb",15,"normal"))

#variables
score=0
delay=0.1
speed=0
bombspeed=0

#functions
def go_left():
    player.left(30)
def go_right():
    player.right(30)
def increase_speed():
    global speed
    speed += 1
def decrease_speed():
    global speed
    speed -=1
def bomb_speed_down():
    global bombspeed
    bombspeed -=1
def bomb_speed_up():
    global bombspeed
    bombspeed +=1

#keyboard bindings
screen.listen()
screen.onkeypress(go_left , "Left" )
screen.onkeypress(go_right , "Right" )
screen.onkeypress(increase_speed,"Up")
screen.onkeypress(decrease_speed , "Down" )
screen.onkeypress(bomb_speed_down,"s")
screen.onkeypress(bomb_speed_up,"w")

while True:
    screen.update()
    c=time.process_time()
    player.forward(speed)
    for i in range (count+1):
        bomb[i].forward(bombspeed)

        #collision checking
        if player.distance(bomb[i])<20:
            x=random.randint(-300,300)
            y=random.randint(-300,300)
            score+=1
            bomb[i].setposition(x,y)
            pen.clear()
            pen.write("Score : {}  time passed {}".format(score,c), align="center", font=("Agencyfb",15,"normal"))
            time.sleep(delay)
            bomb[i].right(random.randint(0,360))
        
    #move the bombs
    for m in range(count+1):
        bomb[m].forward(3)
        
#boundary checking (bomb)
        if bomb[m].xcor() >=315:
            by=bomb[m].ycor()
            bomb[m].setposition(314,by)
            br=random.randint(60,140)
            bomb[m].right(br)
        if bomb[m].xcor()<=-315:
            by=bomb[m].ycor()
            bomb[m].setposition(-314,by)
            br=random.randint(60,140)
            bomb[m].right(br)
        if bomb[m].ycor() >=315:
            bx=bomb[m].xcor()
            bomb[m].setposition(bx,314)
            br=random.randint(60,140)
            bomb[m].right(br)
        if bomb[m].ycor() <=-315:
            bx=bomb[m].xcor()
            bomb[m].setposition(bx,-314)
            br=random.randint(60,140)
            bomb[m].right(br)
            

#boundary checking (player)
    if player.xcor() >325 or player.xcor() <-325:
        player.right(180)
    if player.ycor() >325 or player.ycor() <-325:
        player.right(180)

    #speed limit
    if speed>5:
        speed-=1
    if bombspeed>6:
        bombspeed-=1

    #end game
    if score==50:
        break

   


screen.mainloop()
