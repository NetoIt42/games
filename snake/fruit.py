from random import randint
from typing import Tuple

from constant import WIDTH, HEIGHT


class Fruit:
    def __init__(self):
        self.width: int = WIDTH
        self.height: int = HEIGHT
        self._pos_x: int = 0
        self._pos_y: int = 0

    def get_pos_fruit(self) -> Tuple[int, int]:
        return self._pos_x, self._pos_y

    def set_pos_fruit(self):
        self._pos_x: int = randint(2, self.width - 2)
        self._pos_y: int = randint(2, self.height - 2)
