from flask import Flask
import telegram

from app.config import TOKEN, URL

global bot

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)


def setWebHook():
    bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    print("Webhook setup successful")

