from GuessGame import guess_game
from MemoryGame import memory_game
from CurrencyRouletteGame import curr_roulette_game


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"


def check_value_in_range(value, end_range):
    return value.isnumeric() and int(value) in range(1, end_range)


def load_game():
    games = [{"game_name": "Memory Game",
              "game_desc": "a sequence of numbers will appear for 1 second and you have to guess it back"},
             {"game_name": "Guess Game", "game_desc": "guess a number and see if you chose like the computer"},
             {"game_name": "Currency Roulette",
              "game_desc": "try and guess the value of a random amount of USD in ILS"}]
    num_of_games = len(games)
    while True:
        # choose_game = input(f"Please choose a game to play: \n{list_of_games}\n")
        print(f"Please choose a game to play:")
        [print(f"{games.index(game) + 1}. {game['game_name']} - {game['game_desc']}") for game in games]
        choose_game = input()
        if check_value_in_range(choose_game, num_of_games + 1):
            break
        else:
            print(f"The value is not a number between 1 to {num_of_games}, Please try again\n")
    print(f"The chosen game is: {games[int(choose_game) - 1]['game_name']}\n")
    while True:
        difficulty = input("Please choose game difficulty from 1 to 5: \n")
        if check_value_in_range(difficulty, 6):
            break
        else:
            print(f"The value is not a number between 1 to 5, Please try again\n")
    print(f"The chosen game level is: {difficulty}\n")
    is_winner = play(choose_game, difficulty)
    if is_winner:
        print("You won the game!")
    else:
        print("Try next time....")


def play(game, difficulty):
    if game == '1':
        return memory_game(difficulty)
    elif game == '2':
        return guess_game(difficulty)
    else:
        return curr_roulette_game(difficulty)
