from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from datetime import datetime as dt


class FIAT:
    def __init__(self, country, id_fiat, text):
        self.country = country
        self.id = id_fiat
        self.text = text

list_fiat = [
    FIAT("США", "USD", "Американский доллар"),
    FIAT("Евросоюза", "EUR", "Евро"),
    FIAT("Великобритании", "GBP", "Британский фунт стерлингов"),
    FIAT("Японии", "JPY", "Японская йена"),
    FIAT("Китая", "CNY", "Китайский юань"),
    FIAT("России", "RUB", "Российский рубль"),
    FIAT("Украины", "UAH", "Украинская гривна"),
    FIAT("Тайланда", "THB", "Тайский бат"),
    FIAT("Турции", "TRY", "Турецкая лира"),
    FIAT("Египта", "EGP", "Египетский фунт"),
    FIAT("Канады", "CAD", "Канадский доллар"),
    FIAT("Швейцарии", "CHF", "Швейцарский франк"),
    FIAT("Казахстана", "KZT", "Казахстанский тенге"),
    FIAT("Узбекистана", "UZS", "Узбекский сум")
]


# Функция выбора базовой валюты: крипта или фиатная валюта
def choice():
    if s_val == valutes[0]: # ord(combobox_crypta.get()[0]) < 1000:
        get_price()
    else:
        exchange()


# Функция оформления вывода результата в метки
def label_config(coin, price, name, time):
    t_label2.config(text=f"{dt.now().strftime('%H часов %M минут    %d.%m.%Y')}")
    t_label4.config(text=f"{coin}")
    t_label6.config(text=f" {price} ")
    t_label7.config(text=f" {name}")
    t_label8.config(text=f"( Последнее обновление курса: "
                         f"{dt.fromtimestamp(time).strftime('%H:%M:%S %d.%m.%Y')} )")
    t_label1.pack(side=LEFT, padx=5)
    t_label2.pack(side=LEFT, padx=5)
    t_label3.pack(side=LEFT, padx=5)
    t_label4.pack(side=LEFT, padx=5)
    t_label5.pack(side=LEFT, padx=5)
    t_label6.pack(side=LEFT, padx=10)
    t_label7.pack(side=LEFT, padx=5)
    t_label8.pack(side=LEFT, padx=5)


# Функция для получения цены фиатной валюты
def exchange():
    target_name = combobox_target.get()
    target_code = target_name.upper()
    fi_coin = combobox_fiat.get()
    base_code = fiat[fi_coin].upper()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
#            print(data)
            update_time = data['time_last_update_unix']
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                fiat_price = f"{exchange_rate}"
                label_config(fi_coin, fiat_price, target_name, update_time)
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
    tg0 = combobox_target.get()
    target_name = target[tg0]
    tg1 = tg0.lower()

    # Настройка параметров запроса
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids,
        "vs_currencies": tg1,
        "include_last_updated_at": "true"
    }
    headers = {"Accepts": "application/json"}

    try:
        # Выполнение GET-запроса
        response = requests.get(url=url, params=params, headers=headers)

        # Обработка ответа
        if response.status_code == 200:
            data = response.json()
            update_time = data[ids]['last_updated_at']
            price = data[ids][tg1]
            crypt_price = f"{price:.2f}"

            # Добавление пробелов в многозначное число
            len1 = len(crypt_price)
            if len1 >6:
                ii = 6
                while ii <= len1:
                    crypt_price = crypt_price[:-ii] + ' ' + crypt_price[-ii:]
                    ii +=4
            label_config(cr_coin, crypt_price, target_name, update_time)
        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")

# ---------------------Создание графического интерфейса----------------------

window = Tk()
# window.iconbitmap('bitcoin.ico')
window.resizable(False, False)
window.attributes("-toolwindow", True)
window.title("Курсы ВАлют")
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

# Выбор фиатная или крипто-валюта
valutes = ["КриптоВАлюта", "Валюта"]
s_val = valutes[0]
selected_val = StringVar(value=valutes[0])


def select():
    global s_val
    s_val = selected_val.get()
    if s_val == valutes[0]:
        fiat_label.grid_forget()
        combobox_fiat.grid_forget()
        crypt_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        combobox_crypta.grid(row=0, column=1, padx=10, pady=10, sticky=EW)
    else:
        crypt_label.grid_forget()
        combobox_crypta.grid_forget()
        fiat_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        combobox_fiat.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

i = 0
for val in valutes:
    lang_btn = ttk.Radiobutton(f1, text=val, value=val, variable=selected_val, command=select)
    i += 1
    lang_btn.grid(row=i+1, column=0, padx=10, pady=5, sticky=EW)

# Выбор фиатной валюты
fiat_label = ttk.Label(f1, text="Валюта")
fiat_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
fiat = {
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

fiat1 = dict(list(fiat.items())[:])
fi = list(fiat1.keys())
fi_var = StringVar(value=fi[0])

combobox_fiat = ttk.Combobox(f1, textvariable = fi_var, values = fi,
                             state="readonly", width=28, height=20)
combobox_fiat.grid(row=0, column=1, padx=10, pady=10, sticky=EW)


# Выбор криптовалюты
crypt_label = ttk.Label(f1, text="КриптоВАлюта")
crypt_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
crypta = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Tether": "usdt",
    "Solana": "sol",
    "Ripple": "xrp",
    "Dogecoin": "doge",
    "Cardano": "ada",
    "Stellar": "xlm",
}

crypta1 = dict(list(crypta.items())[:])
cr = list(crypta1.keys())
cr_var = StringVar(value=cr[0])

combobox_crypta = ttk.Combobox(f1, textvariable = cr_var, values = cr,
                               state="readonly", width=28, height=20)
combobox_crypta.grid(row=0, column=1, padx=10, pady=10, sticky=EW)


# Выбор целевой валюты
target_label = ttk.Label(f1, text='К ВАлюте:')
target_label.grid(row=1, column=0, padx=10, pady=10, sticky=EW)
target = {
    "USD": "Долларов США",
    "Rub": "Рублей",
    "EUR": "Евро"
}
tg = list(target.keys())
tg_var = StringVar(value=tg[1])
combobox_target = ttk.Combobox(f1, textvariable=tg_var, values=tg, state="readonly")
combobox_target.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

# Получение курса
Button(f1, text="КВА", command=choice).grid(row=2, column=1, padx=10, pady=10, sticky=EW)

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
