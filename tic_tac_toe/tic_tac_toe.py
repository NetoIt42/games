from random import choice

ZERO = "0"
CROSS = "X"
ACTION = {
    ZERO: "0",
    CROSS: "X"
}

WIN = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


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


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()

    human_action, bot_action = tic_tac_toe.first_action()

    human_player = HumanPlayer(human_action)
    bot_player = BotPlayer(bot_action)

    tic_tac_toe.settings_position(human_player, bot_player)


