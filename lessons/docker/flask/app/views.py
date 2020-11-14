from flask import render_template
from app import app


@app.route('/')
def home():
    return "Hello world!333"


@app.route('/template')
def template():
    return render_template('home.html')
