from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   # means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# ---------- Login ----------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login Succesful.", "success")
                login_user(user, remember=False, duration=None) # 'remember=True' = Keeps the user logged in even after the window is closed
                return redirect(url_for('views.profile'))
            else:
                flash("Incorrect password.", "warning")
        else:
            flash("User does not exists.", "warning")

    return render_template("login-page.html", user=current_user)

# ---------- Logout ----------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# ---------- Sign up ----------
@auth.route('/create-account', methods=['POST'])
def create_account():
    name=request.form['user_name']
    email=request.form['user_email']
    password1=request.form['user_password1']
    password2=request.form['user_password2']

    if len(password1) < 10:
        flash("Password must be at least 10 characters.", "warning")
    elif password1 != password2:
        flash("Passwords don't match.", "warning")
    else:
        try:
            new_user = Users(
                name=name, 
                email=email, 
                password=generate_password_hash(password1)
                )

            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully.", "success")
            return redirect(url_for('views.login'))
        except:
            flash("User already exists.", "warning")
            return redirect(url_for('views.new_account'))     

    return render_template('create-account.html', user=current_user)