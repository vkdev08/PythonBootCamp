import turtle,random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

directions = [0,90,180,270]
timmy = turtle.Turtle()
screen = turtle.Screen()

screen.colormode(255)
for i in range(100):
    timmy.color(random_color())
    timmy.pensize(20)
    timmy.forward(50)
    timmy.setheading(random.choice(directions))

screen.exitonclick()