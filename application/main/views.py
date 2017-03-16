#!/usr/bin/env python3
import os
from flask import Blueprint, redirect, url_for, send_from_directory, render_template, request, flash, session
from application import app

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World"


@main.route('/static/<path:path>')
def send_img(path):
    folder = os.path.dirname(__file__)
    directory = folder + "/../static/"
    return send_from_directory(directory, path)

if __name__ == '__main__':
    app.run()
