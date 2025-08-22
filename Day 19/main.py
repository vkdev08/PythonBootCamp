import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
def move_forward():
    tim.forward(100)
def move_backward():
    tim.right(180)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(key="d",fun=move_right) #here no () in move_forward
#because its a method called inside a method when condition is triggered
#parenthesis triggers it as soon the code reads it - which we don't want
#funtion as a input into another function

#Higher order functions:
#a function as input into another functions - not many languages can do this

screen.exitonclick()