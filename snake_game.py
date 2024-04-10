#snake game
import turtle
import time
import random

delay=0.1
#set up the screen
window=turtle.Screen()
window.title("snake game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)

tails=[]

#functions
def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_left():
    head.direction="left"
def go_right():
    head.direction="right"
    
def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard bindings
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

#main game loop
while True:
    window.update()

    #check for a collision with food
    if head.distance(apple)<20:
        #move food to a random spot on screen
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        apple.goto(x,y)
        # add a segment
        tail=turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color("grey")
        tail.penup()
        tails.append(tail)

    #move the end segments first in reverse order
    for index in range(len(tails)-1,0,-1):
        x=tails[index-1].xcor()
        y=tails[index-1].ycor()
        tails[index].goto(x,y)

    #move segment  0 to where the head is
    if len(tails) >0:
        x=head.xcor()
        y=head.ycor()
        tails[0].goto(x,y)

    #border teleportation
    if head.xcor()>300:
        hx=head.xcor()-1
        hy=head.ycor()
        head.goto(-hx,-hy)

    if head.xcor()<-300:
        hxx=head.xcor()+1
        hyy=head.ycor()
        head.goto(-hxx,-hyy)
        
    if head.ycor()>300:
        hx=head.xcor()-1
        hy=head.ycor()
        head.goto(-hx,-hy)

    if head.ycor()<-300:
        hxx=head.xcor()+1
        hyy=head.ycor()
        head.goto(-hxx,-hyy)

    #head tail collision
    for i in range(len(tails)-1,0,-1):
        tx=tails[i-1].xcor()
        ty=tails[i-1].ycor()
        if head.xcor()>tx and head.xcor()< tx and head.ycor()>ty and head.ycor()<ty :
            tails.clear()
    
    move()

    time.sleep(delay)

window.mainloop()
