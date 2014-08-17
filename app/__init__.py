from flask import Flask
from flask.ext.login import LoginManager
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object("config")
login_manager.init_app(app)

from app import views
