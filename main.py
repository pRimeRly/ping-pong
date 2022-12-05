import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)


def app():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Ping Pong")
    screen.tracer(0)

    l_paddle = Paddle(LEFT_PADDLE_POSITION)
    r_paddle = Paddle(RIGHT_PADDLE_POSITION)
    ball = Ball()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
                ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset_ball()
            scoreboard.increase_left_score()
        if ball.xcor() < -380:
            ball.reset_ball()
            scoreboard.increase_right_score()
    screen.exitonclick()


try:
    app()
except Exception:
    pass
