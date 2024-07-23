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
        date = request.form['date']
        title = request.form['title']
        color = request.form['color']
        description = request.form['description']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
        date = request.args.get('date')
        title = request.args.get('title')
        color = request.args.get('color')
        description = request.args.get('description')
    else:
        masterPassword = None
        date = None
        title = None
        color = None
        description = None

    if masterPassword == Password:
        training = TrainSession(title=title,date=date,color=color,description=description)
        user = User.query.filter_by(id=current_user.get_id()).first()
        user.trainSessions.append(training)
        db.session.commit()
        return {"status":"True","id":str(training.id)}
    else:
        return {"status":"False"}

removeEntry = Blueprint('removeEntry', __name__, template_folder='../templates')

@removeEntry.route('/removeEntry', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
        id = request.form['id']
        date = request.form['date']
        title = request.form['title']
        color = request.form['color']
        description = request.form['description']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
        id = request.args.get('id')
        date = request.args.get('date')
        title = request.args.get('title')
        color = request.args.get('color')
        description = request.args.get('description')
    else:
        masterPassword = None
        id = None
        date = None
        title = None
        color = None
        description = None
        
    if masterPassword == Password:
        training = db.session.scalars(
            select(TrainSession)
            .where(TrainSession.id == id)
            .join(TrainSession.user)
            .where(User.id == current_user.get_id())
        ).first()
        selectedUser = User.query.filter_by(id=current_user.get_id()).first()
        selectedUser.trainSessions.remove(training)
        db.session.commit()
        return {"status":"True"}
    else:
        return {"status":"False"}
