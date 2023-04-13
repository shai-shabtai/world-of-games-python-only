import random


def guess_game(difficulty):
    secret_number = random.randint(1, int(difficulty))
    guess_number = input(f"Please guess a number between 1 and {difficulty}: \n")
    print(f"The generated num is {secret_number}")
    print(f"The guess num is {guess_number}")
    return secret_number == int(guess_number)
