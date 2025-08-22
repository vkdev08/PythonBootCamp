from turtle import Screen
from pad import Paddle
from ball import Ball
import time
#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
START_POSITION_1 = (-390,0)
START_POSITION_2 = (380,0)
#screen creation
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #for screen update enable - to get rid of animation
screen.listen() #for listening to keystrokes


#paddle
player1 = Paddle(START_POSITION_1)
player2 = Paddle(START_POSITION_2)

#ball
ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkeypress(player1.go_up,"w")
    screen.onkeypress(player1.go_down,"s")
    screen.onkeypress(player2.go_up,"Up")
    screen.onkeypress(player2.go_down,"Down")
    player1.check_pos()
    player2.check_pos()
    ball.move()
    ball.bounce()
    ball.check_collision(player1)
    ball.check_collision(player2)
    if ball.xcor() > 380:
        player1.update_score()
        ball.reset_position()
    if ball.xcor() < -380:
        player2.update_score()
        ball.reset_position()

screen.exitonclick() # exit on x click