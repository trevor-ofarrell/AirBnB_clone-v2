#!/usr/bin/python3
""" script that starts a Flask web application: """
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route('/hbnb', strict_slashes=False)
def cisfun('/c/' + argv[1]):
    print(sys.argv[1])
    return ("C")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
