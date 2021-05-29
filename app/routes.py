from app.models import User
from flask import request
from app import app, bot, db
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


@app.route('/testdatabase', methods=['GET'])
def test_database():
    # this test is to try create an user, add to database and return the user
    print(1)
    user = User(chat_id="test_chat_id_123")
    print(2)
    user_id = user.id
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return 'Error adding user, id:' + user_id

    print("user added successfully, id: " + user_id)

    user_from_db = "null"

    try:
        user_from_db = User.query.get(user_id)
    except:
        return "Error querying database"

    return user_from_db
