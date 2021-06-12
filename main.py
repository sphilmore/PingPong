from turtle import Turtle, Screen
from pong import Pong
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
pong_1 = Pong((350, 0))
pong_2 = Pong((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()






screen.listen()
screen.onkey(pong_1.go_up, "Up")
screen.onkey(pong_1.go_down, "Down")
screen.onkey(pong_2.go_up, "w")
screen.onkey(pong_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#Detect the collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#Detect collison with r_paddle
    if ball.distance(pong_1) < 50 and ball.xcor() > 320 or ball.distance(pong_2) < 50 and ball.xcor() <- 320:
        ball.bounce_x()


#Detect the ball out of bounds
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_score_update()


    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_score_update()









screen.exitonclick()