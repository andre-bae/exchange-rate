# CG-4KG7qfiw1foWQzQ1MNVcNzyW
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
# import json
from datetime import datetime as dt
# from typing import List, Dict
# from termcolor import colored

# Функция для получения цены биткоина
def get_price():
    cr_coin = combobox_crypta.get()
    ids = cr_coin.lower()
    fi0 = combobox_fiat.get()
    fiat_name = fiat[fi0]
    fi1 = fi0.lower()
#    print(fiat_name)
    # Настройка параметров запроса
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids,
        "vs_currencies": fi1,
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
            price = data[ids][fi1]
            crypt_price = f"{price:.2f}"
            len1 = len(crypt_price)
            if len1 >6:
                i = 6
                while i< len1:
                    crypt_price = crypt_price[:-i] + ' ' + crypt_price[-i:]
                    i +=4
            # return f"Текущая цена биткоина: {crypt_price} USD"
            t_label.config(text=f"На {dt.now().strftime('%H:%M %d.%m.%Y')}\n"
                                f"Текущий курс {cr_coin} составляет  \n"
                                f"{crypt_price} {fiat_name}\n"
                                f"(Последнее обновление курса: "
                                f"{dt.fromtimestamp(update_time).strftime('%H:%M:%S %d.%m.%Y')})")
        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")

# -------------------------------------------

# Создание графического интерфейса
window = Tk()
window.title("Курсы криптовалют к фиатным")
window.geometry("360x300")

crypt_label = ttk.Label(text='Криптовалюта')
crypt_label.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

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
combobox_crypta.grid(row=0, column=1, padx=10, pady=10, sticky=EW)


fiat_label = ttk.Label(text='Фиатные валюты')
fiat_label.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

fiat = {
    "USD": "Долларов США",
    "Rub": "Рублей",
    "EUR": "Евро"
}

fi = list(fiat.keys())
fi_var = StringVar(value=fi[0])

combobox_fiat = ttk.Combobox(window, textvariable=fi_var, values=fi, state="readonly")
combobox_fiat.grid(row=1, column=1, padx=10, pady=10, sticky=EW)


Button(text="Получить курс обмена", command=get_price).grid(row=2, column=0, padx=10, pady=10, sticky=EW)

t_label = ttk.Label(text='')
t_label.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky=EW)

window.mainloop()

