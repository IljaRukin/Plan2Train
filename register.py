from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import sqlalchemy

from models import db, Users

register = Blueprint('register', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        masterPassword = request.form['masterPassword']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        print("masterPassword: "+masterPassword)
        print("username: "+username)
        print("password: "+password)
        print("confirm_password: "+confirm_password)

        if username and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='pbkdf2:sha256')
                try:
                    new_user = Users(
                        username=username,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                return redirect(url_for('login.show') + '?success=account-created')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')
