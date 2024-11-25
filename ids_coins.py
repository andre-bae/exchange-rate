from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
from datetime import datetime as dt
from typing import List, Dict

def get_all_coins() -> List[Dict]:
    # URL для получения списка всех криптовалют
    url = "https://api.coingecko.com/api/v3/coins/list"

    try:
        # Выполнить GET-запрос к API CoinGecko
        response = requests.get(url)

        if response.status_code == 200:
            # Преобразовать JSON в список словарей
            data = response.json()

            return data
        else:
            print(f"Ошибка при получении данных: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return []


# Вызов функции для получения списка всех криптовалют
all_coins = get_all_coins()

# Вывод результатов (пример)
if all_coins:
    print('Список первых 10 из всех криптовалют')
    for coin in all_coins[:]:  # Вывод только первых 10 монет
#        print(f"Идентификатор: {coin['id']}, Название: {coin['name']}, Символ: {coin['symbol']}")
        with open("coins_symbols.txt", "a", encoding='utf-8') as file:
            file.writelines(f"\n{coin['symbol']}\t\t\t\t{coin['id']}")
#        print(f"{coin['symbol']}\t\t\t\t{coin['id']}")
