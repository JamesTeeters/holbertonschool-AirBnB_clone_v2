#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    return "HBNB"


@app.route("/c/<text>")
def C(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>")
def Python(text="cool"):
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/python")
def cool():
    return "Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
