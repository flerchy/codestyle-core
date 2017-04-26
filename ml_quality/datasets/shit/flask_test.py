#!/usr/bin/env python
from flask import Flask, render_template, Response, send_from_directory, make_response, request, current_app
from functools import update_wrapper
from datetime import timedelta
app = Flask(__name__, static_url_path='')


@app.route('/hello')
def hello_flask():
    return "<h1>Hello Flask</h1>"


@app.route('/after')
def after():
    return "after requested"


@app.route('/button')
def button():
    return render_template('button.html')

if __name__ == '__main__':
    app.run(host='10.1.15.97', port=5000, debug=True)
