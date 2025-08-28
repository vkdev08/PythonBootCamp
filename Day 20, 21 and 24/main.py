import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase()
    #detect collision with tail

    #detect collision with wall
    for segment in snake.segments[2:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            score.reset()
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 290 or snake.head.ycor() < -290):
            score.reset()
            snake.reset()
screen.exitonclick()