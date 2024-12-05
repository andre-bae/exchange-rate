# from tkinter import *
# from tkinter import ttk

# from list_all_coins import *


def select_fiat_coins():

    list_fiat = []

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
            for money in list_fiat_all_FIAT:
                if fiat == money.country:
                    list_fiat_FIAT.append(money)
        cancel_wind_select()


    wind_select = Toplevel()
    wind_select.title("Выбор валют")
    wind_select.geometry("630x250")
    wind_select.protocol("WM_DELETE_WINDOW", lambda: cancel_wind_select())

    ttk.Button(wind_select, text="Добавить", command=add_fiat).grid(row=0, column=1, padx=6, pady=6)

    ttk.Button(wind_select, text="Удалить", command=delete).grid(row=0, column=3, padx=5, pady=5)

    ttk.Button(wind_select, text="▲", command=up_step).grid(row=1, column=3, padx=5, pady=5)

    ttk.Button(wind_select, text="▼", command=down_step).grid(row=2, column=3, padx=5, pady=5)

    ttk.Button(wind_select, text="Очистить", command=del_all).grid(row=3, column=3, padx=5, pady=5)

    ttk.Button(wind_select, text="Ok", command=ok_wind_select).grid(row=4, column=2, padx=5, pady=5)

    ttk.Button(wind_select, text="Cancel", command=cancel_wind_select).grid(row=4, column=3, padx=5, pady=5)

    fiat_all_var = Variable(value=list_fiat_all_country)
    fiat_all_listbox = Listbox(wind_select, listvariable=fiat_all_var, width=35)
    fiat_all_listbox.grid(row=0, column=0, rowspan=4, sticky=EW, padx=5, pady=5)

    fiat_var = Variable(value=list_fiat)
    fiat_listbox = Listbox(wind_select, listvariable=fiat_var, width=35, selectmode="single")
    fiat_listbox.grid(row=0, column=2, rowspan=4, sticky=EW, padx=5, pady=5)

#    wind_select.mainloop()
