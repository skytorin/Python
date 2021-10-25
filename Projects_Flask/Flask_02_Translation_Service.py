#!/usr/bin/env python3


import os


from flask import Flask, redirect, url_for, request, render_template, session


config = {
        "port": os.environ.get('PORT', 5000),
        "debug": os.environ.get('DEBUG', False)
}

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    original_text = request.form['text']
    target_language = request.form['language']
    
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    if target_language == "uppercase":
        original_text_case = original_text.upper()
    elif target_language == "lowercase":
        original_text_case = original_text.lower()
    elif target_language == "swapcase":
        original_text_case = original_text.swapcase()
    else :
        original_text_case = original_text    
     

    return render_template(
        'results.html',
        original_text = original_text_case,
        target_language = target_language,
        key = key,
        endpoint = endpoint,
        location = location
    )
       


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])


