import select
import sys
import time
from typing import Tuple

from board import Board
from fruit import Fruit
from snake import Snake


def _clear():
    import os

    os.system('clear')


if __name__ == "__main__":
    board = Board()
    fruit = Fruit()
    snake = Snake()
    button: str = 'd'

    fruit.set_pos_fruit()

    position_snake = snake.get_pos_snake()
    while True:
        position_fruit: Tuple[int, int] = fruit.get_pos_fruit()

        if not snake.check_lose():
            print("You loss!")
            board.generate_board(position_snake, position_fruit, snake.get_tail_snake(), snake.get_score())
            break

        board.generate_board(position_snake, position_fruit, snake.get_tail_snake(), snake.get_score())
        i, o, e = select.select([sys.stdin], [], [], 1)

        if i:
            button = sys.stdin.readline().strip()
        else:
            button = button

        time.sleep(0.005)
        _clear()
        position_snake = snake.update_pos_snake(button)

        if snake.check_eat_fruit(position_fruit):
            fruit.set_pos_fruit()
