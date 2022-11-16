#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states_ID(id=None):
    """
    list all states / all cites of states with matching ID
    """
    all_states = storage.all(State)
    if id is None:
        return render_template('9-states.html', all_states=all_states)
    else:
        state_id = "State." + id
        return render_template("9-states.html", all_states=all_states,
                               state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    close current session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
