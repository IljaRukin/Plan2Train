from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker

db = SQLAlchemy()

#engine = create_engine(dbPath)
#Session = sessionmaker(bind=engine)
#session = Session()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String)
    
    trainSessions = relationship('TrainSession') # one to many relationship with posts
    #trainSessions: Mapped[list['TrainSessions']] = relationship(back_populates='user')

class TrainSession(db.Model):
    __tablename__ = 'trainSessions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.String(20))

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    #userId: Mapped[int] = mapped_column(ForeignKey('users.id'))
