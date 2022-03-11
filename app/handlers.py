"""Handlers for app"""
# from crypt import methods

import sqlalchemy
from app.app import app
from flask import (
    make_response,
    redirect,
    render_template,
    escape,
    abort,
    request,
    session,
    url_for,
    flash,
)
# from datetime import datetime, timedelta


@app.route('/')
def show_start():
    return render_template("Main.html")


@app.route('/main')
def show_main():
    return render_template("Main.html")


@app.route('/about')
def show_about():
    return render_template("About.html")


@app.route('/shop_list')
def show_shop_list():
    return render_template("ShopList.html")


@app.route('/pencil')
def show_pencil():
    return render_template("Pencil.html")
