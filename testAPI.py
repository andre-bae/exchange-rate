# CG-4KG7qfiw1foWQzQ1MNVcNzyW
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
from datetime import datetime as dt

# Настройка параметров запроса

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}
headers = {
    "Accepts": "application/json"
}

# Выполнение GET-запроса
response = requests.get(url=url, params=params, headers=headers)

# Обработка ответа
if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bitcoin']['usd']
    print(f"Текущая цена биткоина: {bitcoin_price} USD")
else:
    print(f"Ошибка при получении данных: {response.status_code}")
