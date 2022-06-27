from random import choice
from typing import List, NoReturn, Callable, Optional


class Gallows:
    def __init__(self, words: List[str], hangman: List[str]):
        self._words: List[str] = words
        self._hangman: List[str] = hangman
        self._word: List[str] = []
        self._guessed_word: List[str] = []
        self.input_letter: str = ''
        self._error_count: int = 0
        self._errors: int = 6

    def choice_word(self) -> NoReturn:
        self._guessed_word = list(choice(self._words).lower())

        self._word = ["-"] * len(self._guessed_word)

    def enter_letter(self) -> NoReturn:
        self.input_letter = input('Enter letter: ').lower()

    def insert_letter(self, index: int) -> NoReturn:
        self._word[index] = self.input_letter

    def _check_len_letter(self) -> bool:
        if len(self.input_letter) == 1:
            return True

    def _check_language_letter(self) -> bool:
        if (ord(self.input_letter) >= 1072) and (ord(self.input_letter) <= 1103):
            return True

    def check_letter(self) -> Optional[str]:
        if self._check_len_letter():
            if self._check_language_letter():
                count: bool = True
                for index in range(len(self._guessed_word)):
                    if self.input_letter == self._guessed_word[index]:
                        self.insert_letter(index)
                        count = False

                if count:
                    self._error_count += 1
                    self._print_hangman()

                return

            else:
                return f"Enter the russian language"
        else:
            return f"Enter letter = 1"

    def _print_hangman(self) -> NoReturn:
        print(self._hangman[self._error_count])

    def check_error(self) -> bool:
        if self._error_count == self._errors:
            return True

        return False

    def check_win(self) -> bool:
        if str(self._word) == str(self._guessed_word):
            return True

        return False

    def get_word(self) -> List[str]:
        return self._word


if __name__ == "__main__":
    words_list: List[str] = [
        'Компьютер',
        'Телефон',
    ]

    hangman_list: List[str] = [
        """
         +-----+
               |
               |
               |
               |
        ========
        """,
        """
         +-----+
         |     |
         o     |
               |
               |
        ========
        """,
        """
         +-----+
         |     |
         o     |
         |     |
               |
        ========
        """,
        """
         +-----+
         |     |
         o     |
        /|     |
               |
        ========
        """,
        """
         +-----+
         |     |
         o     |
        /|\    |
               |
        ========
        """,
        """
         +-----+
         |     |
         o     |
        /|\    |
        /      |
        ========
        """,
        """
         +-----+
         |     |
         o     |
        /|\    |
        / \    |
        ========
        """,
    ]

    game = Gallows(words_list, hangman_list)
    game.choice_word()

    print(game.get_word())
    print(hangman_list[0])

    run: bool = True
    while run:
        game.enter_letter()
        msg = game.check_letter()

        if msg:
            print(msg)

        print(game.get_word())

        if game.check_error():
            run = False
            break

        if game.check_win():
            run = False
            print(f"----------\n"
                  f"|You win!|\n"
                  f"----------")
