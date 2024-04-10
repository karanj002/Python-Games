#bricks game
import turtle
import time
import random

delay=15
#screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle
pad=turtle.Turtle()
pad.shape('square')
pad.penup()
pad.color('white')
pad.setposition(0,-255)
pad.shapesize(stretch_wid=1,stretch_len=5)
pad.speed(0)

#ball
ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.setposition(0,-235)
ball.speed(0)
ball.dx = 0.5
ball.dy = 0.5
    
#functions
def paddleleft():
    a=pad.xcor()
    a -=20
    pad.setx(a)

def paddleright():
    a=pad.xcor()
    a +=20
    pad.setx(a)

#bindings
wn.listen()
wn.onkeypress(paddleleft,"a")
wn.onkeypress(paddleright,"d")

#main game loop
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
        ball.setx(375)
        ball.dx *=-1

    if ball.xcor() <-375:
        ball.setx(-375)
        ball.dx *=-1
            
