import os
from flask import Flask
import sqlalchemy
from flask_login import LoginManager

from models import db, User, TrainSession

app = Flask(__name__, static_folder='../templates/static')

###dbPath = 'sqlite:///database.db'
dbPath = 'postgres://koyeb-adm:Z6LBg7uNUWRD@ep-young-glade-a2o4n9jq.eu-central-1.pg.koyeb.app/koyebdb'

if 'DATABASE_PW' in os.environ:
    dbPassword = os.environ['DATABASE_PW']

app.config['SECRET_KEY'] = dbPassword
app.config['SQLALCHEMY_DATABASE_URI'] = dbPath

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

#if len(db.session.query.__dict__)==0:
#    print("database empty !")
#    db.create_all()

from index import root, index
app.register_blueprint(root)
app.register_blueprint(index)
from sessions import addEntry, removeEntry
app.register_blueprint(addEntry)
app.register_blueprint(removeEntry)
from users import checkPassword, login, home, logout, register, userSessions, allUsers, trainingDetails
app.register_blueprint(checkPassword)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(userSessions)
app.register_blueprint(allUsers)
app.register_blueprint(trainingDetails)

@login_manager.user_loader
def load_user(userId):
    return User.query.get(int(userId))

if __name__ == '__main__':
    #db.create_all()
    app.run(host='0.0.0.0', port=3000)
