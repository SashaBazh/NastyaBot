import telebot
from telebot import types

bot = telebot.TeleBot('6109820425:AAH-yMur4m_EeHufvwl0OuZZzBy7hgwMHsE')
global score

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Рассказать', callback_data='tell')
    btn2 = types.InlineKeyboardButton('Техники', callback_data='technigues')
    btn3 = types.InlineKeyboardButton('Экстренная помощь',callback_data='help')
    tests = types.InlineKeyboardButton('Тесты', callback_data='tests')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(tests)

    file = open('./start.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=f"Привет, {message.from_user.first_name}\nЯ чат-бот [придумайте] 🖐️\n\nДавай я расскажу тебе чем мы будем тут заниматься?😇",
    reply_markup=markup)


@bot.message_handler()
def none(message):
    bot.send_message(message.chat.id, f'Сообщение не распознано - такой команды не существует 🤨')


def tell(message):
    markup = types.InlineKeyboardMarkup()
    btn4 = types.InlineKeyboardButton('Да😇', callback_data='yes')
    btn5 = types.InlineKeyboardButton('В другой раз', callback_data='no')
    markup.row(btn4)
    markup.row(btn5)

    file = open('./tell.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=f"Моя задача помочь тебе развить навык по осознанию своих эмоций, попробовать понять вместе с тобой,  почему ты ощущаешь то или иное чувство, постараться понять причину возникновения тревоги или злости на что-либо. Попробуем? 🤔",
    reply_markup=markup)

def no(message):
    file = open('./tell2.webp', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=f"Окей, {message.chat.first_name}. Я буду тебя ждать тут. Хорошего дня💜")

def yes(message):
    markup = types.InlineKeyboardMarkup()
    btn6 = types.InlineKeyboardButton('Давай😏', callback_data='ye')
    markup.row(btn6)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=f"Хорошо.🙂\nДавай, для начала, я покажу тебе принцип работы 'Когнитивно - поведенческой терапии' на простом примере с небольшой загадкой🧐",
    reply_markup=markup)

def technigues(message):
    markup = types.InlineKeyboardMarkup()
    btn7 = types.InlineKeyboardButton('Техника №1', url='https://www.instagram.com/kurilenko.psy/')
    btn8 = types.InlineKeyboardButton('Техника №2', url='https://www.instagram.com/kurilenko.psy/')
    btn9 = types.InlineKeyboardButton('Техника №3', url='https://www.instagram.com/kurilenko.psy/')
    btn10 = types.InlineKeyboardButton('Техника №4', url='https://www.instagram.com/kurilenko.psy/')
    btn11 = types.InlineKeyboardButton('Техника №5', url='https://www.instagram.com/kurilenko.psy/')
    btn12 = types.InlineKeyboardButton('Техника №6', url='https://www.instagram.com/kurilenko.psy/')
    btn13 = types.InlineKeyboardButton('Техника №7', url='https://www.instagram.com/kurilenko.psy/')
    btn14 = types.InlineKeyboardButton('Техника №8', url='https://www.instagram.com/kurilenko.psy/')
    markup.row(btn7, btn8)
    markup.row(btn9, btn10)
    markup.row(btn11, btn12)
    markup.row(btn13, btn14)
    file = open('./technigues.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=f"Нужно придумать техники",
                   reply_markup=markup)
def help(message):
    file = open('./help.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=f"Звони с 9.00 до 21.00\n+375336684769",)

def tests(message):
    markup = types.InlineKeyboardMarkup()
    t_1 = types.InlineKeyboardButton('Тест на удовлетворенность отношениями', callback_data='test1')
    t_2= types.InlineKeyboardButton('Тест№2', url='https://www.instagram.com/kurilenko.psy/')
    t_3= types.InlineKeyboardButton('Тест№3', url='https://www.instagram.com/kurilenko.psy/')
    markup.row(t_1)
    markup.row(t_2)
    markup.row(t_3)
    bot.send_message(message.chat.id, "Выбери тест который хочешь пройти", reply_markup=markup)


def test1(message):
    markup = types.InlineKeyboardMarkup()
    t0 = types.InlineKeyboardButton('очень недоволен', callback_data='score')
    t1 = types.InlineKeyboardButton('умеренно недоволен', callback_data='score')
    t2 = types.InlineKeyboardButton('немного недоволен', callback_data='score')
    t3 = types.InlineKeyboardButton('нейтрален', callback_data='score')
    t4 = types.InlineKeyboardButton('слегка доволен', callback_data='score')
    t5 = types.InlineKeyboardButton('умеренно доволен', callback_data='score')
    t6 = types.InlineKeyboardButton('очень доволен', callback_data='score')
    ret = types.InlineKeyboardButton('начать тест заново', callback_data='score')
    markup.row(t0, t1)
    markup.row(t2, t3)
    markup.row(t4, t5)
    markup.row(t6)
    markup.row(ret)
    bot.send_message(message.chat.id, "Общение и открытость", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'tell':
        tell(callback.message)
    elif callback.data == 'no':
        no(callback.message)
    elif callback.data == 'yes':
        yes(callback.message)
    elif callback.data == 'technigues':
        technigues(callback.message)
    elif callback.data == 'help':
        help(callback.message)
    elif callback.data == 'tests':
        tests(callback.message)
    elif callback.data == 'test1':
        test1(callback.message)
    elif callback.data == 'score':
        score(callback.message)

def score(message):
    score = 0
    if message.text == 'очень недоволен':
        score +=0
    if message.text == 'умеренно недоволен':
        score +=1
    if message.text == 'немного недоволен':
        score +=2
    if message.text == 'нейтрален':
        score +=3
    if message.text == 'слегка доволен':
        score +=4
    if message.text == 'умеренно доволен':
        score +=5
    if message.text == 'очень доволен':
        score +=6

bot.polling(none_stop=True)

