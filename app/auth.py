from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template('login.html')

@auth.route("/login", methods=["POST"])
def post_login():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = bool(request.form.get("remember"))

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Incorrect user or password")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))


@auth.route("/register")
def register():
    return render_template('register.html')

@auth.route("/register", methods=["POST"])
def post_register():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    print("user", user)
    if user:
        flash("Email address already exists")
        return redirect(url_for('auth.register'))
    
    new_user = User(
        email=email,
        password=generate_password_hash(password, method='sha256')
        )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))