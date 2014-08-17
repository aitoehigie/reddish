from flask import render_template, url_for, flash, redirect, session, request, g
from forms import LoginForm
from app import app

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", name="ehigie aito")

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(form.username.data)
        return redirect(url_for("index"))
    return render_template("login.html", form=form)
