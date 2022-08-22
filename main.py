from snake import *
from turtle import Screen
import time
from food import Food
from scoreboar import ScoreBoard
from gameover import GameOver



def init_screen():
    my_screen = Screen()
    my_screen.setup(width=600, height=600)
    my_screen.bgcolor("black")
    my_screen.title("Игра Змейка")
    my_screen.tracer(0)
    my_screen.onkey(snake.turn_forward, "Right")
    my_screen.onkey(snake.turn_back, "Left")
    my_screen.onkey(snake.turn_left, "Up")
    my_screen.onkey(snake.turn_right, "Down")
    my_screen.listen()
    return my_screen


snake = Snake()
food = Food()
score = ScoreBoard()
screen = init_screen()
game_is_on = True
endwall = (-300, 300)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Змея съела кусочек еды
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        score.whrite_score()
        snake.add_segment()

    # Змея столкнулась со стеной
    if (snake.head.xcor() > 290 or snake.head.xcor() < -295)\
            or (snake.head.ycor() > 290 or snake.head.ycor() < -295):
        game_is_on = False

    # Змея столкнулась со своим хвостом
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            break

    # Конец игры
    if not game_is_on:
        user_name = screen.textinput(title="Введите имя", prompt="Ваше имя")
        user_score = score.score
        gameover = GameOver(user_name, user_score)

screen.exitonclick()

