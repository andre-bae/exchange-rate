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
    cr_coin = combobox_crypta.get()
    ids = cr_coin.lower()
    fi = combobox_fiat.get()
    fiat_name = fiat[fi]
    print(fiat_name)
    # Настройка параметров запроса
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids, # "bitcoin",
        "vs_currencies": fi,
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
            price = data[ids][fi]
            crypt_price = f"{price:.2f}"
            len1 = len(crypt_price)
            if len1 >6:
                i = 6
                while i< len1:
                    crypt_price = crypt_price[:-i] + ' ' + crypt_price[-i:]
                    i +=4
            # return f"Текущая цена биткоина: {crypt_price} USD"
            t_label.config(text=f"Текущая цена {cr_coin} на {dt.now().strftime('%Y-%m-%d %H:%M:%S')}:\n {crypt_price} {fiat_name}\n")
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

crypta = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Tether": "USDT",
    "solana": "sol",
    "Dogecoin": "doge",
    "Cardano": "ada"
}

cr = list(crypta.keys())
cr_var = StringVar(value=cr[0])

combobox_crypta = ttk.Combobox(window, textvariable=cr_var, values=cr, state="readonly")
combobox_crypta.pack()


fiat = {
    "usd": "Долларов США",
    "rub": "Рублей",
    "eur": "Евро"
}

fi = list(fiat.keys())
fi_var = StringVar(value=fi[0])

combobox_fiat = ttk.Combobox(window, textvariable=fi_var, values=fi, state="readonly")
combobox_fiat.pack()


Button(text="Получить курс обмена", command=get_bitcoin_price).pack(padx=10, pady=10)

window.mainloop()
