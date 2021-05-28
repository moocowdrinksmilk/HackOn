from flask import request
from app import app, bot
import telegram

from app.config import TOKEN
from app import messages


@app.route('/')
def index():
    return "Welcome!"


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id =  update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    print("got text message: ", text)

    if text == '/start':
        bot.sendMessage(chat_id=chat_id, text=messages.bot_welcome, reply_to_message_id=msg_id)
    else:
        #bot logic here
        bot.sendMessage(chat_id=chat_id, text=messages.bot_temp, reply_to_message_id=msg_id)

    return 'wtv, doesnt matter'