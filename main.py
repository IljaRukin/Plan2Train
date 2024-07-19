from flask import Flask
import sqlalchemy
from flask_login import LoginManager

from models import db, User, TrainSession#, Sessions

from index import root, index
from updateData import addEntry, removeEntry
from login import login
from logout import logout
from register import register
from home import home

app = Flask(__name__, static_folder='../templates/static')

dbPath = 'sqlite:///database.db'
with open("master_password.txt", "r") as f:
    Password = f.readline().replace('\r', '').replace('\n', '')

app.config['SECRET_KEY'] = Password
app.config['SQLALCHEMY_DATABASE_URI'] = dbPath

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(root)
app.register_blueprint(index)
app.register_blueprint(addEntry)
app.register_blueprint(removeEntry)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)

@login_manager.user_loader
def load_user(userId):
    return User.query.get(int(userId))

if __name__ == '__main__':
    #db.create_all()
    app.run(host='0.0.0.0', port=3000)
