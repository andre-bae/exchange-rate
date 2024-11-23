# CG-4KG7qfiw1foWQzQ1MNVcNzyW
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
from datetime import datetime as dt
from typing import List, Dict

# Функция для получения цены биткоина
def get_bitcoin_price():
    # Настройка параметров запроса
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    headers = {"Accepts": "application/json"}

    try:
        # Выполнение GET-запроса
        response = requests.get(url=url, params=params, headers=headers)

        # Обработка ответа
        if response.status_code == 200:
            data = response.json()
            bitcoin_price = data['bitcoin']['usd']
            # return f"Текущая цена биткоина: {bitcoin_price} USD"
            t_label.config(text=f"Текущая цена Bitcoin на {dt.now().strftime('%Y-%m-%d %H:%M:%S')}: ${bitcoin_price:.2f}")
        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")

# ------------списoк всех криптовалют---------------------------------------

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
    for coin in all_coins[:10]:  # Вывод только первых 10 монет
        print(f"Идентификатор: {coin['id']}, Название: {coin['name']}, Символ: {coin['symbol']}")

# ------------Список поддерживаемых валют------------------------------

url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print(f'\nСписок поддерживаемых валют\n')
print(response.text)

# -------------------------------------------

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x300")

# Вызов функции для получения цены биткоина
#result = get_bitcoin_price()
#print(result)

t_label = ttk.Label(text='')
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=get_bitcoin_price).pack(padx=10, pady=10)

window.mainloop()
