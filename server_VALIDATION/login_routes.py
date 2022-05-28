from flask import Flask
from validation import app
from user import User


@app.route('/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/signout')
def signout():
    return User().signout()


@app.route('/login', methods=['POST', 'GET'])
def login():
    return User().login()
