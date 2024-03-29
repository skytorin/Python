#!/usr/bin/env python3

import os

from flask import Flask
from flask import request

config = {
        "port": os.environ.get('PORT', 8000),
        "debug": os.environ.get('DEBUG', False)
}

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)    
    
@app.route("/api/sum")
def sum():
    a = request.args.get('a')
    b = request.args.get('b')
    return "{0}+{1}={2}".format(a, b, int(a)+int(b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])
