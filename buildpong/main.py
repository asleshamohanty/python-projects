import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
division = Turtle()
ball = Ball()
scoreboard = ScoreBoard()

#making division
division.hideturtle()
division.color("white")
division.goto(0,-300)
division.goto(0,300)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_collision()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_collision()

    if ball.xcor() > 410:
        time.sleep(1)
        ball.home()
        time.sleep(0.1)
        scoreboard.increase_l_score()
        ball.regame()

    if ball.xcor() < -410:
        ball.home()
        time.sleep(0.1)
        scoreboard.increase_r_score()
        ball.regame()



screen.exitonclick()