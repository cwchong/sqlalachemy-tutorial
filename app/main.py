from flask import Flask, _app_ctx_stack, jsonify, url_for, request
from flask.templating import render_template
from flask_cors import CORS
from sqlalchemy.orm import scoped_session

from . import models
from .database import SessionLocal, engine

# create tables if not exist
models.Base.metadata.create_all(bind=engine)

# export FLASK_APP=app.main:app && flask run --reload
app = Flask(__name__)
CORS(app)
# this solves threading issue b/w different .py calling connection
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

@app.route('/')
def main():
    return f"see data at {url_for('show_records')}"

@app.route('/records/')
def show_records():
    records = app.session.query(models.Record).limit(10) # .all()
    return jsonify([record.to_dict() for record in records])

@app.route('/users/')
def show_users():
    users = app.session.query(models.User).limit(10) # .all()
    return jsonify([record.to_dict() for record in users])

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        user = models.User(name=name, age=int(age))
        app.session.add(user)
        app.session.commit()

        return 'User added'

    return render_template('register.html')

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    # close and returns session to pool
    app.session.remove()