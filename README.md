# Plan2Train
training planing tool with sync to garmin<br>
The site is hosted <a href="https://plan2train-429422.ey.r.appspot.com/home">here</a><br>
using flask, sqlalchemy, werkzeug, <br>

## create database
```
pip3 install -r requirements.txt
python3
from app import db
db.create_all()
```

## run local
```
set FLASK_APP=app.py #commandline
set FLASK_DEBUG=1 #commandline
set WEBSITE_PW=myWebPassword #commandline
set DATABASE_PATH=myDbPath #commandline
set DATABASE_PW=myDbPassword #commandline
$env:FLASK_APP = "app.py" #powershell
$env:FLASK_DEBUG = "1" #powershell
$env:WEBSITE_PW = "myWebPassword" #powershell
$env:DATABASE_PATH = "myDbPath" #powershell
$env:DATABASE_PW = "myDbPassword" #powershell
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
