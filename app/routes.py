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

@app.route("/setwebhook/")
def setwebhook():
    url = "https://d23c86e9a2de.ngrok.io"
    key = "1886467979:AAErWUqnCE-abp7SviRn3ybp_bEJ7M6As44"
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
  
    if s:
        return "Success"
    else:
        return "fail"