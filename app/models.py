from app import db
from datetime import datetime

#class for users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # our own auto generated id for each user -> sqlalchemy requires this
    chat_id = db.Column(db.String(80), unique=True)
    is_registered = db.Column(db.Boolean)

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.is_registered = False # default is false to start with

    def __repr__(self):
        return '<User %r>' % self.id

# class for personalities?


# class for activities

