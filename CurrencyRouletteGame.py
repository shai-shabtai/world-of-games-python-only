import requests
import random


def curr_roulette_game(difficulty):
    total_num_in_usd = random.randint(1, 100)
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=mCMEiGJ82uMpkqBqdKqKWWqYxaXAzVDXj2JFnGvb"
    response = requests.get(url)
    response_json = response.json()
    currency_value = response_json['data']['ILS']
    interval_values = get_money_interval(currency_value, difficulty, total_num_in_usd)
    guess_num = float(input(f"Please enter what you think should be the value of {total_num_in_usd}$ in NIS:\n"))
    return (float(interval_values[0])) <= guess_num <= (float(interval_values[1]))


def get_money_interval(currency_value, difficulty, total_num_in_usd):
    low_usd_range = total_num_in_usd * currency_value - (5 - int(difficulty))
    high_usd_range = total_num_in_usd * currency_value + (5 - int(difficulty))
    return low_usd_range, high_usd_range
