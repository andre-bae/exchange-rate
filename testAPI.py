# CG-4KG7qfiw1foWQzQ1MNVcNzyW
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
from datetime import datetime as dt

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
            return f"Текущая цена Bitcoin на {dt.now().strftime('%Y-%m-%d %H:%M:%S')}: ${bitcoin_price:.2f}"
        else:
            return f"Ошибка при получении данных: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Произошла ошибка при выполнении запроса: {e}"


# Вызов функции для получения цены биткоина
result = get_bitcoin_price()
print(result)