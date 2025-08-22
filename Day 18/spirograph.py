import turtle,random
timmy = turtle.Turtle()
screen = turtle.Screen()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b
screen.colormode(255)
timmy.speed("fastest")
while True:
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(5)
    print(timmy.heading())
    if timmy.heading() == 0:
        break

screen.exitonclick()
