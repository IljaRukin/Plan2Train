from flask import Blueprint, redirect, request

addEntry = Blueprint('addEntry', __name__, template_folder='../templates')

@addEntry.route('/addEntry', methods=['GET'])
def show():
    title = request.args.get('title')
    date = request.args.get('date')
    password = request.args.get('password')
    print("add entry")
    print("title: "+title)
    print("date: "+date)
    print("password: "+password)
    return "True"

removeEntry = Blueprint('removeEntry', __name__, template_folder='../templates')

@removeEntry.route('/removeEntry', methods=['GET'])
def show():
    title = request.args.get('title')
    date = request.args.get('date')
    password = request.args.get('password')
    print("remove entry")
    print("title: "+title)
    print("date: "+date)
    print("password: "+password)
    return "True"
