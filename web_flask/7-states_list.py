#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask, render_template, g
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False


app.route("/states_list")
def states():
    """
    show a list of states
    """
    states_list = storage.all(State)
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    """
    close current session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
