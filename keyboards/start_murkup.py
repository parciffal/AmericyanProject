from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News menu', callback_data='menu')
    ]
])


news_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News', callback_data='news')
    ],
    [
        InlineKeyboardButton('Sport', callback_data='sport')
    ],
    [
        InlineKeyboardButton('Currency', callback_data='curr')
    ],
    [
        InlineKeyboardButton('<< Back', callback_data='back1')
    ]

])


news = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News.am', callback_data='news.am')
    ],
    [
        InlineKeyboardButton('Tert.am', callback_data='tert')
    ],
    [
        InlineKeyboardButton('Times', callback_data='times')
    ],
    [
        InlineKeyboardButton('CNN', callback_data='cnn')
    ],
    [
        InlineKeyboardButton('<< Back', callback_data='back2')
    ]
])


sport = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('News.am', callback_data='news.am')
    ],
    [
        InlineKeyboardButton('Tert.am', callback_data='tert')
    ],
    [
        InlineKeyboardButton('Times', callback_data='times')
    ],
    [
        InlineKeyboardButton('CNN', callback_data='cnn')
    ],
    [
        InlineKeyboardButton('<< Back', callback_data='back2')
    ]
])


curr = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('USD', callback_data='usd')
    ],
    [
        InlineKeyboardButton('EURO', callback_data='euro')
    ],
    [
        InlineKeyboardButton('RUB', callback_data='rub')
    ],
    [
        InlineKeyboardButton('<< Back', callback_data='back2')
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
    butt = InlineKeyboardButton('<< Back', callback_data='back2')
    markup.add(butt)
    da = [markup, callback]
    return da


def reformMarkup(markup):
    max = 1
    number = 0
    markups = []
    markind = len(markup)/max
    while markind > 0:
        markup = InlineKeyboardMarkup()
        for i in range(0, 5):
            markup.add(markup[number])
        if max == 1:
            main = InlineKeyboardButton('Main', callback_data='back1')
            butt = InlineKeyboardButton('>>', callback_data='next{}'.format(str(max)))
            markup.add(main, butt)
        else:
            butt1 = InlineKeyboardButton('<<', callback_data='right{}'.format(str(max)))
            main = InlineKeyboardButton('Main', callback_data='back1')
            butt = InlineKeyboardButton('>>', callback_data='left{}'.format(str(max)))
            markup.add(butt1, main, butt)
        max += 1
        markups.append(markup)
        markind = markind - 1
    return markups

