from turtle import Turtle
LOWERBOUND_Y = -250
UPPERBOUND_Y = 260
LOWERBOUND_PLACING = -240
UPPERBOUND_PLACING = 250
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def check_pos(self):
        if self.ycor() <= LOWERBOUND_Y:
            self.sety(LOWERBOUND_PLACING)
        elif self.ycor() >= UPPERBOUND_Y:
            self.sety(UPPERBOUND_PLACING)
    def update_score(self):
        self.score += 1