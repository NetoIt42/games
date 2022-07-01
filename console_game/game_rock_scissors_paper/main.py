import random

ROCK = 0
SCISSORS = 1
PAPER = 2

ACTION = {
    ROCK: "ROCK",
    SCISSORS: "SCISSORS",
    PAPER: "PAPER"
}

print(f"0 - rock \n"
      f"1 - scissors \n"
      f"2 - paper \n")

win_bot = 0
win_human = 0
run = True
while run:
    try:
        human = int(input("Enter action: "))

        bot = random.randint(0, 2)
        print(f"You chose: {ACTION.get(human)}")
        print(f"The bot chose: {ACTION.get(bot)} \n")

        if human == ROCK:
            if bot == SCISSORS:
                win_human += 1
            elif bot == PAPER:
                win_bot += 1

        elif human == SCISSORS:
            if bot == PAPER:
                win_human += 1
            elif bot == ROCK:
                win_bot += 1

        elif human == PAPER:
            if bot == ROCK:
                win_human += 1
            elif bot == SCISSORS:
                win_bot += 1

        else:
            print('Incorrect input')

        if (win_bot >= 3) or (win_human >= 3):  # если кто-то набирает 3 победы игра окончена
            run = False
    except ValueError:
        print('Введите число')

print(f"Score: \n"
      f"You: {win_human} \n"
      f"Bot: {win_bot}")
