import time
import turtle
from turtle import Turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Snake Game")
screen.tracer(0)
segments = []
starting_position = [(0,0),(-20,0),(-40,0)]
#snake start
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    turtle.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].right(90)
    
screen.exitonclick()