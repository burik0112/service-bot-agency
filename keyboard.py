from telebot import types
from utils import translator as _


# tours = {
#     1: {
#         'title': 'England',
#         'content': 'Lorem ipsum set amet dolor'
#     },
#     2: {
#         'title': 'France',
#         'content': 'Lorem ipsum set amet dolor dsfa ef adsf adsfa'
#     },
#     3: {
#         'title': 'German',
#         'content': 'Lorem ipsum set amet dolor fwas qweq wqw eqw eq weqwe qweqweqwe'
#     },
#     4: {
#         'title': 'USA',
#         'content': 'Lorem ipsum set amet dolor Lorem ipsum set amet dolor'
#     },
# }
def name():
    keyboard = types.ReplyKeyboardMarkup()

    keyboard.add(
        types.KeyboardButton('Name'),
    )
    return keyboard


def surname():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(
        types.KeyboardButton('Surname')
    )
    return keyboard


def number():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(
        types.KeyboardButton('Number')
    )
    keyboard.add(types.KeyboardButton('Назад'))
    return keyboard


def get_id_hotel(hotels):
    keyboard = types.ReplyKeyboardMarkup()

    for hotel in hotels:
        pk = str(hotel['title'])
        keyboard.add(
            types.KeyboardButton(pk),
        )
    keyboard.add(types.KeyboardButton('Назад'))

    return keyboard


def get_contact():
    keyboard = types.ReplyKeyboardMarkup(row_width=1)

    keyboard.add(
        types.KeyboardButton('Назад'),
        types.KeyboardButton('Book', request_contact=True)
    )
    # bot.send_message(message.chat.id, 'Hello', reply_markup=keyboard)
    # bot.register_next_step_handler(message, show_data)
    return keyboard


def tour_id_keyboard(tours):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    for tour in tours:
        pk = str(tour['title'])
        keyboard.add(
            types.KeyboardButton(pk),
        )
    keyboard.add(types.KeyboardButton('Назад'), )

    return keyboard


def choose_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=3)

    keyboard.add(
        types.KeyboardButton('Sayohat turlari'),
        types.KeyboardButton('Biz Milan bog\'laning'),
        types.KeyboardButton('Mehmonxonalar')
    )
    # print(tours['']['title'])
    return keyboard


def back_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(
        types.KeyboardButton('Назад')
    )
    return keyboard
# #     keyboard = types.InlineKeyboardMarkup()
# #
# #     keyboard.add(
# #         types.InlineKeyboardButton('Назад', callback_data='назад')
# #     )
# keyboard.add(
#     types.KeyboardButton('Share contact', request_contact=True),
#
# )
