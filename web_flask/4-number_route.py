#!/usr/bin/python3
'''
script that starts a Flask web application
'''

from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
