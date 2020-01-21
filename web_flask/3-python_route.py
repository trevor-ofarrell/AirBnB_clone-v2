#!/usr/bin/python3
""" script that starts a Flask web application: """
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    text = text.replace("_", " ")
    return ("C " + text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyisfun(text="is_cool"):
    text = text.replace("_", " ")
    return ("Python " + text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
