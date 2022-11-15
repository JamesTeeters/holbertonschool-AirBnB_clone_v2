#!/usr/bin/python3
"a script that starts a Flask web application"
from flask import Flask, g
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


def get_db():
    if 'db' not in g:
        g.db = storage.all()
    return g.db


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
