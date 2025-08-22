import turtle,random
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

timmy = turtle.Turtle()
timmy.speed("fastest")
screen = turtle.Screen()
screen.colormode(255)
n = 3
while n<11:
    timmy.pencolor(random_color())
    for i in range(n):
        timmy.forward(100)
        timmy.left(360/n)
    n = n+1
screen.exitonclick()
