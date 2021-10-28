#!/usr/bin/env python3


import os
from module_pg_select import pg_select

from flask import Flask, redirect, url_for, request, render_template, session


config = {
        "port": os.environ.get('PORT', 5000),
        "debug": os.environ.get('DEBUG', True)
}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/select', methods=['GET'])
def select_page():
    return render_template('select.html')


@app.route('/insert', methods=['GET'])
def insert_page():
    return render_template('insert.html')


@app.route('/update', methods=['GET'])
def update_page():
    return render_template('update.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])


