from turtle import Turtle
MIN_DISTANCE = 50
LEFT_COLLISION = -360
RIGHT_COLLISION = 360
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # collision with wall
    def bounce(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1
    #collision with paddle
    def check_collision(self,paddle):
        if self.distance(paddle) < MIN_DISTANCE and (self.xcor()<LEFT_COLLISION or self.xcor() > RIGHT_COLLISION) :

            self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)