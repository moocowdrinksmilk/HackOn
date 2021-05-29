from flask import Flask
import telegram
from flask_sqlalchemy import SQLAlchemy

from app.config import TOKEN, URL

global bot

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


def setWebHook():
    bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    print("Webhook setup successful")


