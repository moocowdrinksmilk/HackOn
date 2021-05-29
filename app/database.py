from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from app import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

userTasks = db.Table('user_tasks',
db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True),
db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key = True),
db.Column('times_issued', db.Integer))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    userTasks = db.relationship('Task', secondary=userTasks, lazy = 'subquery', backref = db.backref('users',lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username

class Task(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable = False)
    description = db.Column(db.Text)