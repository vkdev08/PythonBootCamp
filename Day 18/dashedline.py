import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
screen.exitonclick()