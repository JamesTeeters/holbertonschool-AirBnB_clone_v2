#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def states_list():
    """
    list cites by state
    """
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    close current session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
