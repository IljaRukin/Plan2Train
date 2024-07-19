from flask import Blueprint, redirect, request
from models import db, User, TrainSession

with open("master_password.txt", "r") as f:
    Password = f.readline().replace('\r', '').replace('\n', '')

addEntry = Blueprint('addEntry', __name__, template_folder='../templates')

@addEntry.route('/addEntry')
def show():
    masterPassword = request.args.get('masterPassword')
    if masterPassword == Password:
        title = request.args.get('title')
        date = request.args.get('date')
        print("add entry")
        print("title: "+title)
        print("date: "+date)
        print("masterPassword: "+masterPassword)
        print("current_user: "+current_user.get_id())
        training = TrainSession(title=title,date=date)
        user = User.query.filter_by(username=current_user.get_id()).first()
        #user = db.session.execute(select(User).filter_by(name="sandy")).scalar_one()
        user.trainSessions.append(training)
        db.session[user.userId]=user#.add(user)
        db.session.commit()
        return "True"
    else:
        return "False"

removeEntry = Blueprint('removeEntry', __name__, template_folder='../templates')

@removeEntry.route('/removeEntry')
def show():
    masterPassword = request.args.get('masterPassword')
    if masterPassword == app.config['SECRET_KEY']:
        title = request.args.get('title')
        date = request.args.get('date')
        print("remove entry")
        print("title: "+title)
        print("date: "+date)
        print("masterPassword: "+masterPassword)
        print("current_user: "+current_user.get_id())
        training = TrainSession(title=title,date=date)
        user = User.query.filter_by(username=current_user.get_id()).first()
        #user = db.session.execute(select(User).filter_by(name="sandy")).scalar_one()
        user.trainSessions.remove(training)
        db.session[user.userId]=user#.add(user)
        db.session.commit()
        return "True"
    else:
        return "False"
