from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from datetime import datetime as dt
# import os

def choice():
    if ord(combobox_crypta.get()[0]) < 1000:
        get_price()
    else:
        exchange()

# Функция для получения цены фиатной валюты
def exchange():
    fiat_name = combobox_fiat.get()
    target_code = fiat_name.upper()
    cr_coin = combobox_crypta.get()
    base_code = crypta[cr_coin].upper()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()
#            print(data)
            update_time = data['time_last_update_unix']

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
#                base = base_code # currencies[base_code]
#                target = target_code # currencies[target_code]
                crypt_price = f"{exchange_rate}"
#                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")

                t_label2.config(text=f"{dt.now().strftime('%H часов %M минут    %d.%m.%Y')}")
                t_label4.config(text=f"{cr_coin}")
                t_label6.config(text=f" {crypt_price} ")
                t_label7.config(text=f" {fiat_name}")
                t_label8.config(text= f"( Последнее обновление курса: "
                                      f"{dt.fromtimestamp(update_time).strftime('%H:%M:%S %d.%m.%Y')} )")
                t_label1.pack(side=LEFT, padx=5)
                t_label2.pack(side=LEFT, padx=5)
                t_label3.pack(side=LEFT, padx=5)
                t_label4.pack(side=LEFT, padx=5)
                t_label5.pack(side=LEFT, padx=5)
                t_label6.pack(side=LEFT, padx=10)
                t_label7.pack(side=LEFT, padx=5)
#                t_label8.pack_forget()
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


# Функция для получения цены криптовалюты
def get_price():
    cr_coin = combobox_crypta.get()
    ids = cr_coin.lower()
    fi0 = combobox_fiat.get()
    fiat_name = fiat[fi0]
    fi1 = fi0.lower()

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
#            print(data)
            update_time = data[ids]['last_updated_at']
            price = data[ids][fi1]
            crypt_price = f"{price:.2f}"

            # Добавление пробелов в многозначное число
            len1 = len(crypt_price)
            if len1 >6:
                i = 6
                while i <= len1:
                    crypt_price = crypt_price[:-i] + ' ' + crypt_price[-i:]
                    i +=4

            t_label2.config(text=f"{dt.now().strftime('%H часов %M минут    %d.%m.%Y')}")
            t_label4.config(text=f"{cr_coin}")
            t_label6.config(text=f" {crypt_price} ")
            t_label7.config(text=f" {fiat_name}")
            t_label8.config(text= f"( Последнее обновление курса: "
                                  f"{dt.fromtimestamp(update_time).strftime('%H:%M:%S %d.%m.%Y')} )")
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

# ---------------------Создание графического интерфейса----------------------

window = Tk()
# window.iconbitmap('bitcoin.ico')
window.resizable(False, False)
window.attributes("-toolwindow", True)
window.title("Курсы валют")
window.geometry("420x300")

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

# Выбор криптовалюты
crypt_label = ttk.Label(f1, text='Базовая валюта:')
crypt_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

crypta = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Tether": "USDT",
    "solana": "sol",
    "Dogecoin": "doge",
    "Cardano": "ada",
    "Американский доллар": "USD",
    "Евро": "EUR",
    "Британский фунт стерлингов": "GBP",
    "Японская йена": "JPY",
    "Китайский юань": "CNY",
    "Российский рубль": "RUB",
    "Украинская гривна": "UAH",
    "Тайский бат": "THB",
    "Турецкая лира": "TRY",
    "Египетский фунт": "EGP",
    "Канадский доллар": "CAD",
    "Швейцарский франк": "CHF",
    "Казахстанский тенге": "KZT",
    "Узбекский сум": "UZS"
}

cr = list(crypta.keys())
cr_var = StringVar(value=cr[0])

combobox_crypta = ttk.Combobox(f1, textvariable=cr_var,
                               values=cr, state="readonly", width=28, height=20)
combobox_crypta.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

# Выбор фиатной валюты
fiat_label = ttk.Label(f1, text='Целевая валюта:')
fiat_label.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

fiat = {
    "USD": "Долларов США",
    "Rub": "Рублей",
    "EUR": "Евро"
}

fi = list(fiat.keys())
fi_var = StringVar(value=fi[1])

combobox_fiat = ttk.Combobox(f1, textvariable=fi_var, values=fi, state="readonly")
combobox_fiat.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

# Получение курса
Button(f1, text="Получить курс обмена", command=choice).grid(row=2, column=1,
                                                             padx=10, pady=10, sticky=EW)

t_label1 = ttk.Label(f2, text='На ', font="Helvetica 10")
t_label2 = ttk.Label(f2, text='', font="Helvetica 10 bold")
t_label3 = ttk.Label(f3, text='Текущий курс ', font="Helvetica 10")
t_label4 = ttk.Label(f3, text='', font="Helvetica 10 bold")
t_label5 = ttk.Label(f3, text=' составляет  ', font="Helvetica 10")
t_label6 = ttk.Label(f4, text='', font="Helvetica 14 bold",
                     foreground='Red', background='White', borderwidth=1, relief=SOLID)
t_label7 = ttk.Label(f4, text='', font="Helvetica 10 bold")
t_label8 = ttk.Label(f5, text='')

window.mainloop()
