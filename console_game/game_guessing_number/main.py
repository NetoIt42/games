import random
from typing import Tuple

ATTEMPT: int = 3


def guessing_number() -> None:
    attempt: int = 0
    run: bool = True

    while (attempt < ATTEMPT) and run:
        input_number: int = enter_number()
        random_number: int = generate_number()

        run = check_number(random_number, input_number)

        attempt += 1


def enter_number() -> int:
    print("Enter a number from 0 to 10")
    return int(input("Number: "))


def generate_number() -> int:
    return random.randint(0, 10)


def check_number(number_1: int, number_2: int) -> bool:
    if number_1 == number_2:
        print("You win!")
        return False
    elif number_1 < number_2:
        print("Need less!")
    else:
        print("Need more!")

    return True


if __name__ == "__main__":
    guessing_number()
