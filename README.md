# Overview

The prospect of this project is to be able to send an alert (as it is right now, we are planning around an alert functionability for e-mails, but Telegram alerts is another possibility) when inventory becomes available for the LCBO's hard-to-find inventory.

As it is right now, this respository is a prototype for testing scraping on LCBO's online inventory, according to user input.

# How to clone

If you'd like to simply clone this repo, here's the abbreviated steps:

Start MongoDB with Docker Compose:

```
docker-compose up
export MONGO_URL=mongodb://root:rootPass@127.0.0.1:27017/
```

This guide assumes you're runing Python 3. `pipenv` is required for setting up the virtual environment.

Start the Python backend:
```
FLASK_APP=$PWD/server/server.py FLASK_ENV=development pipenv run python -m flask run --port 8080
```
Start the React frontend:
```
cd client
npm i
npm start
```

# Common Issues

## Python Interpreter not recognizing imports on VSCode

That's because your interpreter is not the virtual environment interpreter. If you're on Windows:
```
Ctrl+Shift+P > Python: Select Interpreter > ('lcbo': pipenv) 
```

It should take your imports and auto-complete properly now.

## DockerException: Error fetching server API

Are you sure docker is running on your system? You can get that error when compose is not able to connect to docker via docker socket.

If the issue still persists, try to reset the Docker Desktop, and sign out your account from Docker Desktop. Sign in again and run the command again in your terminal.