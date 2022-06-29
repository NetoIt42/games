import random
from typing import Tuple

from constant import WIDTH, HEIGHT, HEAD_D, HEAD_W, HEAD_A, HEAD_S


class Snake:
    def __init__(self):
        self.width: int = WIDTH
        self.height: int = HEIGHT
        self._tail: int = 0
        self._pos_x: int = random.randint(2, self.width - 2)
        self._pos_y: int = random.randint(2, self.height - 2)
        self._icon: str = HEAD_D
        self._score: int = 0

    def get_pos_snake(self) -> Tuple[int, int, str]:
        return self._pos_x, self._pos_y, self._icon

    def update_pos_snake(self, btn: str) -> Tuple[int, int, str]:
        if btn == 'd':
            self._pos_x += 1
            self._icon = HEAD_D
        elif btn == 'a':
            self._pos_x -= 1
            self._icon = HEAD_A
        elif btn == 'w':
            self._pos_y -= 1
            self._icon = HEAD_W
        elif btn == 's':
            self._pos_y += 1
            self._icon = HEAD_S

        return self._pos_x, self._pos_y, self._icon

    def check_eat_fruit(self, pos_frt: Tuple[int, int]) -> bool:
        if (self._pos_x == pos_frt[0]) and (self._pos_y == pos_frt[1]):
            self._tail += 1
            self._score += 1
            return True

        return False

    def check_lose(self) -> bool:
        if (self._pos_x == self.width) or (self._pos_y == self.height):
            return False

        return True

    def get_tail_snake(self) -> int:
        return self._tail

    def get_score(self) -> int:
        return self._score
