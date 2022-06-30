from typing import Tuple

from constant import WIDTH, HEIGHT, HEAD_D


class Board:
    def __init__(self, ):
        self.width: int = WIDTH
        self.height: int = HEIGHT

    def generate_board(self, pos_player: Tuple[int, int, str], pos_fruit: Tuple[int, int], tail: int, score: int):
        print(f'Score: {score}')
        for y in range(self.height):
            for x in range(self.width):
                if (x == 0) and (y == 0):
                    print('+', end='')
                elif (x == 0) and (y == self.height - 1):
                    print('+', end='')
                elif (x == self.width - 1) and (y == 0):
                    print('+', end='')
                elif (x == self.width - 1) and (y == self.height - 1):
                    print('+', end='')
                elif (x == 0) or (x == self.width - 1):
                    print('|', end='')
                elif (y == 0) or (y == self.height - 1):
                    print('-', end='')
                elif (x == pos_player[0]) and (y == pos_player[1]):
                    print(pos_player[2], end='')
                elif (x == pos_fruit[0]) and (y == pos_fruit[1]):
                    print('*', end='')
                else:
                    print(' ', end='')

            print()
