# Plan2Train
training planing tool with sync to garmin
using flask, sqlalchemy, werkzeug, 

## create database
```
pip3 install -r requirements.txt
python3
from main import db
db.create_all()
```

## run local
```
set FLASK_APP=main.py
set FLASK_DEBUG=1
$env:FLASK_APP = "main.py"
$env:FLASK_DEBUG = "1"
flask run
```

## run on google server
first setup and install
```
https://console.cloud.google.com/appengine/
https://cloud.google.com/sdk/?hl=de
```
then run
```
gcloud --version
gcloud app deploy
gcloud app browse
```

## TODO
* gitignore database file
* registering users protected by a password
* add separate file to store master password + gitignore
* sqlalchemy orm
* garmin sync