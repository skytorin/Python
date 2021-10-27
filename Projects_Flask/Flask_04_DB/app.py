#!/usr/bin/env python3


import os


from flask import Flask, redirect, url_for, request, render_template, session


config = {
        "port": os.environ.get('PORT', 5000),
        "debug": os.environ.get('DEBUG', True)
}

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
#    original_text = request.form['text']
#    target_language = request.form['language'] 
     return render_template(
        'select.html'
#        original_text = original_text_case,
#        target_language = target_language,
#        key = key,
#        endpoint = endpoint,
#        location = location
    )
       


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])


