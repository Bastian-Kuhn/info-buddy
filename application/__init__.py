from flask import Flask, redirect, url_for, flash 
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)

bootstrap = Bootstrap(app)

from application.main.views import main

app.register_blueprint(main)

