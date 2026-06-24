from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route("/about")
def about():
    name = request.args.get("name", "Flask")
    return "<p>Flask training</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('hello.html', person=name)
