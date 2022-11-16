#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask, render_template
from models import storage
from models import State, Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters/")
def hbnb_filters():
    """
    list States, Cities, and Amenities from DB
    """
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", all_amenities=all_amenities,
                           all_states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    close current session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
