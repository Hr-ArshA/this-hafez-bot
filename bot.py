import telebot
from random import choice
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '6053104639:AAHK93viDvYxf5BXd67Dn3YBjFMxLP1fUu0'

secret = 'jnjsdkvmsd'
url = f'https://rbytugsihksk.pythonanywhere.com/{secret}'

bot = telebot.TeleBot(token)
bot.remove_webhook()
bot.set_webhook(url=url)


app = Flask(__name__)


@app.route(f'/{secret}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    text = 'سلام\nبرای اینکه فال خود را بگیرید دکمه ی زیر را لمس کنید.'
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("فالم رو بگیر", callback_data="hafez_fall"))

    bot.reply_to(message, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "hafez_fall":
        number = choice(range(1, 496))
        name = f'hafez/sh{number}.txt'
        # print(number, name)
        text = str()
        with open(name, 'r') as f:
            text = f.read()

        # print(call)
        bot.send_message(call.from_user.id, text)
        send_welcome(call.message)


# bot.infinity_polling()