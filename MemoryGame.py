import random
from time import sleep
import os
from os import system


def memory_game(difficulty):
    generate_sequence = []
    for i in range(0, int(difficulty)):
        generate_sequence.append(random.randint(1, 101))
    print(generate_sequence)
    sleep(0.7)
    # os.system('cls' if os.name == 'nt' else 'clear')
    system('clear')
    remember_numbers = get_list_from_user(difficulty)
    return remember_numbers == generate_sequence


def get_list_from_user(difficulty):
    print(f"Please enter {difficulty} numbers:")
    remember_numbers = []
    for i in range(0, int(difficulty)):
        remember_numbers.append(int(input()))
    print(remember_numbers)
    return remember_numbers
