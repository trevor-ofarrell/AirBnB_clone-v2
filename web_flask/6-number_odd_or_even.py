#!/usr/bin/python3
""" script that starts a Flask web application and renders html"""
from flask import Flask
from flask import request, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) == int:
        return ("{} {}".format(n, "is a number"))
    return


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if type(n) == int:
        return render_template('5-number.html', n=n)
    return


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if type(n) == int:
        if n % 2 == 0:
            x = "even"
        else:
            x = "odd"
        return render_template('6-number_odd_or_even.html', n=n, x=x)
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
