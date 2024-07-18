from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
#    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String)

#class Sessions(UserMixin, db.Model):
#    __tablename__ = 'sessions'
#    id = db.Column(db.Integer, primary_key=True)
#    sessionId = db.Column(db.Integer, db.ForeignKey('users.id'))
