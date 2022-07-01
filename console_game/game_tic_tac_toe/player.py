from random import choice
from constant import *


class Player:
    def __init__(self, action):
        self.action = action
        self.position = list(range(0, 9))

    def choice_position(self, field):
        pass


class HumanPlayer(Player):
    def __init__(self, action):
        super().__init__(action)

    def choice_position(self, field):
        choice_pos = int(input("Input position(1-9): "))
        if field[choice_pos - 1] is None:
            field[choice_pos - 1] = ACTION.get(self.action)
            self.position.remove(choice_pos - 1)

            return

        return self.choice_position(field)


class BotPlayer(Player):
    def __init__(self, action):
        super().__init__(action)

    def choice_position(self, field):
        choice_pos = choice(self.position)
        if field[choice_pos] is None:
            field[choice_pos] = ACTION.get(self.action)
            self.position.remove(choice_pos)

            return

        return self.choice_position(field)
