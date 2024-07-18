from flask import Blueprint, redirect, request

addEntry = Blueprint('addEntry', __name__, template_folder='../templates')

@addEntry.route('/addEntry', methods=['GET'])
def show():
    masterPassword = request.args.get('masterPassword')
    title = request.args.get('title')
    date = request.args.get('date')
    print("add entry")
    print("title: "+title)
    print("date: "+date)
    print("masterPassword: "+masterPassword)
    return "True"

removeEntry = Blueprint('removeEntry', __name__, template_folder='../templates')

@removeEntry.route('/removeEntry', methods=['GET'])
def show():
    masterPassword = request.args.get('masterPassword')
    title = request.args.get('title')
    date = request.args.get('date')
    print("remove entry")
    print("title: "+title)
    print("date: "+date)
    print("masterPassword: "+masterPassword)
    return "True"
