from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Storage
from . import db
import json

views = Blueprint('views', __name__)

# ---------- Pages navigation ----------
@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        menu_option = request.form['menu_option']

        if menu_option == 'password_creator':
            return render_template('password-creator.html', user=current_user)
        elif menu_option == 'new_account':
            return render_template('create-account.html', user=current_user)
    
    return render_template('index.html', user=current_user)

@views.route('/login')
def login():
    return render_template('login-page.html', user=current_user)

@views.route('/create-password')
def create_password():
    return render_template('password-creator.html', user=current_user)

@views.route('/new-account')
def new_account():
    return render_template('create-account.html', user=current_user)

@views.route('/profile')
def profile():
    return render_template('user-account.html', user=current_user)

# ---------- Password Creator Page ----------
from .functions import weak_password_generator, strong_password_generator

@views.route('/password-creator', methods=['POST'])
def password_creator():
    # Check if password length is number
    try:
        input_data = int(request.form['length_data'])
        if input_data:
            pass
    except ValueError:
        flash("Password length invalid.", "warning")
        return render_template('password-creator.html') 

    try:
        include_symbols = request.form['strength_data']
        if include_symbols:
            pass
    except:
        flash("Please answer 'YES' or 'NO' for including symbols.", "warning")
        return render_template('password-creator.html') 

    if  include_symbols == "yes":
        generated_password = strong_password_generator(input_data)
    elif include_symbols == "no":
        generated_password = weak_password_generator(input_data)

    return render_template('password-creator.html', password=generated_password, msg="The generated password is: ")
