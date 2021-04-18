# Overview

The prospect of this project is to be able to send an alert (as it is right now, we are planning around an alert functionability for e-mails, but Telegram alerts is another possibility) when inventory becomes available for the LCBO's hard-to-find inventory.

As it is right now, this respository is a prototype for testing scraping on LCBO's online inventory, according to user input.

# How to clone

If you'd like to simply clone this repo, here's the abbreviated steps:

Start MongoDB with Docker Compose:

```
docker-compose up
export MONGO_URL=mongodb://mongo_user:mongo_secret@0.0.0.0:27017/
```

Start the Python backend:
```
FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433
```
Start the React frontend:
```
cd client
npm i
npm start
```
