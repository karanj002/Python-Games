import turtle
import time

delay=15
#screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle_a
pad_a=turtle.Turtle()
pad_a.shape('square')
pad_a.penup()
pad_a.color('white')
pad_a.setposition(-355,0)
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.speed(0)

#paddle_b
pad_b=turtle.Turtle()
pad_b.shape('square')
pad_b.penup()
pad_b.color('white')
pad_b.setposition(355,0)
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.speed(0)

#ball
ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.setposition(0,0)
ball.speed(0)
ball.dx = 0.5
ball.dy = 0.5

#functions
def paddle_a_up():
    a=pad_a.ycor()
    a +=20
    pad_a.sety(a)

def paddle_a_down():
    a=pad_a.ycor()
    a -=20
    pad_a.sety(a)

def paddle_b_up():
    b=pad_b.ycor()
    b +=20
    pad_b.sety(b)

def paddle_b_down():
    b=pad_b.ycor()
    b -=20
    pad_b.sety(b)

#bindings
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border_checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() >375:
        ball.goto(0,0)
        ball.dx *=-1

    if ball.xcor() <-375:
        ball.goto(0,0)
        ball.dx *=-1

    #paddle and ball collisions
    if ball.xcor() >340 and ball.xcor()<350 and (ball.ycor() <pad_b.ycor() +50) and (ball.ycor() > pad_b.ycor() -50):
        ball.dx *=-1

    if ball.xcor() <-340 and ball.xcor()> -350 and (ball.ycor() <pad_a.ycor() +50) and (ball.ycor() > pad_a.ycor() -50):
        ball.dx *=-1
    
