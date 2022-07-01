import os

from random import choices
from typing import List, Tuple


def clear() -> None:
    os.system('clear')


def read_csv_file() -> List[Tuple[str, str]]:
    quest_answers: List[Tuple[str, str]] = []
    with open('quiz.csv', 'r') as question:
        while True:
            line: List[str] = question.readline().strip().split(',')

            if line == ['']:
                break

            quest_answers.append((line[1], line[2]))

    return quest_answers


def random_choice_quest(quest_answers: List[Tuple[str, str]]) -> Tuple[str, str]:
    quest_answer: Tuple[str, str] = choices(quest_answers)[0]

    return quest_answer


def quiz_game(quest_answer: Tuple[str, str], win: int, loss: int) -> Tuple[int, int]:
    question: str = quest_answer[0]
    answer: str = quest_answer[1]

    print(F"Question: {question}")
    player_answer: str = input('Enter answer: ')

    win, loss = check_win(player_answer, answer, win, loss)

    return win, loss


def check_win(answer_1: str, answer_2: str, win: int, loss: int) -> Tuple[int, int]:
    if answer_1.lower() == answer_2.lower():
        win += 1
    else:
        loss += 1

    return win, loss


if __name__ == "__main__":
    quiz = read_csv_file()

    count_question: int = 5
    right: int = 0
    not_right: int = 0
    for i in range(count_question):
        question_answer = random_choice_quest(quiz)
        right, not_right = quiz_game(question_answer, right, not_right)
        clear()

    print(f"Score:\n"
          f"-Right: {right}\n"
          f"-Not right: {not_right}\n"
          f"-Percentage of correct answers: {right / count_question * 100}%")
