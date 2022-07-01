import random
from typing import Tuple

from constant import WIDTH, HEIGHT, HEAD_D


class Fruit:
    def __init__(self):
        self._width: int = WIDTH
        self._height: int = HEIGHT
        self._pos_x: int = random.randint(2, self._width - 2)
        self._pos_y: int = random.randint(2, self._height - 2)

    def get_position_fruit(self) -> Tuple[int, int]:
        return self._pos_x, self._pos_y

    def set_position_fruit(self, tail):
        while [self._pos_x, self._pos_y] in tail:
            self._pos_x: int = random.randint(2, self._width - 2)
            self._pos_y: int = random.randint(2, self._height - 2)