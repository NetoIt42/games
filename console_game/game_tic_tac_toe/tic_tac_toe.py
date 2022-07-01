from random import choice

from constant import *


class TicTacToe:
    def __init__(self):
        self.field = [None] * 9

    def check_win(self):
        for positions in WIN:
            if self.field[positions[0]] == self.field[positions[1]] == self.field[positions[2]]:
                return self.field[positions[0]]

        return False

    @staticmethod
    def first_action():
        human = choice([CROSS, ZERO])

        if human == CROSS:
            bot = ZERO
        else:
            bot = CROSS

        return human, bot

    def settings_position(self, player_1, player_2):
        count_player_1 = 0
        count_player_2 = 0
        run = True
        while run:
            player_1.choice_position(self.field)
            count_player_1 += 1
            if count_player_2 < 4:
                player_2.choice_position(self.field)
                count_player_2 += 1

            self.print_field()

            if count_player_1 + count_player_2 > 4:
                result = self.check_win()
                if result:
                    print(ACTION.get(result))
                    run = False

            if count_player_1 + count_player_2 == 9:
                run = False

    def print_field(self):
        print(f"{self.field[:3]}\n"
              f"{self.field[3:6]}\n"
              f"{self.field[6:9]}")

        print("-" * 18)
