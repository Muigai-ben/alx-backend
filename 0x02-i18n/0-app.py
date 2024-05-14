#!/usr/bin/env python3
"""
0-app module

This module sets up a basic Flask app with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route for the homepage

    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html', title='Welcome to Holberton', header='Hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
