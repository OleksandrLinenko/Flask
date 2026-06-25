from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template
from .hellos import hellos_bp

app = Flask(__name__)

app.register_blueprint(hellos_bp)

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
