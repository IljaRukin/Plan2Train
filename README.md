# Plan2Train
training planing tool with sync to garmin<br>
The site is hosted <a href="https://plan2train-429422.ey.r.appspot.com/home">here</a><br>
using flask, sqlalchemy, werkzeug, <br>

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
first setup and install<br>
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
* popup for train session editing<br>
* sqlalchemy orm<br>
* garmin sync<br>
