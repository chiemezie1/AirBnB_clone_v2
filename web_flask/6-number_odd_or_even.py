#!/usr/bin/python3
"""
A simple flask app, that returns "Hello HBNB!"
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template(
            '6-number_odd_or_even.html', number=n, even="even"
        )
    else:
        return render_template(
            '6-number_odd_or_even.html', number=n, even="odd"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
