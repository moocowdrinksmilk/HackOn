# HackOn
Lousy telegram bot that works 
I used ref: https://www.toptal.com/python/telegram-bot-tutorial-python

Note: I used heroku as it automates the Webhooks process
(see: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)


## Deployment
Push to heroku repository

## Usage
https://tryve-bot.herokuapp.com/
Send messages on Telegram to TRYVEbot

To view terminal: type this into your terminal (Heroku CLI needs to be installed)
``` bash
heroku logs --tail
```

## Create local environment and install dependencies
Run virtual environment 
```bash
source venv/bin/activate
```
Install requirements.txt
```bash
pip install -r requirements.txt
```

## Export environment variables and run flask app
```bash
$ export FLASK_ENV=development
$ export FLASK_APP=run.py
$ flask run
```
