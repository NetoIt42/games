from player import HumanPlayer, BotPlayer
from tic_tac_toe import TicTacToe

tic_tac_toe = TicTacToe()

human_action, bot_action = tic_tac_toe.first_action()

human_player = HumanPlayer(human_action)
bot_player = BotPlayer(bot_action)

tic_tac_toe.settings_position(human_player, bot_player)
