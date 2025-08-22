from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.high_score = 0
            self.penup()
            self.color("white")
            self.goto(0,280)
            self.hideturtle()
            self.write_score()
        def increase(self):
            self.score += 1
            self.write_score()

        def write_score(self):

            self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
            self.score = 0
            self.write_score()
        # def game_over(self):
        #     self.goto(0,0)
        #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)