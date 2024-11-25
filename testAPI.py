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
    ids = combobox_crypta.get().lower()
    print(ids)
    # Настройка параметров запроса
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids, # "bitcoin",
        "vs_currencies": "usd",
        "include_last_updated_at": "true"
    }
    headers = {"Accepts": "application/json"}

    try:
        # Выполнение GET-запроса
        response = requests.get(url=url, params=params, headers=headers)

        # Обработка ответа
        if response.status_code == 200:
            data = response.json()
            print(data)
            update_time = data[ids]['last_updated_at']
            print("Время последнего обновления курса: ", dt.fromtimestamp(update_time).strftime('%Y-%m-%d %H:%M:%S'))
            bitcoin_price = data[ids]['usd']
            # return f"Текущая цена биткоина: {bitcoin_price} USD"
            t_label.config(text=f"Текущая цена Bitcoin на {dt.now().strftime('%Y-%m-%d %H:%M:%S')}: ${bitcoin_price:.2f}\n")
        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")

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

def selected(event):
    global num
    num = int(cb_kol.get())

crypta = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Binance Coin": "bnb"
}
#cr = StringVar(value=crypta["btc"])
#label_kol = ttk.Label(window,  text='Выберите криптовалюту', font=("Arial", 14))
#label_kol.pack(side=LEFT, padx=5, pady=5)
#cb_kol = ttk.Combobox(window, textvariable=cr, font=("Arial", 14), values=crypta[],
#                      state="readonly", width=10, height=4)
#cb_kol.pack(side=LEFT, padx=5, pady=5)
#cb_kol.bind("<<ComboboxSelected>>", selected)

cr = list(crypta.keys())
cr_var = StringVar(value=cr[0])
#cr.set(crypta.keys()[0])  # Устанавливаем первый ключ по умолчанию
combobox_crypta = ttk.Combobox(window, textvariable=cr_var, values=cr, state="readonly")

#for key in crypta:
#    combobox['values'] += tuple(crypta[key])
combobox_crypta.pack()

# cb_kol.bind("<<ComboboxSelected>>", selected)

window.mainloop()
