from flask import request
from app import app, bot
from app.database import db, User
import telegram

from app import config, messages

import requests


@app.route('/', methods=['GET']) # index page
def index():
    return "Welcome!"


@app.route('/', methods=['POST']) # receiving messages
def receive():
       
    resp = request.get_json()
    msgtext = resp["message"]["text"]
    sendername = resp["message"]["from"]["first_name"]
    username = resp["message"]["from"]["username"]
    chatid = resp["message"]["chat"]["id"]
    bot.sendMessage(chat_id=chatid, text='Welcum!')
    user = User.query.get(chatid)
    
    if user is None:
        new_user = User(id =chatid, username = username)
        db.session.add(new_user)
        db.session.commit() 
    else:
        bot.sendMessage(chat_id=chatid, text= 'Bak!')
    return "suck my cock"



@app.route("/setwebhook")
def setwebhook():
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(config.TOKEN,config.NGROK))
  
    if s:
        return "Success"
    else:
        return "fail"

