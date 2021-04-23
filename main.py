from aiogram import Bot, Dispatcher, executor
from aiogram import types
from config import *
import logging
from keyboards import start_murkup
from AmericyanProject.newsamParser.parser import Parser


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
parser = Parser()


@dp.callback_query_handler(lambda call: call.data in ['back1', 'back2', 'back3', 'back4'])
async def call_back(call):
    try:
        if call.data == 'back1':
            markup = start_murkup.start_markup
            await bot.edit_message_text('Welcome to news bot\n'
                                        'To continue press button',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'back2':
            markup = start_murkup.news_menu
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'back3':
            markup = start_murkup.curr
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'back4':
            markup = start_murkup.start_markup
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['menu', 'news', 'sport', 'curr'])
async def call_two(call):
    try:
        if call.data == 'menu':
            markup = start_murkup.news_menu
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'news':
            markup = start_murkup.news
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'sport':
            markup = start_murkup.sport
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'curr':
            markup = start_murkup.curr
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['tert', 'times', 'cnn', 'news.am', 'back6'])
async def call_names(call):
    try:
        if call.data == 'news.am' or call.data == 'back6':
            data = parser.find_newsam()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkup(markdata, name='newsam')
            markup = source[0]
            callbackdt = source[1]
            await bot.edit_message_text(text='News.am news',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in callbackdt)
            async def call_nwam(ca):
                for ar in callbackdt:
                    if ca.data == ar:
                        mar = types.InlineKeyboardMarkup()
                        butt = types.InlineKeyboardButton('<< Back', callback_data='back6')
                        mar.add(butt)
                        text = markdata[int(ar[-1])][2]+'\n'+markdata[int(ar[-1])][1]
                        await bot.edit_message_text(text=text, chat_id=ca.message.chat.id, message_id=call.message.message_id, reply_markup=mar)
        elif call.data == 'tert':
            markup = start_murkup.news
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'times':
            markup = start_murkup.sport
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
        elif call.data == 'cnn':
            markup = start_murkup.curr
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['usd', 'euro', 'rub'])
async def call_two(call):
    try:
        currency = parser.find_curr()
        if call.data == 'usd':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('<< Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['usd'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'euro':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('<< Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['eur'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'rub':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('<< Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['rub'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['newsam'])
async def call_newsam(call):
    try:
        if call.data == 'newsam':
            print('vvvvvvvvv')
            data = parser.find_newsam()
            newsdata = start_murkup.returnMarkup(data, 'newsam')
            markup = newsdata[0]
            makr = types.InlineKeyboardMarkup()
            for ma in markup:
                makr.add(ma)
            markups = start_murkup.reformMarkup(markup)
            print(markups)
            await bot.send_message(call.message.chat.id, 'Welcome to news bot\n'
                                                    'to continue press button', reply_markup=makr)

    except Exception as e:
        repr(e)



@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    try:
        markup = start_murkup.start_markup
        await bot.send_message(message.chat.id, 'Hi {username}'.format(username=message.from_user.username))
        await bot.send_message(message.chat.id, 'Welcome to news bot\n'
                                                'to continue press button', reply_markup=markup)

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    executor.start_polling(dp)
