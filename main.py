from aiogram import Bot, Dispatcher, executor
from aiogram import types
from config import *
import logging
from keyboards import start_murkup
from AmericyanProject.newsamParser.parser import Parser
from dbconnect.database import DataConnector


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
parser = Parser()
db = DataConnector()


@dp.callback_query_handler(lambda call: call.data in ['back1', 'back2', 'back3', 'back4', 'back5'])
async def call_back(call):
    try:
        if call.data == 'back1':
            markup = start_murkup.start_markup
            await bot.edit_message_text('  🗞 Welcome to news bot 🗞\n'
                                        '👇 Press button to continue 👇',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'back2':
            markup = start_murkup.news_menu
            await bot.edit_message_text(' 🗞 Choose category 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'back3':
            markup = start_murkup.curr
            await bot.edit_message_text('💱 Choose a type of currency 💱',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'back4':
            markup = start_murkup.news
            await bot.edit_message_text('🗞 Which source do you prefer? 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'back5':
            markup = start_murkup.sport
            await bot.edit_message_text('🗞 Which source do you prefer? 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['menu', 'news', 'sport', 'curr'])
async def call_two(call):
    try:
        if call.data == 'menu':
            markup = start_murkup.news_menu
            await bot.edit_message_text(' 🗞 Choose category 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'news':
            markup = start_murkup.news
            await bot.edit_message_text('🗞 Which source do you prefer? 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'sport':
            markup = start_murkup.sport
            await bot.edit_message_text('🗞 Which source do you prefer? 🗞',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'curr':
            markup = start_murkup.curr
            await bot.edit_message_text('💱 Choose a type of currency 💱',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['tert', 'times', 'cnn', 'news.am', 'back6', 'back7', 'back8', 'back9'])
async def call_names(call):
    try:
        if call.data == 'news.am' or call.data == 'back6':
            data = parser.find_newsam()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkup(markdata, name='newsam')
            markup = source[0]
            callbackdt = source[1]
            await bot.edit_message_text(text='📃 News.am 📃',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in callbackdt)
            async def call_nwam(ca):
                try:
                    for ar in callbackdt:
                        if ca.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back6')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2]+'\n'+markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=ca.message.chat.id, message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
        elif call.data == 'tert' or call.data == 'back7':
            data = parser.find_tert()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkup(markdata, name='tert')
            markup = source[0]
            calldata = source[1]
            await bot.edit_message_text(text='📃 Tert.am 📃',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in calldata)
            async def call_times(call1):
                try:
                    for ar in calldata:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back7')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2] + '\n' + markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id,
                                                        message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
        elif call.data == 'times' or call.data == 'back8':
            data = parser.find_nytimes()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkup(markdata, name='times')
            markup = source[0]
            calldata = source[1]
            await bot.edit_message_text(text='📃 NY Times 📃',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in calldata)
            async def call_times(call1):
                try:
                    for ar in calldata:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back8')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2] + '\n' + markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id,
                                                        message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
        elif call.data == 'cnn' or call.data == 'back9':
            data = parser.find_lurer()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkup(markdata, name='cnn')
            markup = source[0]
            calldata = source[1]
            await bot.edit_message_text(text='📃 Lurer.am 📃',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in calldata)
            async def call_times(call1):
                try:
                    for ar in calldata:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back9')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2] + '\n' + markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id,
                                                        message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['tertsport', 'timessport', 'cnnsport', 'newssport', 'back10', 'back11', 'back12', 'back13'])
async def call_sport(call):
    try:
        if call.data == 'newssport' or call.data == 'back10':
            data = parser.find_sportnewsam()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkupSport(markdata, name='newssport')
            markup = source[0]
            callbackdt = source[1]
            await bot.edit_message_text(text='⚽ News.am ⚽',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda call1: call1.data in callbackdt)
            async def call_nwam(call1):
                try:
                    for ar in callbackdt:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back10')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2]+'\n'+markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id, message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
        elif call.data == 'timessport' or call.data == 'back12':
            data = parser.find_nytimesSport()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkupSport(markdata, name='timessport')
            markup = source[0]
            calldata = source[1]
            await bot.edit_message_text(text='🏀 NY Times 🏀',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda call1: call1.data in calldata)
            async def call_times(call1):
                try:
                    for ar in calldata:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back12')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2] + '\n' + markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id,
                                                        message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
        elif call.data == 'cnnsport' or call.data == 'back13':
            data = parser.find_lurersport()
            markdata = start_murkup.convert_data_mdata(data)
            source = start_murkup.returnMarkupSport(markdata, name='cnnsport')
            markup = source[0]
            calldata = source[1]
            await bot.edit_message_text(text='🏈 Lurer 🏈',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

            @dp.callback_query_handler(lambda ca: ca.data in calldata)
            async def call_times(call1):
                try:
                    for ar in calldata:
                        if call1.data == ar:
                            mar = types.InlineKeyboardMarkup()
                            butt = types.InlineKeyboardButton('↩ Back', callback_data='back13')
                            mar.add(butt)
                            text = markdata[int(ar[-1])][2] + '\n' + markdata[int(ar[-1])][1]
                            await bot.edit_message_text(text=text, chat_id=call1.message.chat.id,
                                                        message_id=call.message.message_id, reply_markup=mar)
                except Exception as e:
                    print(repr(e))
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['usd', 'euro', 'rub'])
async def call_two(call):
    try:
        currency = parser.find_curr()
        if call.data == 'usd':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('↩ Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['usd'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'euro':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('↩ Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['eur'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        elif call.data == 'rub':
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton('↩ Back', callback_data='back3')
            markup.add(b1)
            await bot.edit_message_text(currency['rub'],
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)

    except Exception as e:
        print(repr(e))


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    try:
        db.add_user(message.from_user.username, message.from_user.id, False)
        markup = start_murkup.start_markup
        await bot.send_message(message.chat.id, '✋ {username}'.format(username=message.from_user.username))
        await bot.send_message(message.chat.id, '  🗞 Welcome to news bot 🗞\n'
                                                '👇 Press button to continue 👇', reply_markup=markup)

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    executor.start_polling(dp)
