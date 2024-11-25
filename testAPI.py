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
                while i <= len1:
                    crypt_price = crypt_price[:-i] + ' ' + crypt_price[-i:]
                    i +=4
            # return f"Текущая цена биткоина: {crypt_price} USD"
            t_label2.config(text=f"{dt.now().strftime('%H часов %M минут    %d.%m.%Y')}")
            t_label4.config(text=f"{cr_coin}")
            t_label6.config(text=f" {crypt_price} ")
            t_label7.config(text=f" {fiat_name}")
            t_label8.config(text= f"(Последнее обновление курса: {dt.fromtimestamp(update_time).strftime('%H:%M:%S %d.%m.%Y')})")
            t_label1.pack(side=LEFT, padx=5)
            t_label2.pack(side=LEFT, padx=5)
            t_label3.pack(side=LEFT, padx=5)
            t_label4.pack(side=LEFT, padx=5)
            t_label5.pack(side=LEFT, padx=5)
            t_label6.pack(side=LEFT, padx=10)
            t_label7.pack(side=LEFT, padx=5)
            t_label8.pack(side=LEFT, padx=5, pady=5)
        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")

# -------------------------------------------

# Создание графического интерфейса
window = Tk()
window.title("Курсы криптовалют к фиатным")
window.geometry("360x300")


f1 = Frame(window, borderwidth=1, relief=SOLID)
f1.pack(padx=10)
f2 = Frame(window)
f2.pack(anchor=NW, padx=10, pady=(10,0))
f3 = Frame(window)
f3.pack(anchor=NW, padx=10)
f4 = Frame(window)
f4.pack(anchor=NW, padx=10, pady=5)
f5 = Frame(window)
f5.pack(anchor=NW, padx=10)

crypt_label = ttk.Label(f1, text='Криптовалюта')
crypt_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

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

combobox_crypta = ttk.Combobox(f1, textvariable=cr_var, values=cr, state="readonly")
combobox_crypta.grid(row=0, column=1, padx=10, pady=10, sticky=EW)


fiat_label = ttk.Label(f1, text='Фиатные валюты')
fiat_label.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

fiat = {
    "USD": "Долларов США",
    "Rub": "Рублей",
    "EUR": "Евро"
}

fi = list(fiat.keys())
fi_var = StringVar(value=fi[0])

combobox_fiat = ttk.Combobox(f1, textvariable=fi_var, values=fi, state="readonly")
combobox_fiat.grid(row=1, column=1, padx=10, pady=10, sticky=EW)


Button(f1, text="Получить курс обмена", command=get_price).grid(row=2, column=1, padx=10, pady=10, sticky=EW)

t_label1 = ttk.Label(f2, text='На ', font=("Helvetica 10"))
t_label2 = ttk.Label(f2, text='', font=("Helvetica 10 bold"))
t_label3 = ttk.Label(f3, text='Текущий курс ', font=("Helvetica 10"))
t_label4 = ttk.Label(f3, text='', font=("Helvetica 10 bold"))
t_label5 = ttk.Label(f3, text=' составляет  ', font=("Helvetica 10"))
t_label6 = ttk.Label(f4, text='', font=("Helvetica 14 bold"), foreground='Red', background='White', borderwidth=1, relief=SOLID)
t_label7 = ttk.Label(f4, text='', font=("Helvetica 10 bold"))
t_label8 = ttk.Label(f5, text='')



window.mainloop()

