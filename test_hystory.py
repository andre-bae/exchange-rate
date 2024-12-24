from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import requests
from datetime import datetime as dt
import os
import sys
import base64

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------Функция для графика цены криптовалюты----------------------

def get_price_graf():
    cr_coin = combobox_crypta.get()
    ids = cr_coin.lower()
    tg0 = combobox_target.get()
    target_name = target[tg0]
    tg1 = tg0.lower()
    days_graf = 100

    # Настройка параметров запроса
    url = f"https://api.coingecko.com/api/v3/coins/bitc{ids}oin/market_chart?vs_currency={tg1}&days={days_graf}"
    headers = {"accept": "application/json"}

    try:
        # Выполнение GET-запроса
        response = requests.get(url, headers=headers)

        # Обработка ответа
        def unix_to_readable(unix_time):
            return dt.fromtimestamp(unix_time / 1000).strftime('%H:%M:%S %d.%m.%Y')

        if response.status_code == 200:
            data = response.json()

            graf_time = [row[0] for row in data['prices']]
            readable_times = [unix_to_readable(time) for time in graf_time]

            graf_price = [row[1] for row in data['prices']]

            # Создание массивов координат
            x = np.array(readable_times)
            y = np.array(graf_price)

            # Построение графика
            plt.figure(figsize=(10, 6))
            plt.plot(x, y)

            # Дополнительные настройки
            plt.title('Двумерный график из массива координат')
            plt.xlabel('Время')
            plt.ylabel('Ордината')
            plt.grid(True)

            # Отображение графика
            plt.show()

        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")

    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")


# ---------------------Создание графического интерфейса----------------------

#window = Tk()

get_price_graf()

#window.mainloop()