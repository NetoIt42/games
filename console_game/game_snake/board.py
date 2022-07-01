from typing import Tuple, List

from constant import WIDTH, HEIGHT


class Board:
    def __init__(self):
        self._width: int = WIDTH
        self._height: int = HEIGHT

    def generate_board(self, score: int,
                       tail: List[List[int]],
                       pos_snake: Tuple[int, int, str],
                       pos_fruit: Tuple[int, int]) -> None:

        print(f"Score: {score}")

        for y in range(self._height):
            for x in range(self._width):
                if (x == 0) and (y == 0):
                    print('+', end='')
                elif (x == self._width - 1) and (y == 0):
                    print('+', end='')
                elif (x == 0) and (y == self._height - 1):
                    print('+', end='')
                elif (x == self._width - 1) and (y == self._height - 1):
                    print('+', end='')
                elif (x == 0) or (x == self._width - 1):
                    print('|', end='')
                elif (y == 0) or (y == self._height - 1):
                    print('-', end='')
                elif (x == pos_snake[0]) and (y == pos_snake[1]):
                    print(pos_snake[2], end='')
                elif [x, y] in tail:
                    print('o', end='')
                elif (x == pos_fruit[0]) and (y == pos_fruit[1]):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

        print(f"Position snake: {pos_snake[0], pos_snake[1]}")

        print(f"Controls: WASD + Enter - movement\n"
              f"\t\t Q - exit")
