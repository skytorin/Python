#!/usr/bin/env python3

import os

from flask import Flask, render_template, request


config = {
        "port": os.environ.get('PORT', 5000),
        "debug": os.environ.get('DEBUG', False)
}


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])

