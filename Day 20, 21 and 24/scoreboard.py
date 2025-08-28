from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            with open("data.txt",mode = 'r') as data:
                self.high_score = int(data.read())
            self.penup()
            self.color("white")
            self.goto(0,280)
            self.hideturtle()
            self.write_score()
        def increase(self):
            self.score += 1
            self.write_score()

        def write_score(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("data.txt",mode='w') as data:
                    data.write(str(self.high_score))
            self.score = 0
            self.write_score()
        # def game_over(self):
        #     self.goto(0,0)
        #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)