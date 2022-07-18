from flask import Flask
app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Returns the welcome string"""
    return "Welcome"


@app.route("/welcome/home")
def welcome_home():
    """Returns the welcome home string"""
    return "Welcome home"


@app.route("/welcome/back")
def welcome_back():
    """Returns the welcome back string"""
    return "Welcome back"
