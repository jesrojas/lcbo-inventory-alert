from flask import Flask, jsonify, g, request
from server.lcbo.service import Service as Item
from server.lcbo.schema import GithubRepoSchema
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route("/items", methods=["GET"])
def index():
    return jsonify(Item().find_all_items())
