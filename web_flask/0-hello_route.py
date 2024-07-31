#!/usr/bin/python3
"""
simple flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    print("Hello HBNB!")
