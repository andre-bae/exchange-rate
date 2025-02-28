from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime, timedelta
import os
import sys
import base64

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from xml.etree import ElementTree

from list_all_coins import *

s_val = 0
fiat_cod = None
fiat_name = ''
plt.rcParams['toolbar'] = 'None'
multiplier = 1.0

# записываем полные пути к файлам картинок чтобы их засунуть в один ехе файл потом
def resource_path(relative_path):
    try:
        # noinspection PyProtectedMember
        base_path = sys._MEIPASS  # type: ignore
    except AttributeError:  # Перехватываем только AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --------------------Функция оформления вывода результата в метки------------------------

def label_config(money, price, name, time):
    t_label2.config(text=f"{datetime.now().strftime('%H часов %M минут    %d.%m.%Y')}")
    t_label4.config(text=f"{money}")
    t_label6.config(text=f" {price} ")
    t_label7.config(text=f" {name}")
    t_label8.config(text=f"( Последнее обновление курса: "
                         f"{datetime.fromtimestamp(time).strftime('%H:%M:%S %d.%m.%Y')} )")
    t_label1.pack(side=LEFT, padx=5)
    t_label2.pack(side=LEFT, padx=5)
    t_label3.pack(side=LEFT, padx=5)
    t_label4.pack(side=LEFT, padx=5)
    t_label6.pack(side=LEFT, padx=10)
    t_label7.pack(side=LEFT, padx=5)
    t_label8.pack(side=LEFT, padx=5)


# ----------------------Получение курса базовой валюты: крипта или фиатная валюта-----------------

def choice():
    global fiat_cod, fiat_name, multiplier
    label_frog.pack_forget()
    label_kva.pack_forget()
    if s_val:
        get_price()
        fiat_cod = None
        button_graf.pack(side=RIGHT, padx=5)
    else:
        exchange()
        for fit in list_fiat_FIAT:
            if fit.country == combobox_fiat.get():
                fiat_cod = fit.optional_history
                fiat_name = fit.text
                if combobox_target.get() == 'Rub' and fiat_cod is not None:
                    button_graf.pack(side=RIGHT, padx=5)
                break
            else:
                button_graf.pack_forget()


# ---------------------------Функция для получения цены фиатной валюты----------------------

def exchange():
    global multiplier
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
                multiplier = float(fiat_price)
            else:
                messagebox.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка: {e}")
    else:
        messagebox.showwarning("Внимание", "Выберите коды валют")


# ------------------------------Функция для получения цены криптовалюты----------------------

def get_price():
    global multiplier
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
            multiplier = float(price)

            # Добавление пробелов в многозначное число
            len1 = len(crypt_price)
            if len1 >6:
                ii = 6
                while ii <= len1:
                    crypt_price = crypt_price[:-ii] + ' ' + crypt_price[-ii:]
                    ii +=4
            label_config(cr_coin, crypt_price, target_name, update_time)

        else:
            messagebox.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")


# Функция для получения данных о курсе валюты к рублю за последний год
def get_currency_rate(currency_code):
    """
    Получает курс выбранной валюты к рублю за последний год.
    :param currency_code: Код валюты (например, 'R01235' для доллара, 'R01239' для евро).
    :return: Словарь с датами и курсами или None в случае ошибки.
    """
    try:
        # Определяем даты начала и конца периода
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        # URL API Центрального банка России
        url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date.strftime('%d/%m/%Y')}&date_req2={end_date.strftime('%d/%m/%Y')}&VAL_NM_RQ={currency_code}"

        # Отправляем запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, есть ли ошибки HTTP

        # Парсим XML-ответ
        root = ElementTree.fromstring(response.content)

        currency_rates = {}
        for record in root.findall('Record'):
            try:
                date = datetime.strptime(record.attrib['Date'], '%d.%m.%Y').date()
                rate = float(record.find('Value').text.replace(',', '.'))
                currency_rates[date] = rate
            except (ValueError, AttributeError, KeyError) as e:
                messagebox.showerror("Ошибка", f"Ошибка при обработке записи: {e}. Пропускаем запись.")
                continue

        return currency_rates

    except requests.exceptions.RequestException as e:
        # Обработка ошибок сети или HTTP
        messagebox.showerror("Ошибка", f"Ошибка при выполнении запроса: {e}")
        return None
    except ElementTree.ParseError as e:
        # Обработка ошибок парсинга XML
        messagebox.showerror("Ошибка", f"Ошибка при парсинге XML: {e}")
        return None
    except Exception as e:
        # Обработка всех остальных ошибок
        messagebox.showerror("Ошибка", f"Неожиданная ошибка: {e}")
        return None


# Функция для построения графика
def plot_currency_rate(dates, rates, currency_name):
    """
    Строит график курса валюты к рублю.
    :param dates: Список с датами.
    :param rates: Список с курсами.
    :param currency_name: Название валюты (например, 'USD/RUB' или 'EUR/RUB').
    """
    global multiplier

    # Создаем фигуру
    fig, ax = plt.subplots(figsize=(8, 4))

    # Убираем маркеры (параметр marker)
    ax.plot(dates, rates, label=currency_name, color='blue', linestyle='-')

    # Настраиваем сетку по месяцам
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xticks(rotation=45)

    # Включаем сетку для основных делений (месяцы)
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)

    # Заголовок графика
    ax.set_title(f'Курс {currency_name} за последний год', fontsize=16)

    multiplier = multiplier/rates[-1]
    if multiplier > 5 or multiplier < 0.5:
        # Если множитель есть, добавляем подпись над осью Y
        plt.ylabel(f'Курс (руб × {multiplier:.0e})', fontsize=14)
    else:
        # Если множителя нет, подпись остается без изменений
        plt.ylabel('Курс (руб)', fontsize=14)

    plt.tight_layout()
    plt.gcf().canvas.manager.set_window_title(f"График курса {currency_name}")


    # Обработчик закрытия окна
    def on_close(_):
        button_graf.pack_forget()

    # Подключаем обработчик события закрытия окна
    fig.canvas.mpl_connect('close_event', on_close)

    # Отображение графика
    plt.show()

# ------------------------------Функция получения данных для графика цены----------------------

def get_price_graf():
    global fiat_cod, fiat_name
    if fiat_cod is not None:
        try:
            # Получаем данные о курсе
            currency_rates = get_currency_rate(fiat_cod)
            dates = list(currency_rates.keys())
            rates = list(currency_rates.values())
            # Строим график
            plot_currency_rate(dates, rates, f"{fiat_name} к рублю")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        cr_coin = combobox_crypta.get()
        ids = cr_coin.lower()
        tg0 = combobox_target.get()
        tg1 = tg0.lower()
        days_graf = 365

        url = f"https://api.coingecko.com/api/v3/coins/{ids}/market_chart?vs_currency={tg1}&days={days_graf}"
        headers = {"accept": "application/json"}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()

                graf_time = [row[0] for row in data['prices']]
                dates = [datetime.fromtimestamp(ts / 1000).date() for ts in graf_time]
                rates = [row[1] for row in data['prices']]

                plot_currency_rate(dates, rates, f"{cr_coin} к рублю")
            else:
                if response.status_code == 429:
                    messagebox.showerror("Ошибка", f"Ошибка при получении данных: слишком много запросов!")
                else:
                    messagebox.showerror("Ошибка", f"Ошибка при получении данных: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении запроса: {e}")


# ---------------------Создание графического интерфейса----------------------

def quit1():
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
window.title("Актуальные Курсы ВАлют более 160 стран")
window.geometry("480x320")
window.protocol("WM_DELETE_WINDOW", lambda: quit1())

f1 = Frame(window, borderwidth=1, relief=SOLID)
f1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
f_button_graf = Frame(window)
f_button_graf.grid(row=1, rowspan=3, column=1, padx=10, pady=(0, 10), sticky="ne")
f2 = Frame(window)
f2.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nw")
f3 = Frame(window)
f3.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nw")
f4 = Frame(window)
f4.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="nw")
f5 = Frame(window)
f5.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="ew")

# Настройка растягивания столбцов и строк
window.grid_columnconfigure(0, weight=1)  # Левый столбец (фреймы f2-f4) растягивается
window.grid_columnconfigure(1, weight=0)  # Правый столбец (кнопка) не растягивается
window.grid_rowconfigure(1, weight=1)     # Строки растягиваются
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

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


# --------------------------Кнопка получения курса----------------------------------------------

def button_kva_enter(_):
    global img_hover_kva
    button_kva.config(image=img_hover_kva)  # type: ignore


def button_kva_leave(_):
    global img_kva
    button_kva.config(image=img_kva)  # type: ignore

img_kva = ImageTk.PhotoImage(Image.open(resource_path("btn_kva3.gif")))
img_hover_kva = ImageTk.PhotoImage(Image.open(resource_path("btn_kva4.gif")))
button_kva = Button(f1, image=img_kva, command=choice, relief='flat', borderwidth=0)  # type: ignore
button_kva.grid(row=2, column=2, padx=10, sticky=E)
button_kva.bind("<Enter>", button_kva_enter)
button_kva.bind("<Leave>", button_kva_leave)

t_label1 = ttk.Label(f2, text='На ', font="Helvetica 10")
t_label2 = ttk.Label(f2, text='', font="Helvetica 10 bold")
t_label3 = ttk.Label(f3, text='Курс ', font="Helvetica 10")
t_label4 = ttk.Label(f3, text='', font="Helvetica 10 bold")
t_label6 = ttk.Label(f4, text='', font="Helvetica 14 bold",
                     foreground='Red', background='White', borderwidth=1, relief=SOLID)
t_label7 = ttk.Label(f4, text='', font="Helvetica 10 bold")
t_label8 = ttk.Label(f5, text='')


# ----------------------Кнопка получения графика криптовалюты------------------------------

def button_graf_enter(_):
    global img_hover_graf
    button_graf.config(image=img_hover_graf)  # type: ignore


def button_graf_leave(_):
    global img_graf
    button_graf.config(image=img_graf)  # type: ignore


img_graf = ImageTk.PhotoImage(Image.open(resource_path("btn_graf3.gif")))
img_hover_graf = ImageTk.PhotoImage(Image.open(resource_path("btn_graf4.gif")))
button_graf = Button(f_button_graf, image=img_graf, command=get_price_graf, borderwidth=3)  # type: ignore
button_graf.bind("<Enter>", button_graf_enter)
button_graf.bind("<Leave>", button_graf_leave)


# ------------------------------Загрузка лягушки------------------------------

frog = Image.open(resource_path("frog4.gif"))
frog_tk = ImageTk.PhotoImage(frog)
label_frog = Label(f_button_graf, image=frog_tk)  # type: ignore
label_frog.pack(side=RIGHT)

kva = Image.open(resource_path("kva2.gif"))
kva_tk = ImageTk.PhotoImage(kva)
label_kva = Label(f2, image=kva_tk)  # type: ignore
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
            file = filedialog.askopenfilename(
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
            messagebox.showerror("Ошибка", "Файл не найден")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


    def save_coins():
        try:
            file = filedialog.asksaveasfilename(
                initialfile="default",  # Предлагаемое имя файла
                defaultextension=".kva",  # Расширение по умолчанию
                filetypes=[("KBA файлы", "*.kva"),  # Допустимые типы файлов
                           ("Все файлы", "*.*")])
            if file:  # Проверяем, выбран ли файл
                with open(file, 'w') as f:
                    f.write('\n'.join(list_fiat))
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Не удалось сохранить файл")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# ---------------------------------геометрия всплывающего окна настройки---------------

    wind_select = Toplevel()
    wind_select.title("Выбор валют")
    wind_select.geometry("730x300")
    wind_select.grab_set()
    wind_select.protocol("WM_DELETE_WINDOW", lambda: cancel_wind_select())
    wind_select.resizable(False, True)

    wind_select.rowconfigure(0, weight=1)
    wind_select.rowconfigure(1, weight=1)
    wind_select.rowconfigure(2, weight=1)
    wind_select.rowconfigure(3, weight=1)

    ttk.Button(wind_select, text="Добавить", command=add_fiat).grid(row=0, column=2, padx=6, pady=6)
    ttk.Button(wind_select, text="Удалить", command=delete).grid(row=0, column=7, padx=5, pady=5)
    ttk.Button(wind_select, text="▲", command=up_step).grid(row=1, column=7, padx=5, pady=5)
    ttk.Button(wind_select, text="▼", command=down_step).grid(row=2, column=7, padx=5, pady=5)
    ttk.Button(wind_select, text="Очистить", command=del_all).grid(row=3, column=7, padx=5, pady=5)
    ttk.Button(wind_select, text="Ok", command=ok_wind_select).grid(row=4, column=3, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Загрузить", command=load_coins).grid(row=4, column=4, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Сохранить", command=save_coins).grid(row=4, column=5, sticky=S, padx=5, pady=5)
    ttk.Button(wind_select, text="Cancel", command=cancel_wind_select).grid(row=4, column=7, sticky=S, padx=5, pady=5)

    fiat_all_var = Variable(value=list_fiat_all_country)
    fiat_all_listbox = Listbox(wind_select, listvariable=fiat_all_var, width=41)
    fiat_all_listbox.grid(row=0, column=0, rowspan=5, sticky=NS, padx=(10,0), pady=(5,10))
    scrollbar_all = Scrollbar(wind_select, orient="vertical", command=fiat_all_listbox.yview)
    scrollbar_all.grid(row=0, column=1, rowspan=5, sticky=NS, pady=(5, 10))
    fiat_all_listbox.config(yscrollcommand=scrollbar_all.set)

    fiat_var = Variable(value=list_fiat)
    fiat_listbox = Listbox(wind_select, listvariable=fiat_var, width=35, selectmode="single")
    fiat_listbox.grid(row=0, column=3, rowspan=4, columnspan=3, sticky=NSEW, padx=5, pady=5)
    scrollbar = Scrollbar(wind_select, orient="vertical", command=fiat_listbox.yview)
    scrollbar.grid(row=0, column=6, rowspan=5, sticky=NS, pady=(5, 10))
    fiat_listbox.config(yscrollcommand=scrollbar.set)


# ------------------------------------Кнопка настройки-----------------------------

def settings_enter(_):
    global img_hover_settings
    button_settings.config(image=img_hover_settings)  # type: ignore


def settings_leave(_):
    global img_settings
    button_settings.config(image=img_settings)  # type: ignore

img_settings = ImageTk.PhotoImage(Image.open(resource_path("settings1.gif")))
img_hover_settings = ImageTk.PhotoImage(Image.open(resource_path("settings2.gif")))
button_settings = Button(f1, image=img_settings, command=select_fiat_coins, relief='flat', borderwidth=0)  # type: ignore
button_settings.grid(row=0, column=0, padx=(0,5), sticky=E)
button_settings.bind("<Enter>", settings_enter)
button_settings.bind("<Leave>", settings_leave)

# --------------------------- загрузка default.kva ----------------------

file_name = 'default.kva'
file_path = os.path.join(os.path.dirname(__file__), file_name)
try:
    if os.path.exists(file_path):
        list_test = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                list_test.extend(f.read().split('\n'))
        if len(list_test) > 0:
            list_fiat_FIAT.clear()
            for fiat in list_test:
                for coins in list_fiat_all_FIAT:
                    if fiat == coins.country:
                        list_fiat_FIAT.append(coins)
            f_i = list(map(lambda p: p.country, list_fiat_FIAT))
            combobox_fiat['values'] = f_i
            combobox_fiat.current(0)
            fi_var.set(combobox_fiat['values'][0])
except Exception as exc:
    messagebox.showerror("Ошибка", f"Произошла ошибка: {exc}")

window.mainloop()
