from flask import Blueprint, redirect, request
from flask_login import LoginManager, current_user
from models import db, User, TrainSession
from sqlalchemy import select

with open("master_password.txt", "r") as f:
    Password = f.readline().replace('\r', '').replace('\n', '')

login_manager = LoginManager()




addEntry = Blueprint('addEntry', __name__, template_folder='../templates')

@addEntry.route('/addEntry', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
        title = request.form['title']
        date = request.form['date']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
        title = request.args.get('title')
        date = request.args.get('date')
    else:
        masterPassword = None
        title = None
        date = None

    if masterPassword == Password:
        training = TrainSession(title=title,date=date)
        user = User.query.filter_by(id=current_user.get_id()).first()
        ###user = db.session.execute(select(User).filter_by(name="sandy")).scalar_one()
        user.trainSessions.append(training)
        #db.session.add(training)
        db.session.commit()
        return "True"
    else:
        return "False"

removeEntry = Blueprint('removeEntry', __name__, template_folder='../templates')

@removeEntry.route('/removeEntry', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
        title = request.form['title']
        date = request.form['date']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
        title = request.args.get('title')
        date = request.args.get('date')
    else:
        masterPassword = None
        title = None
        date = None
        
    if masterPassword == Password:
        training = db.session.scalars(
            select(TrainSession)
            .join(TrainSession.user)
            .where(User.id == current_user.get_id())
        ).first()
        #training = TrainSession(title=title,date=date)
        print(training)
        selectedUser = User.query.filter_by(id=current_user.get_id()).first()
        ###user = db.session.execute(select(User).filter_by(name="sandy")).scalar_one()
        selectedUser.trainSessions.remove(training)
        #db.session.remove(training)
        print(selectedUser)
        db.session.commit()
        return "True"
    else:
        return "False"
