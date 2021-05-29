from flask import Flask
import telegram

from app import config

global bot


app = Flask(__name__)
bot = telegram.Bot(token=config.TOKEN)
