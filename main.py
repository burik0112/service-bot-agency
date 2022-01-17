import requests
import telebot
from utils import translator as _
from telebot import types
from keyboard import *
import urllib.request

bot = telebot.TeleBot("5011031911:AAE3wQAvX2ZsZCThKw2KhLwC3rPzkJob9NU")


def next(message):
    if message.text == '⬅️Назад':
        keyboard_answer(message)
    else:
        info(message)


def chek(message):
    if message.text == '⬅️Назад':
        tour(message)
    else:
        get_number(message)
        bot.send_message(message.chat.id, 'asdasdasdasdasdasd')


def back(message):
    if message.text == '⬅️Назад':
        tour(message)
    else:
        contact_message(message)



def location(message):
    bot.send_location(
        message.chat.id,
        41.352306269133685,
        69.20365553816254, reply_markup=back_keyboard()
    )
    bot.register_next_step_handler(message, keyboard_answer)



def validation(message):
    if message.text == '⬅️Назад':
        hotel(message)

    else:
        contact_message(message)



def checker(message):
    if message.text == '⬅️Назад':
        keyboard_answer(message)
    else:
        tours(message)



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
                reply_markup=book()
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
    bot.register_next_step_handler(message, next)





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
                reply_markup=book()
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



def keyboard_answer(message):
    if message.text == '✈️ Наши Туры':
        tour(message)
        bot.send_message(message.chat.id, 'Выберите наши туры')

    elif message.text == '☎️Наш телефонный номер':
        print(message)
        bot.send_message(
            message.chat.id,
            '+998971122202',
            reply_markup=back_keyboard()
        )

        bot.register_next_step_handler(message, start)

    if message.text == '🏢Гостиницы':
        hotel(message)

    if message.text == '📍Наш адрес':
        location(message)

    elif message.text == '⬅️Назад':
        back_from_tour(message)


@bot.message_handler(commands=['start'])
def start(message):
    markup = choose_keyboard()

    bot.send_message(
        message.chat.id,
        'Здраствуйте Выберите одно из следующих',
        reply_markup=markup
    )

    bot.register_next_step_handler(message, keyboard_answer)


def back_from_tour(message):
    markup = choose_keyboard()

    bot.send_message(
        message.chat.id,
        'Здраствуйте Выберите одно из следующих',
        reply_markup=markup
    )

    bot.register_next_step_handler(message, keyboard_answer)


@bot.message_handler(commands=['contact'])
def contact_command(message):
    keyboard = book()
    # data = data['results']

    bot.send_message(message.chat.id, '', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact_message(message):
    print(message.contact)
    data = requests.post(f'http://127.0.0.1:8000/ru/api/application/create/', {
        'phone': message.contact.phone_number,
        'name': message.contact.first_name,
        'surname': message.contact.last_name,
    })
    print(data.json())
    bot.send_message(message.chat.id, 'Заявка принято, Спасибо вам мы выйдем вам на связь')
    bot.register_next_step_handler(message, start)


bot.polling()
