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
https://cloud.google.com/sdk/?hl=de
https://console.cloud.google.com/appengine/
´´´
gcloud --version
gcloud app deploy
gcloud app browse
´´´