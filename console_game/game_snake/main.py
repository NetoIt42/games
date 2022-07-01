import os
import select
import sys
import time
from typing import NoReturn

from board import Board
from fruit import Fruit
from snake import Snake

from constant import TIME_LVL_5


def clear() -> NoReturn:
    os.system('clear')


board = Board()
snake = Snake()
fruit = Fruit()

button: str = 'd'

while snake.check_lose():
    clear()

    position_fruit = fruit.get_position_fruit()
    tails = snake.get_tail()

    board.generate_board(
        snake.get_score(),
        tails,
        snake.get_position_snake(),
        fruit.get_position_fruit()
    )

    if snake.check_eat_fruit(position_fruit, TIME_LVL_5):
        fruit.set_position_fruit(tails)

    i, o, e = select.select([sys.stdin], [], [], 1)

    if i:
        button = sys.stdin.readline().strip().lower()
    else:
        button = button

    if button == 'q':
        sys.exit()

    snake.movement(button)

    time.sleep(TIME_LVL_5)
