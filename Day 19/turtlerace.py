import turtle
import webcolors
from colorsys import rgb_to_hls
import random
from operator import truediv


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

#screen set-up
screen = turtle.Screen()
screen.setup(600, 600)
screen.colormode(255)

#turtles - 3
#turtles setup for race
turtles = []
y = [-70,0,70];
cnt = 0
for i in range(3):
    tim = turtle.Turtle()
    tim.shape("turtle")
    tim.fillcolor(random_color())
    tim.penup()
    turtles.append(tim)
    tim.setpos(-280,y[cnt])
    cnt += 1
#start the race
racing_on = True
winner =  ""
while racing_on:
    for turtle in turtles:
        if turtle.xcor() > 280:
            racing_on = False
            fill_color_rgb = turtle.fillcolor()
            try:
                color = webcolors.rgb_to_name(fill_color_rgb, spec='css3')
            except ValueError:
                print(f"The winner has an RGB color of {fill_color_rgb}. No exact CSS3 color name found.")

        random_dis = random.randint(0,10)
        turtle.forward(random_dis)
print("Good game")
screen.exitonclick()