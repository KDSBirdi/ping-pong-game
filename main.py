import sys

import pygame
pygame.init()

import turtle
# import os

my_sound = pygame.mixer.Sound('pong_sound.mp3')

win = turtle.Screen()
win.title("PING PONG")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Left Stick
stick_a = turtle.Turtle()
stick_a.speed(0) #Speed of animation
stick_a.shape("square")
stick_a.color("white")
stick_a.shapesize(stretch_wid=5, stretch_len=1)
stick_a.penup()
stick_a.goto(-350, 0)



# Right Stick
stick_b = turtle.Turtle()
stick_b.speed(0) 
stick_b.shape("square")
stick_b.color("white")
stick_b.shapesize(stretch_wid=5, stretch_len=1)
stick_b.penup()
stick_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.1
ball.dy = 0.1


# Score
score_a=0
score_b=0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 22, "normal"))



def stick_a_up():
    y = stick_a.ycor()
    y+=20
    stick_a.sety(y)

def stick_a_down():
    y = stick_a.ycor()
    y-=20
    stick_a.sety(y)

def stick_b_up():
    y = stick_b.ycor()
    y+=20
    stick_b.sety(y)

def stick_b_down():
    y = stick_b.ycor()
    y-=20
    stick_b.sety(y)

def to_quit():
    sys.exit()


# Keyboard Binding
win.listen()
win.onkeypress(stick_a_up, "w")
win.onkeypress(stick_a_down, "s")

win.onkeypress(stick_b_up, "Up")
win.onkeypress(stick_b_down, "Down")

# Main Loop
while 1:
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("apaly")
        my_sound.play()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        my_sound.play()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 22, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 22, "normal"))


    # Stick and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stick_b.ycor() + 40) and (ball.ycor() > stick_b.ycor() - 40) :
        ball.setx(340)
        ball.dx *= -1
        my_sound.play()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stick_a.ycor() + 40) and (ball.ycor() > stick_a.ycor() - 40) :
        ball.setx(-340)
        ball.dx *= -1
        my_sound.play()


win.onkeypress(to_quit, "Escape")
