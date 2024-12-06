
class FIAT:
    def __init__(self, country, cod, text):
        self.country = country
        self.cod = cod
        self.text = text

list_fiat_all_FIAT = [
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
    FIAT("Восточно-Карибских государств", "XCD", "восточно-карибского доллара"),
    FIAT("Специальных прав заимствования", "XDR", "специальных прав заимствования"),
    FIAT("Африканского финансового сообщества", "XOF", "западноафриканского франка КФА"),
    FIAT("французских общин Тихого океана", "XPF", "франка КФП"),
    FIAT("Йемена", "YER", "йеменского риала"),
    FIAT("Южно-Африканской Республики", "ZAR", "южноафриканского рэнда"),
    FIAT("Замбии", "ZMW", "замбийской квачи"),
    FIAT("Зимбабве", "ZWL", "зимбабвийского доллара")
]

list_fiat_all_country = []
for coin in list_fiat_all_FIAT:
    list_fiat_all_country.append(coin.country)
list_fiat_all_country.sort(key=str.lower)


list_fiat_FIAT = [
    FIAT("США", "USD", "американского доллара"),
    FIAT("Евросоюза", "EUR", "евро"),
    FIAT("Великобритании", "GBP", "британского фунта стерлингов"),
    FIAT("Японии", "JPY", "японской йены"),
    FIAT("Китая", "CNY", "китайского юаня"),
    FIAT("России", "RUB", "российского рубля"),
    FIAT("Украины", "UAH", "украинской гривны"),
    FIAT("Тайланда", "THB", "тайского бата"),
    FIAT("Турции", "TRY", "турецкой лиры"),
    FIAT("Египта", "EGP", "египетского фунта"),
    FIAT("Канады", "CAD", "канадского доллара"),
    FIAT("Швейцарии", "CHF", "швейцарского франка"),
    FIAT("Казахстана", "KZT", "казахстанского тенге"),
    FIAT("Узбекистана", "UZS", "узбекского сума")
]


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
