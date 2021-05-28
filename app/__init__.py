from flask import Flask, request
import telegram

from app.config import TOKEN, URL
from app import messages

global bot

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)


def setWebHook():
    return bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))

@app.route('/')
def index():
    s = setWebHook()
    if s:
        return "webhook setup sucessful"
    else:
        return "webhook setup failed"


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

