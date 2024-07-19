from flask import Blueprint, redirect, render_template

root = Blueprint('root', __name__, template_folder='../templates')

@root.route('/', methods=['GET'])
def show():
    return render_template('index.html')

index = Blueprint('index', __name__, template_folder='../templates')

@index.route('/index', methods=['GET'])
def show():
    return render_template('index.html')
