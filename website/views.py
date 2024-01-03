from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Storage
from . import db
import json

views = Blueprint('views', __name__)

# ---------- Pages navigation ----------
@views.route('/')
def index():
    return render_template('index.html')

@views.route('/main', methods=['POST'])
def main():
    menu_option = request.form['menu_option']

    if menu_option == 'password_creator':
        return render_template('password-creator.html')
    elif menu_option == 'new_account':
        return render_template('create-account.html')

@views.route('/login')
def login():
    return render_template('login-page.html')

@views.route('/create-password')
def create_password():
    return render_template('password-creator.html')

@views.route('/new-account')
def new_account():
    return render_template('create-account.html')

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
