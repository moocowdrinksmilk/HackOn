from flask import Flask
import telegram

# from app.config import TOKEN, URL

global bot

key  = "1801864743:AAHKi8TVKEgLGp-D7ufBrAElf03sHra18EY"
bot = telegram.Bot(token=key)
app = Flask(__name__)

from flask import Flask,request
import requests
from app import app, bot



app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    if(request.method == "POST"):
       
        resp = request.get_json()
        # msgtext = resp["message"]["text"]
        # sendername = resp["message"]["from"]["first_name"]
        chatid = resp["message"]["chat"]["id"]
        # return resp
        bot.sendMessage(chat_id=chatid, text='Welcum!')
        print
        print(resp)
    return "suck my cock"


def sendmessage(chatid):
    print(chatid)

@app.route("/setwebhook/")
def setwebhook():
    url = "https://6f70a18620a0.ngrok.io/"
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
  
    if s:
        return "Success"
    else:
        return "fail"



@app.route('/{}'.format(key), methods=['POST'])
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

