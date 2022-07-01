import random
from typing import Tuple, List

from constant import (
    WIDTH,
    HEIGHT,
    HEAD_D,
    HEAD_A,
    HEAD_W,
    HEAD_S,
    TIME_LVL_1,
    TIME_LVL_2,
    TIME_LVL_3,
    TIME_LVL_4,
    TIME_LVL_5,
)


class Snake:
    def __init__(self):
        self._head: str = HEAD_D
        self._tail: List[List[int]] = []
        self._width: int = WIDTH
        self._height: int = HEIGHT
        self._btn_default: str = 'd'
        self._score: int = 0
        self._pos_x: int = random.randint(2, self._width - 2)
        self._pos_y: int = random.randint(2, self._height - 2)

    def get_score(self) -> int:
        return self._score

    def get_tail(self) -> List[List[int]]:
        return self._tail

    def get_position_snake(self) -> Tuple[int, int, str]:
        return self._pos_x, self._pos_y, self._head

    def movement(self, btn: str) -> None:
        self._btn_default = self._check_button(btn)
        if self._btn_default == 'd':
            self._movement_tail()

            self._pos_x += 1
            self._head = HEAD_D
        elif self._btn_default == 'a':
            self._movement_tail()

            self._pos_x -= 1
            self._head = HEAD_A
        elif self._btn_default == 'w':
            self._movement_tail()

            self._pos_y -= 1
            self._head = HEAD_W
        elif self._btn_default == 's':
            self._movement_tail()

            self._pos_y += 1
            self._head = HEAD_S

    def _movement_tail(self) -> None:
        tail_old = []

        for i in range(len(self._tail)):
            if i == 0:
                tail_old = self._tail[i]
                self._tail[i] = [self._pos_x, self._pos_y]
            else:
                tail_old_2 = self._tail[i]
                self._tail[i] = tail_old
                tail_old = tail_old_2

    def check_lose(self) -> bool:
        if (self._pos_x == self._width) or (self._pos_x == 0):
            return False
        elif (self._pos_y == self._height) or (self._pos_y == 0):
            return False
        elif [self._pos_x, self._pos_y] in self._tail:
            return False

        return True

    def _check_button(self, btn: str) -> str:
        if (self._btn_default == 'd') and (btn == 'a'):
            return self._btn_default
        elif (self._btn_default == 'a') and (btn == 'd'):
            return self._btn_default
        elif (self._btn_default == 'w') and (btn == 's'):
            return self._btn_default
        elif (self._btn_default == 's') and (btn == 'w'):
            return self._btn_default

        self._btn_default = btn

        return self._btn_default

    def check_eat_fruit(self, pos_fruit: Tuple[int, int], score_x: int) -> bool:
        if (self._pos_x == pos_fruit[0]) and (self._pos_y == pos_fruit[1]):
            self._set_score(score_x)
            self._tail.append([pos_fruit[0], pos_fruit[1]])
            return True

        return False

    def _set_score(self, score_x):
        if score_x == TIME_LVL_1:
            self._score += 1
        elif score_x == TIME_LVL_2:
            self._score += 1 + int(TIME_LVL_2)
        elif score_x == TIME_LVL_3:
            self._score += 1 + int(TIME_LVL_3 * 2)
        elif score_x == TIME_LVL_4:
            self._score += 1 + int(TIME_LVL_4 * 10)
        elif score_x == TIME_LVL_5:
            self._score += 1 + int(TIME_LVL_5 * 1000)
