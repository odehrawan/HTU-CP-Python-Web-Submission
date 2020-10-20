import os

from flask import Flask, session, render_template
from .core import db, intialize_db_config

# create the Flask
app = Flask(__name__)

# configure the app
app.config.from_mapping(
    SECRET_KEY='dev'
)

intialize_db_config(app)

# a simple test route
@app.route('/hello')
def hello():
    return 'Hello, World!'



@app.route('/showsession')
def show_session():
    return render_template('session.html')

# register the 'user' blueprint
from .views import user
app.register_blueprint(user.bp)

# register the 'home' blueprint
from .views import home
app.register_blueprint(home.bp)

# register the 'tasklists' blueprint
# from .views import item
# app.register_blueprint(item.app)

# register the 'task' blueprint
from .views import item
app.register_blueprint(item.bp)

from .views import seller
app.register_blueprint(seller.bp)