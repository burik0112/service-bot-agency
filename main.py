import requests
import telebot
from utils import translator as _
from telebot import types
from keyboard import *
import urllib.request

bot = telebot.TeleBot("5011031911:AAE3wQAvX2ZsZCThKw2KhLwC3rPzkJob9NU")


def chek(message):
    if message.text == 'Назад':
        tour(message)
    else:
        get_number(message)
        bot.send_message(message.chat.id, 'asdasdasdasdasdasd')


def back(message):
    if message.text == 'Назад':
        hotel(message)
    else:
        info(message)
        # bot.send_message(message.chat.id, 'Спасибо вам мы выйдем вам на связь')


def validation(message):
    if message.text == 'Назад':
        hotel(message)

    else:
        start(message)
        print(message.text)
        bot.send_message(message.chat.id, 'Спасибо вам мы выйдем вам на связь')


def info(message):
    data = requests.get(f'http://127.0.0.1:8000/ru/api/hotels/').json()
    result = data['results']
    for i in range(len(result)):
        if message.text in result[i]['title']:
            url = result[i]['image']
            bot.send_photo(
                message.chat.id,
                photo=urllib.request.urlopen(url).read(),
                caption=f"{result[i]['short_descriptions']}",
                reply_markup=get_contact()
            )

    # bot.send_message(message.chat.id,
    #                  'Если хотите узнать больше информацию оставте '
    #                  'нам заявку наши операторы выйдут на связь')
    bot.register_next_step_handler(message, validation)


def hotel(message):
    data = requests.get(f'http://127.0.0.1:8000/ru/api/hotels/').json()
    data = data['results']
    result = ''
    for i in data:
        result += f"{i['title']}\n"

    keyboard = get_id_hotel(data)

    bot.send_message(message.chat.id, result, reply_markup=keyboard)
    bot.register_next_step_handler(message, back)


def contact(message):
    print(message)

    bot.send_message(message.chat.id, 'sfdsfdsfsdfdsf', reply_markup=back_keyboard())
    bot.register_next_step_handler(message, tour)


def checker(message):
    if message.text == 'Назад':
        keyboard_answer(message)
    else:
        tours(message)


def tours(message):
    data = requests.get(f'http://127.0.0.1:8000/ru/api/destinations/').json()
    result = data['results']

    for i in range(len(result)):
        if message.text in result[i]['title']:
            url = result[i]['image']
            print(url)
            bot.send_photo(
                message.chat.id,
                photo=urllib.request.urlopen(url).read(),
                caption=f"{result[i]['short_description']}",
                reply_markup=get_contact()
            )

    # bot.send_message(
    #     message.chat.id,
    #     'Если хотите узнать больше информацию оставте нам заявку наши операторы выйдут на связь'
    # )

    bot.register_next_step_handler(message, back)


def tour(message):
    data = requests.get(f'http://127.0.0.1:8000/ru/api/destinations/').json()
    data = data['results']
    result = ''
    for i in data:
        result += f"{i['title']}\n"

    keyboard = tour_id_keyboard(data)

    bot.send_message(message.chat.id, result, reply_markup=keyboard)
    bot.register_next_step_handler(message, checker)


# def answer(message):
#     bot.send_message(message.chat.id, 'cacdhbcahjbchjdabc')
#     bot.register_next_step_handler(message, tours)
#
#
def get_number(message):
    print(message.text)

    bot.send_message(message.chat.id, 'asdasdasdadasdasd')
    bot.register_next_step_handler(message, chek)
#c
#
# def get_surname(message):
#     print(message.text)
#     keyboard = surname()
#
#     bot.send_message(message.chat.id, 'Familiyangizni kiriting')
#     bot.register_next_step_handler(message, get_number)
#
#
# def booking(message):
#     print(message.text)
#     keyboard = name()
#
#     bot.send_message(message.chat.id, 'Ismingizni kiriting', reply_markup=types.ReplyKeyboardRemove())
#     bot.register_next_step_handler(message, get_surname)


def keyboard_answer(message):
    if message.text == 'Sayohat turlari':
        tour(message)
        bot.send_message(message.chat.id, 'Sayohat turini tanlang')

    elif message.text == 'Biz Milan bog\'laning':
        print(message)
        bot.send_message(
            message.chat.id,
            '+998971122202',
            reply_markup=back_keyboard()
        )

        bot.register_next_step_handler(message, start)

    if message.text == 'Mehmonxonalar':
        hotel(message)


    elif message.text == 'Назад':
        back_from_tour(message)


@bot.message_handler(commands=['start'])
def start(message):
    markup = choose_keyboard()

    bot.send_message(
        message.chat.id,
        'Assalomu aleykum'
        'Informatsiyani bilish uchun quyidagi tugmalardan birini bosing',
        reply_markup=markup
    )

    bot.register_next_step_handler(message, keyboard_answer)


def back_from_tour(message):
    markup = choose_keyboard()

    bot.send_message(
        message.chat.id,
        'Quyidagi tugmalardan birini bosing',
        reply_markup=markup
    )

    bot.register_next_step_handler(message, keyboard_answer)


# def get_about(message):
#     bot.send_message(message.chat.id, "https://telegra.ph/Our-Story-12-30")
# def blog_menu(message):
#     keyboard = contact()
#     bot.reply_to(message, "https://telegra.ph/How-influince-Covid-19-12-29  ")
#     bot.send_message(message.chat.id, "https://telegra.ph/Google-inks-pact-for-new-35-storey-office-12-30")
#     bot.send_message(message.chat.id,
#                      "https://telegra.ph/Second-divided-from-form-fish-beast-made-every-of-seas-all-gathered-us-saying-he-our-12-30")
#     bot.send_message(message.chat.id,
#                      "https://telegra.ph/Second-divided-from-form-fish-beast-made-every-of-seas-all-gathered-us-saying-he-our-12-30-2",
#                      reply_markup=keyboard)
#     bot.register_next_step_handler(message, get_about)
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     keyboard = blog()
#     bot.reply_to(message, "https://telegra.ph/knjdnq-12-29")
#     bot.send_message(message.chat.id, "https://telegra.ph/Mayami-beach-12-29")
#     bot.send_message(message.chat.id, "https://telegra.ph/London-12-29-20")
#     bot.send_message(message.chat.id, "https://telegra.ph/Dubay-12-29", reply_markup=keyboard)
#     bot.register_next_step_handler(message, blog_menu)


# @bot.message_handler(commands=['blog'])


# bot.reply_to(message, "https://telegra.ph/How-influince-Covid-19-12-29  ")
# bot.send_message(message.chat.id, "https://telegra.ph/Google-inks-pact-for-new-35-storey-office-12-30")
# bot.send_message(message.chat.id, "https://telegra.ph/Second-divided-from-form-fish-beast-made-every-of-seas-all-gathered-us-saying-he-our-12-30")
# bot.send_message(message.chat.id, "https://telegra.ph/Second-divided-from-form-fish-beast-made-every-of-seas-all-gathered-us-saying-he-our-12-30-2")


# def get_menu(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     keyboard.add(
#         types.KeyboardButton('Share contact', request_contact=True),
#     )
#     bot.send_message(message.chat.id,'', reply_markup=keyboard())
bot.polling()
