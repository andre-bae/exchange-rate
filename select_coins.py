# from tkinter import *
# from tkinter import ttk

class FIAT:
    def __init__(self, country, cod, text):
        self.country = country
        self.cod = cod
        self.text = text
list_fiat_all = [
    FIAT("ОАЭ", "AED", "дирхама ОАЭ"),
    FIAT("Афганистана", "AFN", "афганского афгани"),
    FIAT("Албании", "ALL", "албанского лека"),
    FIAT("Армении", "AMD", "армянского драма"),
    FIAT("Антильских о-в (Нидерланды)", "ANG", "нидерландского антильского гульдена"),
    FIAT("Анголы", "AOA", "ангольской кванзи"),
    FIAT("Аргентины", "ARS", "аргентинского песо"),
    FIAT("Австралии", "AUD", "австралийского доллара"),
    FIAT("Арубы (Нидерланды)", "AWG", "арубанского флорина"),
    FIAT("Азербайджана", "AZN", "азербайджанского маната"),
    FIAT("Боснии и Герцеговины", "BAM", "марки Боснии и Герцеговины"),
    FIAT("Барбадоса", "BBD", "барбадосского доллара"),
    FIAT("Бангладеш", "BDT", "бангладешской таки"),
    FIAT("Болгарии", "BGN", "болгарского лева"),
    FIAT("Бахрейна", "BHD", "бахрейнского динара"),
    FIAT("Бурунди", "BIF", "бурундийского франка"),
    FIAT("Бермудских о-в", "BMD", "бермудского доллара"),
    FIAT("Брунея", "BND", "брунейского доллара"),
    FIAT("Боливии", "BOB", "боливийского боливиано"),
    FIAT("Бразилии", "BRL", "бразильского реала"),
    FIAT("Багамских о-в", "BSD", "багамского доллара"),
    FIAT("Бутана", "BTN", "бутанского нгултрума"),
    FIAT("Ботсваны", "BWP", "ботсванского пула"),
    FIAT("Белоруссии", "BYN", "белорусского рубля"),
    FIAT("Белиза", "BZD", "белизского доллара"),
    FIAT("Канады", "CAD", "канадского доллара"),
    FIAT("Конго", "CDF", "конголезского франка"),
    FIAT("Швейцарии", "CHF", "швейцарского франка"),
    FIAT("Чили", "CLP", "чилийского песо"),
    FIAT("Китая", "CNY", "китайского юаня"),
    FIAT("Колумбии", "COP", "колумбийского песо"),
    FIAT("Коста-рики", "CRC", "коста-риканского колона"),
    FIAT("Кубы", "CUP", "кубинского песо"),
    FIAT("Кабо-Верде", "CVE", "эскудо Кабо-Верде"),
    FIAT("Чехии", "CZK", "чешской кроны"),
    FIAT("Джибути", "DJF", "франка Джибути"),
    FIAT("Дании", "DKK", "датской кроны"),
    FIAT("Доминиканы", "DOP", "доминиканского песо"),
    FIAT("Алжира", "DZD", "алжирского динара"),
    FIAT("Египта", "EGP", "египетского фунта"),
    FIAT("Эритреи", "ERN", "эритрейской накфы"),
    FIAT("Эфиопии", "ETB", "эфиопского быра"),
    FIAT("Евросоюза", "EUR", "евро"),
    FIAT("Фиджи", "FJD", "доллара Фиджи"),
    FIAT("Фолклендских о-в", "FKP", "фунта Фолклендских островов"),
    FIAT("Фарерских о-в", "FOK", "фарерской кроны"),
    FIAT("Великобритании", "GBP", "британского фунта стерлингов"),
    FIAT("Грузии", "GEL", "грузинского лари"),
    FIAT("Гернси", "GGP", "фунта Гернси"),
    FIAT("Ганы", "GHS", "ганского седи"),
    FIAT("Гибралтара", "GIP", "гибралтарского фунта"),
    FIAT("Гамбии", "GMD", "гамбийский даласи"),
    FIAT("Гвинеи", "GNF", "гвинейского франка"),
    FIAT("Гватемалы", "GTQ", "гватемальского кетцаля"),
    FIAT("Гайаны", "GYD", "гайанского доллара"),
    FIAT("Гонконга", "HKD", "гонконгского доллара"),
    FIAT("Гондураса", "HNL", "гондурасской лемпиры"),
    FIAT("Хорватии", "HRK", "хорватской куны"),
    FIAT("Гаити", "HTG", "гаитянского гурда"),
    FIAT("Венгрии", "HUF", "венгерского форинта"),
    FIAT("Индонезии", "IDR", "индонезийской рупии"),
    FIAT("Израиля", "ILS", "нового израильского шекеля"),
    FIAT("острова Мэн", "IMP", "мэнского фунта"),
    FIAT("Индии", "INR", "индийской рупии"),
    FIAT("Ирака", "IQD", "иракского динара"),
    FIAT("Ирана", "IRR", "иранского риала"),
    FIAT("Исландии", "ISK", "исландской кроны"),
    FIAT("Джерси", "JEP", "Джерси паунда"),
    FIAT("Ямайки", "JMD", "ямайского доллара"),
    FIAT("Иордании", "JOD", "иорданского динара"),
    FIAT("Японии", "JPY", "японской йены"),
    FIAT("Кении", "KES", "кенийского шиллинга"),
    FIAT("Киргизии", "KGS", "киргизского сома"),
    FIAT("Камбоджи", "KHR", "камбоджийского риеля"),
    FIAT("Кирибати","KID", "доллара Кирибати"),
    FIAT("Коморских о-в", "KMF", "коморского франка"),
    FIAT("Южной Кореи", "KRW", "южнокорейской воны"),
    FIAT("Кувейта", "KWD", "кувейтского динара"),
    FIAT("Каймановых о-в", "KYD", "доллара Каймановых островов"),
    FIAT("Казахстана", "KZT", "казахстанского тенге"),
    FIAT("Лаоса", "LAK", "лаосского кипа"),
    FIAT("Ливана", "LBP", "ливанского фунта"),
    FIAT("Шри-ланки", "LKR", "шри-ланкийской рупии"),
    FIAT("Либерии", "LRD", "либерийского доллара"),
    FIAT("Лесото", "LSL", "Лесото лоти"),
    FIAT("Ливии", "LYD", "ливийского динара"),
    FIAT("Марокко", "MAD", "марокканского дирхама"),
    FIAT("Молдавии", "MDL", "молдавского лея"),
    FIAT("Мадагаскара", "MGA", "малагасийского ариари"),
    FIAT("Македонии", "MKD", "македонского денара"),
    FIAT("Бирмы", "MMK", "бирманского кьята"),
    FIAT("Монголии", "MNT", "монгольского тогрога"),
    FIAT("Макао", "MOP", "патака Макао"),
    FIAT("Мавритании", "MRU", "мавританской угии"),
    FIAT("острова Маврикий", "MUR", "маврикийской рупии"),
    FIAT("Мальдивов", "MVR", "мальдивской руфии"),
    FIAT("Малави", "MWK", "малавийской квачи"),
    FIAT("Мексики", "MXN", "мексиканского песо"),
    FIAT("Малайзии", "MYR", "малазийского ринггита"),
    FIAT("Мозамбика", "MZN", "мозамбикского метикала"),
    FIAT("Намибии", "NAD", "намибийского доллара"),
    FIAT("Нигерии", "NGN", "нигерийского найра"),
    FIAT("Никарагуа", "NIO", "никарагуанского кордова"),
    FIAT("Норвегии", "NOK", "норвежской кроны"),
    FIAT("Непала", "NPR", "непальской рупии"),
    FIAT("Новой Зеландии", "NZD", "новозеландского доллара"),
    FIAT("Омана", "OMR", "оманского риала"),
    FIAT("Панамы", "PAB", "панамского бальбоа"),
    FIAT("Перу", "PEN", "перуанского сольи"),
    FIAT("Папуа-Новая Гвинея", "PGK", "кина Папуа-Новая Гвинея"),
    FIAT("Филиппин", "PHP", "филиппинского песо"),
    FIAT("Пакистана", "PKR", "пакистанской рупии"),
    FIAT("Польши", "PLN", "польского злотого"),
    FIAT("Парагвая", "PYG", "парагвайского гуарани"),
    FIAT("Катара", "QAR", "катарского риала"),
    FIAT("Румынии", "RON", "румынского лея"),
    FIAT("Сербии", "RSD", "сербского динара"),
    FIAT("России", "RUB", "российского рубля"),
    FIAT("Руанды", "RWF", "руандийского франка"),
    FIAT("Саудовской Аравии", "SAR", "саудовского рияла"),
    FIAT("Соломоновых о-в", "SBD", "доллара Соломоновых островов"),
    FIAT("Сейшельских о-в", "SCR", "сейшельской рупии"),
    FIAT("Судана", "SDG", "суданского фунта"),
    FIAT("Швеции", "SEK", "шведской кроны"),
    FIAT("Сингапура", "SGD", "сингапурского доллара"),
    FIAT("острова Святой Елены", "SHP", "фунта острова Святой Елены"),
    FIAT("Сьерра-Леоне", "SLE", "леоне Сьерра-Леоне"),
    FIAT("Сомали", "SOS", "сомалийского шиллинга"),
    FIAT("Суринама", "SRD", "суринамского доллара"),
    FIAT("Южного Судана", "SSP", "южносуданского фунта"),
    FIAT("Сан-Томе и Принсипи", "STN", "добра Сан-Томе и Принсипи"),
    FIAT("Сирии", "SYP", "сирийского фунта"),
    FIAT("Лилангени", "SZL", "эсватини Лилангени"),
    FIAT("Тайланда", "THB", "тайского бата"),
    FIAT("Таджикстана", "TJS", "таджикского сомони"),
    FIAT("Туркменистана", "TMT", "туркменского маната"),
    FIAT("Туниса", "TND", "тунисского динара"),
    FIAT("Тонго", "TOP", "тонганского паанга"),
    FIAT("Турции", "TRY", "турецкой лиры"),
    FIAT("Тринидада и Тобаго", "TTD", "доллара Тринидада и Тобаго"),
    FIAT("Тувалу", "TVD", "доллара Тувалу"),
    FIAT("Тайваня", "TWD", "нового тайваньского доллара"),
    FIAT("Танзании", "TZS", "танзанийского шиллинга"),
    FIAT("Украины", "UAH", "украинской гривны"),
    FIAT("Уганды", "UGX", "угандийского шиллинга"),
    FIAT("США", "USD", "американского доллара"),
    FIAT("Уругвая", "UYU", "уругвайского песо"),
    FIAT("Узбекистана", "UZS", "узбекского сума"),
    FIAT("Венесуэлы", "VES", "венесуэльского боливара соберано"),
    FIAT("Вьетнама", "VND", "вьетнамского донга"),
    FIAT("Вануату", "VUV", "вату Вануату"),
    FIAT("Самоа", "WST", "самоанской талы"),
    FIAT("Центральной Африки", "XAF", "центральноафриканского франка КФА"),
    FIAT("Организации Восточно-Карибских государств", "XCD", "восточно-карибского доллара"),
    FIAT("Специальных прав заимствования", "XDR", "специальных прав заимствования"),
    FIAT("Африканского финансового сообщества", "XOF", "западноафриканского франка КФА"),
    FIAT("французских общин Тихого океана", "XPF", "франка КФП"),
    FIAT("Йемена", "YER", "йеменского риала"),
    FIAT("Южно-Африканской Республики", "ZAR", "южноафриканского рэнда"),
    FIAT("Замбии", "ZMW", "замбийской квачи"),
    FIAT("Зимбабве", "ZWL", "зимбабвийского доллара")
]

dict_fiat_all = {
    "Дирхам ОАЭ": "AED",
    "Афганский афгани": "AFN",
    "Албанский лек": "ALL",
    "Армянский драм": "AMD",
    "Нидерландский антильский гульден": "ANG",
    "Ангольская кванза": "AOA",
    "Аргентинское песо": "ARS",
    "Австралийский доллар": "AUD",
    "Арубанский Флорин": "AWG",
    "Азербайджанский манат": "AZN",
    "Марка Боснии и Герцеговины": "BAM",
    "Барбадосский доллар": "BBD",
    "Бангладешская така": "BDT",
    "Болгарский лев": "BGN",
    "Бахрейнский динар": "BHD",
    "Бурундийский франк": "BIF",
    "Бермудский доллар": "BMD",
    "Брунейский доллар": "BND",
    "Боливийский боливиано": "BOB",
    "Бразильский реал": "BRL",
    "Багамский доллар": "BSD",
    "Бутанский Нгултрум": "BTN",
    "Ботсвана Пула": "BWP",
    "Белорусский рубль": "BYN",
    "Белизский доллар": "BZD",
#    "Канадский доллар": "CAD",
    "Конголезский франк": "CDF",
#    "Швейцарский франк": "CHF",
    "Чилийское песо": "CLP",
#    "Китайский юань": "CNY",
    "Колумбийское песо": "COP",
    "Коста-риканский колон": "CRC",
    "Кубинское песо": "CUP",
    "Эскудо Кабо-Верде": "CVE",
    "Чешская крона": "CZK",
    "Франк Джибути": "DJF",
    "Датская крона": "DKK",
    "Доминиканское песо": "DOP",
    "Алжирский динар": "DZD",
#    "Египетский фунт": "EGP",
    "Эритрейская накфа": "ERN",
    "Эфиопский быр": "ETB",
#    "Евро": "EUR",
    "Доллар Фиджи": "FJD",
    "Фунт Фолклендских островов": "FKP",
    "Фарерская крона": "FOK",
#    "Фунт стерлингов": "GBP",
    "Грузинский Лари": "GEL",
    "Фунт Гернси": "GGP",
    "Ганский седи": "GHS",
    "Гибралтарский фунт": "GIP",
    "Гамбийский даласи": "GMD",
    "Гвинейский франк": "GNF",
    "Гватемальский кетцаль": "GTQ",
    "Гайанский доллар": "GYD",
    "Гонконгский доллар": "HKD",
    "Гондурасская лемпира": "HNL",
    "Хорватская куна": "HRK",
    "Гаитянский гурд": "HTG",
    "Венгерский форинт": "HUF",
    "Индонезийская рупия": "IDR",
    "Новый израильский шекель": "ILS",
    "Мэнский фунт": "IMP",
    "Индийская рупия": "INR",
    "Иракский динар": "IQD",
    "Иранский риал": "IRR",
    "Исландская крона": "ISK",
    "Джерси Паунд": "JEP",
    "Ямайский доллар": "JMD",
    "Иорданский динар": "JOD",
#    "Японская иена": "JPY",
    "Кенийский шиллинг": "KES",
    "Киргизский сом": "KGS",
    "Камбоджийский риель": "KHR",
    "Доллар Кирибати": "KID",
    "Коморский франк": "KMF",
    "Южнокорейская вона": "KRW",
    "Кувейтский динар": "KWD",
    "Доллар Каймановых островов": "KYD",
#    "Казахстанский Тенге": "KZT",
    "Лаосский кип": "LAK",
    "Ливанский фунт": "LBP",
    "Шри-ланкийская рупия": "LKR",
    "Либерийский доллар": "LRD",
    "Лесото Лоти": "LSL",
    "Ливийский динар": "LYD",
    "Марокканский дирхам": "MAD",
    "Молдавский лей": "MDL",
    "Малагасийский ариари": "MGA",
    "Македонский денар": "MKD",
    "Бирманский кьят": "MMK",
    "Монгольский тогрог": "MNT",
    "Патака Макао": "MOP",
    "Мавританская угия": "MRU",
    "Маврикийская рупия": "MUR",
    "Мальдивская руфия": "MVR",
    "Малавийская квача": "MWK",
    "Мексиканское песо": "MXN",
    "Малазийский ринггит": "MYR",
    "Мозамбикский метикал": "MZN",
    "Намибийский доллар": "NAD",
    "Нигерийская найра": "NGN",
    "Никарагуанская Кордова": "NIO",
    "Норвежская крона": "NOK",
    "Непальская рупия": "NPR",
    "Новозеландский доллар": "NZD",
    "Оманский риал": "OMR",
    "Панамский бальбоа": "PAB",
    "Перуанский соль": "PEN",
    "Папуа-Новая Гвинея Кина": "PGK",
    "Филиппинское песо": "PHP",
    "Пакистанская рупия": "PKR",
    "Польский злотый": "PLN",
    "Парагвайский гуарани": "PYG",
    "Катарский риал": "QAR",
    "Румынский лей": "RON",
    "Сербский динар": "RSD",
#    "Российский рубль": "RUB",
    "Руандийский франк": "RWF",
    "Саудовский риял": "SAR",
    "Доллар Соломоновых Островов": "SBD",
    "Сейшельская рупия": "SCR",
    "Суданский фунт": "SDG",
    "Шведская крона": "SEK",
    "Сингапурский доллар": "SGD",
    "Фунт острова Святой Елены": "SHP",
    "Сьерра-Леоне леоне": "SLE",
    "Сомалийский шиллинг": "SOS",
    "Суринамский доллар": "SRD",
    "Южносуданский фунт": "SSP",
    "Сан-Томе и Принсипи Добра": "STN",
    "Сирийский фунт": "SYP",
    "Эсватини Лилангени": "SZL",
#    "Тайский бат": "THB",
    "Таджикский сомони": "TJS",
    "Туркменский манат": "TMT",
    "Тунисский динар": "TND",
    "Тонганский Паанга": "TOP",
#    "Турецкая лира": "TRY",
    "Доллар Тринидада и Тобаго": "TTD",
    "Доллар Тувалу": "TVD",
    "Новый тайваньский доллар": "TWD",
    "Танзанийский шиллинг": "TZS",
#    "Украинская гривна": "UAH",
    "Угандийский шиллинг": "UGX",
#    "Доллар США": "USD",
    "Уругвайское песо": "UYU",
#    "Узбекский сум": "UZS",
    "Венесуэльский Боливар Соберано": "VES",
    "Вьетнамский донг": "VND",
    "Вануату Вату": "VUV",
    "Самоанская тала": "WST",
    "Центральноафриканский франк КФА": "XAF",
    "Восточно-карибский доллар": "XCD",
    "Специальные права заимствования": "XDR",
    "Западноафриканский франк КФА": "XOF",
    "Франк КФП": "XPF",
    "Йеменский риал": "YER",
    "Южноафриканский рэнд": "ZAR",
    "Замбийская квача": "ZMW",
    "Зимбабвийский доллар": "ZWL"
}

dict_crypta_all = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Tether": "usdt",
    "Solana": "sol",
#    "Binance Coin": "bnb",
    "Ripple": "xrp",
    "Dogecoin": "doge",
    "Cardano": "ada",
#    "USDC": "usdc",
#    "EOS": "eos",
#    "Litecoin": "ltc",
#    "Stablecoin": "stable",
    "Stellar": "xlm"
}

# list_fiat_all = list(dict_fiat_all)
list_crypta_all = list(dict_crypta_all)
list_fiat = []
list_crypta = []


# добавление нового элемента
def add_fiat():
    s = fiat_all_listbox.curselection()
    new_fiat = list_fiat_all[s[0]]
    if new_fiat not in list_fiat:
        list_fiat.append(new_fiat)
        fiat_var.set(list_fiat)
#        print(list_fiat)
#    print(selection, list1[selection[0]], dict1_all[list1[selection[0]]])
#    dict2[list1[selection[0]]] = dict1_all[list1[selection[0]]]
#    print(dict2)


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
'''
wind_select = Tk()
wind_select.title("Выбор валют")
wind_select.geometry("630x250")

ttk.Button(text="Добавить", command=add_fiat).grid(row=0, column=1, padx=6, pady=6)

ttk.Button(text="Удалить", command=delete).grid(row=0, column=3, padx=5, pady=5)

ttk.Button(text="▲", command=up_step).grid(row=1, column=3, padx=5, pady=5)

ttk.Button(text="▼", command=down_step).grid(row=2, column=3, padx=5, pady=5)

ttk.Button(text="Очистить", command=del_all).grid(row=3, column=3, padx=5, pady=5)

fiat_all_var = Variable(value=list_fiat_all)
fiat_all_listbox = Listbox(listvariable=fiat_all_var, width=35)
fiat_all_listbox.grid(row=0, column=0, rowspan=4, sticky=EW, padx=5, pady=5)

fiat_var = Variable(value=list_fiat)
fiat_listbox = Listbox(listvariable=fiat_var, width=35, selectmode="single")
fiat_listbox.grid(row=0, column=2, rowspan=4, sticky=EW, padx=5, pady=5)

wind_select.mainloop()
'''