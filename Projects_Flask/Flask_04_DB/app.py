#!/usr/bin/env python3


import os
from flask import Flask, redirect, url_for, request, render_template, session
from module_psycopg2_select import psycopg2_select
# from module_pymssql_select import pymssql_select
# from module_pypyodbc_select import pypyodbc_select


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
    x = psycopg2_select()
    return render_template('select.html', button_select=x)


@app.route('/insert', methods=['GET'])
def insert_page():
    return render_template('insert.html')


@app.route('/update', methods=['GET'])
def update_page():
    return render_template('update.html')


@app.route('/delete', methods=['GET'])
def delete_page():
    return render_template('delete.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])
