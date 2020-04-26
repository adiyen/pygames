import random
import turtle
from turtle import listen, onkeypress, onkey
import time

bird = turtle.Turtle()
bird.penup()
turtle.setup(420, 420)
wn = turtle.Screen() 
bird.shape("circle")
bird.color("green")
pipes = []

top_pipe = turtle.Turtle()
top_pipe.hideturtle()
top_pipe.penup()
top_pipe.shape("square")
top_pipe.shapesize(stretch_wid=15, stretch_len=2)
top_pipe.goto(0, 200)
top_pipe.showturtle()
pipes.append(top_pipe)

bottom_pipe = turtle.Turtle()
bottom_pipe.hideturtle()
bottom_pipe.penup()
bottom_pipe.shape("square")
bottom_pipe.shapesize(stretch_wid=15, stretch_len=2)
bottom_pipe.goto(0, -200)
bottom_pipe.showturtle()
pipes.append(bottom_pipe)

def jump():
    global bird
    y = bird.ycor()
    y+=20
    bird.goto(bird.xcor(), y)

def game():
    count = 0
    wn.onkey(jump, "Up")
    listen()
    while True:
        # wn.update()
        # time.sleep(0.1)
        bird_x = bird.xcor()
        bird_y = bird.ycor()

        y = bird.ycor()
        y-=5
        bird.goto(bird.xcor(), y)

        top_pipe = pipes[0]
        bottom_pipe = pipes[1]
        top_pipe.showturtle()
        bottom_pipe.showturtle()
        top_pipe_x = top_pipe.xcor()
        bottom_pipe_x = bottom_pipe.xcor()
        top_pipe_x-=10
        bottom_pipe_x-=10
        top_pipe.goto(top_pipe_x, top_pipe.ycor())
        bottom_pipe.goto(bottom_pipe_x, bottom_pipe.ycor())
        if(top_pipe_x < -210):
            top_pipe.hideturtle()
            bottom_pipe.hideturtle()
            space = random.randint(-50, 50)
            top_pipe.goto(200, top_pipe.ycor()+space)
            bottom_pipe.goto(200, bottom_pipe.ycor()+space)
            top_pipe.showturtle()
            bottom_pipe.showturtle()

game()
turtle.done()