import os

from flask import Flask, render_template
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from Controller.userController import usersB
from Controller.bookController import bookB
from Util.db import DataBase
from datetime import timedelta

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

app.register_blueprint(usersB)
app.register_blueprint(bookB)

load_dotenv()
db = DataBase()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def notFound(e):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000)
