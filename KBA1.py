import tkinter as tk
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from list_all_coins import *


# записываем полные пути к файлам картинок чтобы их засунуть в один ехе файл потом
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

s_val = 0


# --------------------Функция оформления вывода результата в метки------------------------

def label_config(money, price, name, time):
    t_label2.config(text=f"{dt.now().strftime('%H часов %M минут    %d.%m.%Y')}")
    t_label4.config(text=f"{money}")
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


# ---------------------------Функция для получения цены фиатной валюты----------------------

def exchange():
    target_name = combobox_target.get()
    target_code = target_name.upper()
    fi_coin = combobox_fiat.get()
    base_code = ''
    coin_name = ''
    for fit in list_fiat_FIAT:
        if fit.country == fi_coin:
            base_code = fit.cod.upper()
            coin_name = fit.text

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            update_time = data['time_last_update_unix']
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                fiat_price = f"{exchange_rate}"
                label_config(coin_name, fiat_price, target_name, update_time)
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


# ------------------------------Функция для получения цены криптовалюты----------------------

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
        response = requests.get(url=url, params=params, headers=headers)

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


# ------------------------------Функция для графика цены криптовалюты----------------------

def get_price_graf():
    cr_coin = combobox_crypta.get()
    ids = cr_coin.lower()
    tg0 = combobox_target.get()
    tg1 = tg0.lower()
    days_graf = 365

    url = f"https://api.coingecko.com/api/v3/coins/{ids}/market_chart?vs_currency={tg1}&days={days_graf}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)


        def unix_to_readable(unix_time):
            return dt.fromtimestamp(unix_time / 1000).strftime('%d.%m')

        if response.status_code == 200:
            data = response.json()

            graf_time = [row[0] for row in data['prices']]
            readable_times = [unix_to_readable(time) for time in graf_time]

            graf_price = [row[1] for row in data['prices']]

            x = np.array(readable_times)
            y = np.array(graf_price)
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_title(f'График курса {cr_coin} к {tg0} за {days_graf} дней')
            ax.set_xlabel('Даты')
            ax.set_ylabel(f'Курс {cr_coin} к {tg0}')
            x_ticks = np.arange(0, days_graf, days_graf//12)
            ax.set_xticks(x_ticks)
            ax.grid(True)


#            def cancel_wind_graf():
#                plt.close(fig)
#                wind_graf.grab_release()
#                wind_graf.destroy()
#                button_graf.pack_forget()

#            wind_graf = Toplevel()
#            wind_graf.title(f"График курса {cr_coin}")
#            wind_graf.geometry("1000x400")
#            wind_graf.grab_set()
#            wind_graf.protocol("WM_DELETE_WINDOW", lambda: cancel_wind_graf())

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            mb.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")

    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")


# ---------------------Создание графического интерфейса----------------------

def quit1():
    plt.close(fig)
    window.destroy()

# Преобразование иконки в base64
with open(resource_path("frog2.ico"), 'rb') as image:
    binary_icon = base64.b64encode(image.read())

# Использование иконки при запуске и в папке и на рабочем столе (после перезагрузки)
with open(resource_path("frog2.ico"), 'wb') as image:
    image.write(base64.b64decode(binary_icon))

window = Tk()
window.iconbitmap(resource_path("frog2.ico"))
window.resizable(False, False)
# window.attributes("-toolwindow", True)
window.title("Актуальные Курсы ВАлют более 160 стран")
window.geometry("480x300")
window.protocol("WM_DELETE_WINDOW", lambda: quit1())

f1 = Frame(window, borderwidth=1, relief=SOLID)
f1.pack(padx=10)
f2 = Frame(window)
f2.pack(fill=BOTH, expand=True, anchor=NW, padx=10, pady=(10,0))
f3 = Frame(window)
f3.pack(fill=BOTH, expand=True, anchor=NW, padx=10)
f4 = Frame(window)
f4.pack(fill=BOTH, expand=True, anchor=NW, padx=10, pady=5)
f5 = Frame(window)
f5.pack(fill=BOTH, expand=True, anchor=NW, padx=10)

# ------------------------------Выбор криптовалюты------------------------------

crypt_label = ttk.Label(f1, text="КриптоВАлюта", width=14)

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
                               state="readonly", width=40, height=20)
combobox_crypta.grid(row=0, column=2, padx=10, pady=5, sticky=EW)

# ---------------------------Выбор фиатной валюты-------------------------------

f_text = "Валюта".rjust(20)
fiat_label = ttk.Label(f1, text=f_text, width=14)
fiat_label.grid(row=0, column=1, padx=10, pady=5, sticky=E)
fi = list(map(lambda p: p.country, list_fiat_FIAT))
fi_var = StringVar(value=fi[0])

combobox_fiat = ttk.Combobox(f1, textvariable = fi_var, values = fi,
                             state="readonly", width=40, height=20)
combobox_fiat.grid(row=0, column=2, padx=10, pady=5, sticky=EW)

# ----------------Выбор целевой валюты---------------------------------------

target_label = ttk.Label(f1, text='К ВАлюте:')
target_label.grid(row=1, column=1, padx=10, pady=5, sticky=E)
target = {
    "USD": "Долларов США",
    "Rub": "Рублей",
    "EUR": "Евро"
}
tg = list(target.keys())
tg_var = StringVar(value=tg[1])

combobox_target = ttk.Combobox(f1, textvariable=tg_var, values=tg, state="readonly")
combobox_target.grid(row=1, column=2, padx=10, pady=5, sticky=EW)


# ----------------------------Чекбокс выбора фиатная или крипто-валюта-----------------------

def select():
     global s_val
     if check_crypta.get() == 1:
        s_val = 1
        fiat_label.grid_forget()
        combobox_fiat.grid_forget()
        crypt_label.grid(row=0, column=1, padx=10, pady=5, sticky=E)
        combobox_crypta.grid(row=0, column=2, padx=10, pady=5, sticky=EW)
     else:
        s_val = 0
        crypt_label.grid_forget()
        combobox_crypta.grid_forget()
        fiat_label.grid(row=0, column=1, padx=10, pady=5, sticky=E)
        combobox_fiat.grid(row=0, column=2, padx=10, pady=5, sticky=EW)

check_crypta = IntVar()
enabled_checkbutton = Checkbutton(f1, text="КриптоВАлюта", variable=check_crypta, command=select)
enabled_checkbutton.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=EW)


# ----------------------Получение курса базовой валюты: крипта или фиатная валюта-----------------

def choice():
    label_frog.pack_forget()
    label_kva.pack_forget()
    if s_val:
        get_price()
        button_graf.pack(side=RIGHT, padx=5)
    else:
        exchange()
        button_graf.pack_forget()


# Кнопка получения курса

def button_kva_enter(event):
    global img_hover_kva
    button_kva.config(image=img_hover_kva)


def button_kva_leave(event):
    global img_kva
    button_kva.config(image=img_kva)

img_kva = ImageTk.PhotoImage(Image.open(resource_path("btn_kva3.gif")))
img_hover_kva = ImageTk.PhotoImage(Image.open(resource_path("btn_kva4.gif")))
button_kva = Button(f1, image=img_kva, command=choice, relief='flat', borderwidth=0)
button_kva.grid(row=2, column=2, padx=10, sticky=E)
button_kva.bind("<Enter>", button_kva_enter)
button_kva.bind("<Leave>", button_kva_leave)

t_label1 = ttk.Label(f2, text='На ', font="Helvetica 10")
t_label2 = ttk.Label(f2, text='', font="Helvetica 10 bold")
t_label3 = ttk.Label(f3, text='Текущий курс ', font="Helvetica 10")
t_label4 = ttk.Label(f3, text='', font="Helvetica 10 bold")
t_label5 = ttk.Label(f3, text=' составляет  ', font="Helvetica 10")
t_label6 = ttk.Label(f4, text='', font="Helvetica 14 bold",
                     foreground='Red', background='White', borderwidth=1, relief=SOLID)
t_label7 = ttk.Label(f4, text='', font="Helvetica 10 bold")
t_label8 = ttk.Label(f5, text='')


# Кнопка получения графика криптовалюты

def button_graf_enter(event):
    global img_hover_graf
    button_graf.config(image=img_hover_graf)


def button_graf_leave(event):
    global img_graf
    button_graf.config(image=img_graf)


img_graf = ImageTk.PhotoImage(Image.open(resource_path("btn_graf1.jpg")))
img_hover_graf = ImageTk.PhotoImage(Image.open(resource_path("btn_graf2.jpg")))
button_graf = Button(f2, image=img_graf, command=get_price_graf, borderwidth=3)
button_graf.bind("<Enter>", button_graf_enter)
button_graf.bind("<Leave>", button_graf_leave)

# ------------------------------Загрузка лягушки------------------------------

frog = Image.open(resource_path("frog4.gif"))
# frog = frog.resize((150, 150))
frog_tk = ImageTk.PhotoImage(frog)
label_frog = Label(window, image=frog_tk)
label_frog.pack(side=RIGHT)

kva = Image.open(resource_path("kva2.gif"))
kva_tk = ImageTk.PhotoImage(kva)
label_kva = Label(window, image=kva_tk)
label_kva.pack(side=LEFT)


# ----------------------------------------Настройка списка фиатных валют----------------

def select_fiat_coins():

    list_fiat = []
    for money in list_fiat_FIAT:
        list_fiat.append(money.country)


    # добавление нового элемента
    def add_fiat():
        s = fiat_all_listbox.curselection()
        if len(s) == 1:
            s = s[0]
            new_fiat = fiat_all_listbox.get(s)
            if new_fiat not in list_fiat:
                list_fiat.append(new_fiat)
                fiat_var.set(list_fiat)


    # удаление выделенного элемента
    def delete():
        s = fiat_listbox.curselection()
        if len(s) == 1:
            list_fiat.pop(s[0])
            fiat_var.set(list_fiat)


    # очистка списка выбранных валют
    def del_all():
        list_fiat.clear()
        fiat_var.set(list_fiat)


    def up_step():
        s = fiat_listbox.curselection()
        if len(s) == 1:
            s = s[0]
            list_fiat[s-1:s+1] = list_fiat[s-1:s+1][::-1]
            fiat_var.set(list_fiat)
            fiat_listbox.selection_clear(0, END)
            fiat_listbox.selection_set(s-1)


    def down_step():
        s = fiat_listbox.curselection()
        if len(s) == 1:
            s = s[0]
            list_fiat[s:s+2] = list_fiat[s:s+2][::-1]
            fiat_var.set(list_fiat)
            fiat_listbox.selection_clear(0, END)
            fiat_listbox.selection_set(s+1)


    def cancel_wind_select():
        wind_select.grab_release()
        wind_select.destroy()


    def ok_wind_select():
        list_fiat_FIAT.clear()
        for fiat in list_fiat:
            for coins in list_fiat_all_FIAT:
                if fiat == coins.country:
                    list_fiat_FIAT.append(coins)
        f_i = list(map(lambda p: p.country, list_fiat_FIAT))
        combobox_fiat['values'] = f_i
        combobox_fiat.current(0)
        fi_var.set(combobox_fiat['values'][0])
        cancel_wind_select()


    def load_coins():
        try:
            file = fd.askopenfilename(
                defaultextension=".kva",
                filetypes=[("KBA файлы", "*.kva"), ("Все файлы", "*.*")]
            )
            list_test = []
            if file:
                with open(file, 'r') as f:
                    list_test.extend(f.read().split('\n'))
            if len(list_test) > 0:
                list_fiat.clear()
                for fiat in list_test:
                    for coins in list_fiat_all_FIAT:
                        if fiat == coins.country:
                            list_fiat.append(fiat)
                fiat_var.set(list_fiat)
        except FileNotFoundError:
            mb.showerror("Ошибка", "Файл не найден")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")


    def save_coins():
        try:
            file = fd.asksaveasfilename(
                initialfile="my_coins",  # Предлагаемое имя файла
                defaultextension=".kva",  # Расширение по умолчанию
                filetypes=[("KBA файлы", "*.kva"),  # Допустимые типы файлов
                           ("Все файлы", "*.*")])
            if file:  # Проверяем, выбран ли файл
                with open(file, 'w') as f:
                    f.write('\n'.join(list_fiat))
        except FileNotFoundError:
            mb.showerror("Ошибка", "Не удалось сохранить файл")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")

# ---------------------------------геометрия всплывающего окна настройки---------------

    wind_select = Toplevel()
    wind_select.title("Выбор валют")
    wind_select.geometry("700x300")
    wind_select.grab_set()
    wind_select.protocol("WM_DELETE_WINDOW", lambda: cancel_wind_select())
    wind_select.resizable(False, True)

    wind_select.rowconfigure(0, weight=1)
    wind_select.rowconfigure(1, weight=1)
    wind_select.rowconfigure(2, weight=1)
    wind_select.rowconfigure(3, weight=1)
 #   wind_select.rowconfigure(4, weight=1)

    ttk.Button(wind_select, text="Добавить", command=add_fiat).grid(row=0, column=1, padx=6, pady=6)
    ttk.Button(wind_select, text="Удалить", command=delete).grid(row=0, column=5, padx=5, pady=5)
    ttk.Button(wind_select, text="▲", command=up_step).grid(row=1, column=5, padx=5, pady=5)
    ttk.Button(wind_select, text="▼", command=down_step).grid(row=2, column=5, padx=5, pady=5)
    ttk.Button(wind_select, text="Очистить", command=del_all).grid(row=3, column=5, padx=5, pady=5)
    ttk.Button(wind_select, text="Ok", command=ok_wind_select).grid(row=4, column=2, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Загрузить", command=load_coins).grid(row=4, column=3, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Сохранить", command=save_coins).grid(row=4, column=4, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Cancel", command=cancel_wind_select).grid(row=4, column=5, sticky=S, padx=5, pady=5)

    fiat_all_var = Variable(value=list_fiat_all_country)
    fiat_all_listbox = Listbox(wind_select, listvariable=fiat_all_var, width=41)
    fiat_all_listbox.grid(row=0, column=0, rowspan=5, sticky=NS, padx=(10,5), pady=(5,10))

    fiat_var = Variable(value=list_fiat)
    fiat_listbox = Listbox(wind_select, listvariable=fiat_var, width=35, selectmode="single")
    fiat_listbox.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=NSEW, padx=5, pady=5)


# ------------------------------------Кнопка настройки-----------------------------

def settings_enter(event):
    global img_hover_settings
    button_settings.config(image=img_hover_settings)


def settings_leave(event):
    global img_settings
    button_settings.config(image=img_settings)

img_settings = ImageTk.PhotoImage(Image.open(resource_path("settings.gif")))
img_hover_settings = ImageTk.PhotoImage(Image.open(resource_path("settings2.gif")))
button_settings = Button(f1, image=img_settings, command=select_fiat_coins, relief='flat', borderwidth=0)
button_settings.grid(row=0, column=0, padx=(0,5), sticky=E)
button_settings.bind("<Enter>", settings_enter)
button_settings.bind("<Leave>", settings_leave)

window.mainloop()
