from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📃 Menu', callback_data='menu')
    ]
])


news_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('🗞 News', callback_data='news')
    ],
    [
        InlineKeyboardButton('⚽ Sport', callback_data='sport')
    ],
    [
        InlineKeyboardButton('💱 Currency', callback_data='curr')
    ],
    [
        InlineKeyboardButton('↩ Back', callback_data='back1')
    ]

])


news = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News.am 📃', callback_data='news.am')
    ],
    [
        InlineKeyboardButton('Tert.am 📃', callback_data='tert')
    ],
    [
        InlineKeyboardButton('NY Times 📃', callback_data='times')
    ],
    [
        InlineKeyboardButton('Lurer.am 📃', callback_data='cnn')
    ],
    [
        InlineKeyboardButton('↩ Back', callback_data='back2')
    ]
])


sport = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News.am ⚽', callback_data='newssport')
    ],
    [
        InlineKeyboardButton('NY Times 🏀', callback_data='timessport')
    ],
    [
        InlineKeyboardButton('Lurer 🏈', callback_data='cnnsport')
    ],
    [
        InlineKeyboardButton('↩ Back', callback_data='back2')
    ]
])


curr = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('💵 USD', callback_data='usd')
    ],
    [
        InlineKeyboardButton('💶 EURO', callback_data='euro')
    ],
    [
        InlineKeyboardButton('💴 RUB', callback_data='rub')
    ],
    [
        InlineKeyboardButton('↩ Back', callback_data='back2')
    ]
])


def convert_data_mdata(data):
    """converting data from parsing site to make it easyer
     to make it murkup"""
    markup = []
    for ar in data:
        butt = []
        text = ar[1]
        butt.append(text[:25] + '..')
        butt.append(ar[0])
        butt.append(ar[1])
        markup.append(butt)
    return markup


def returnMarkupSport(data, name: str):
    markup = InlineKeyboardMarkup()
    max = 9
    callback = []
    i = 0
    for ar in data:
        if max < 0:
            break
        butt = InlineKeyboardButton(ar[0], callback_data=name+'{}'.format(str(i)))
        callback.append(name+'{}'.format(str(i)))
        markup.add(butt)
        i = i+1
        max -= 1
    butt = InlineKeyboardButton('↩ Back', callback_data='back5')
    markup.add(butt)
    da = [markup, callback]
    return da


def returnMarkup(data, name: str):
    markup = InlineKeyboardMarkup()
    max = 9
    callback = []
    i = 0
    for ar in data:
        if max < 0:
            break
        butt = InlineKeyboardButton(ar[0], callback_data=name+'{}'.format(str(i)))
        callback.append(name+'{}'.format(str(i)))
        markup.add(butt)
        i = i+1
        max -= 1
    butt = InlineKeyboardButton('↩ Back', callback_data='back4')
    markup.add(butt)
    da = [markup, callback]
    return da



