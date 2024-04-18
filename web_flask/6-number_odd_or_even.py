#!/usr/bin/python3
'''
script that starts a Flask web application
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    displays Hello HBNB
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    displays HBNB
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    displays C followed by a text
    '''
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    '''
    displays Python followed by a text
    '''
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    displays n is a number if n is an integer
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    displays html page if n is an integer
    '''
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    displays html page if n is an integer
    '''
    if n % 2 == 0:
        evenness = "even"
    else:
        evenness = "odd"
    return render_template("6-number_odd_or_even.html", n=n, evenness=evenness)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
