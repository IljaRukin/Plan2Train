from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy

from models import db, User

with open("master_password.txt", "r") as f:
    Password = f.readline().replace('\r', '').replace('\n', '')

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
        if masterPassword == Password:
            return "True"
        else:
            return "False"
    else:
        return "False"

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
            return redirect(url_for('home.show'))
        else:
            return redirect(url_for('login.show') + '?error=incorrect-password')
    else:
        return redirect(url_for('login.show') + '?error=user-not-found')

home = Blueprint('home', __name__, template_folder='../templates')
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    return render_template('home.html')

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
        if masterPassword == Password:
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

allUsers = Blueprint('allUsers', __name__, template_folder='../templates')

@allUsers.route('/allUsers', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
    elif request.method == 'GET':
        masterPassword = request.args.get('masterPassword')
    else:
        masterPassword = None

    if masterPassword == Password:
        users = User.query.all()
        return render_template('allUsers.html', users=users)
    else:
        return redirect(url_for('login.show'))
