import os
from flask import Blueprint, url_for, render_template, redirect, request, Response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy
import json

from models import db, User, TrainSession

if 'WEBSITE_PW' in os.environ:
    webPassword = os.environ['WEBSITE_PW']

login_manager = LoginManager()



checkPassword = Blueprint('checkPassword', __name__, template_folder='../templates')

@checkPassword.route('/checkPassword', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
    else:
        masterPassword = None

    if masterPassword:
        if masterPassword == webPassword:
            return {"status":"True"}
        else:
            return {"status":"False"}
    else:
        return {"status":"False"}

login = Blueprint('login', __name__, template_folder='../templates')
login_manager.init_app(login)

@login.route('/login', methods=['GET', 'POST'])
def show():
    username = None
    password = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    elif request.method == 'GET':
        #username = request.args.get['username']
        #password = request.args.get['password']
        return render_template('login.html')
    else:
        return render_template('login.html')

    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            #trainSessions = User.query.filter_by(id=current_user.get_id()).first().trainSessions
            return render_template('home.html')#, trainSessions=trainSessions)
        else:
            return redirect(url_for('login.show') + '?error=incorrect-password')
    else:
        return redirect(url_for('login.show') + '?error=user-not-found')

home = Blueprint('home', __name__, template_folder='../templates')
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    #trainSessions = User.query.filter_by(id=current_user.get_id()).first().trainSessions
    return render_template('home.html')#, trainSessions=trainSessions)

logout = Blueprint('logout', __name__, template_folder='../templates')
login_manager.init_app(logout)

@logout.route('/logout')
@login_required
def show():
    logout_user()
    return redirect(url_for('login.show') + '?success=logged-out')

register = Blueprint('register', __name__, template_folder='../frontend')
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
        if masterPassword == webPassword:
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['confirm-password']

            if username and password and confirm_password:
                if password == confirm_password:
                    hashed_password = generate_password_hash(
                        password, method='pbkdf2:sha256')
                    try:
                        new_user = User(
                            username=username,
                            password=hashed_password,
                        )

                        db.session.add(new_user)
                        db.session.commit()
                    except sqlalchemy.exc.IntegrityError:
                        return redirect(url_for('register.show') + '?error=user-exists')

                    return redirect(url_for('login.show') + '?success=account-created')
            else:
                return redirect(url_for('register.show') + '?error=missing-fields')
        else:
            return redirect(url_for('register.show') + '?error=wrong-masterPassword')
    elif request.method == 'GET':
        #masterPassword = request.args.get('masterPassword')
        return render_template('register.html')
    else:
        #masterPassword = None
        return render_template('register.html')

userSessions = Blueprint('userSessions', __name__, template_folder='../templates')

@userSessions.route('/userSessions', methods=['GET', 'POST'])
def data():
    trainSessions = User.query.filter_by(id=current_user.get_id()).first().trainSessions
    processedTrainingSessions = list()
    for row in trainSessions:
        processedTrainingSessions.append({
            'id': row.id,
            'start': row.date,
            'title': row.title,
            'color': row.color,
            'description': row.description,
            'url': "javascript: clickLink("+str(row.id)+")"
            })
    return Response(json.dumps(processedTrainingSessions),  mimetype='application/json')

allUsers = Blueprint('allUsers', __name__, template_folder='../templates')

@allUsers.route('/allUsers', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
    else:
        masterPassword = None

    if masterPassword == webPassword:
        users = User.query.all()
        return render_template('allUsers.html', users=users)
    else:
        return redirect(url_for('login.show'))

trainingDetails = Blueprint('trainingDetails', __name__, template_folder='../templates')

@trainingDetails.route('/trainingDetails', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        id = request.form['id']
        # date = request.form['date']
        # title = request.form['title']
        # color = request.form['color']
        # description = request.form['description']
    elif request.method == 'GET':
        id = request.args.get('id')
        # date = request.args.get('date')
        # title = request.args.get('title')
        # color = request.args.get('color')
        # description = request.args.get('description')
    else:
        masterPassword = None
        id = None
        # date = None
        # title = None
        # color = None
        # description = None
        return render_template('home.html')
        
    training = db.session.scalars(
        sqlalchemy.select(TrainSession)
        .where(TrainSession.id == id)
        .join(TrainSession.user)
        .where(User.id == current_user.get_id())
    ).first()
    #return render_template('trainingDetails.html' +'?id='+id, training=training)
    return render_template('trainingDetails.html', training=training)
