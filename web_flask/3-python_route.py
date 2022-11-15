#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """
    prints Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """
    prints HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def C(text):
    """
    prints C followed by user input
    """
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
def P_is_cool():
    """
    displays Python is cool
    """
    return "Python is cool"


@app.route("/python/<text>")
def P_is_cool(text="is cool"):
    """
    print Python followed by user input
    """
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
