from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Storage
from . import db
from werkzeug.security import generate_password_hash 

views = Blueprint('views', __name__)

# ---------- Pages navigation ----------
@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        show_popup = False
        menu_option = request.form['menu_option']

        if menu_option == 'password_creator':
            return render_template('password-creator.html', user=current_user)
        elif menu_option == 'new_account':
            return render_template('create-account.html', user=current_user)
        elif menu_option == 'manage_stored_passwords':
            show_popup = True
            return render_template('user-account.html', user=current_user, manage_pwd_popup=show_popup)
        elif menu_option == 'store_new_password':
            show_popup = True
            return render_template('user-account.html', user=current_user, new_pwd_popup=show_popup)
    
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

# ---------- Add new password (User Enviroment) ----------
@views.route('/add-password', methods=['GET', 'POST'])
@login_required
def add_password():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        website = request.form['website']
        
        # Check for auto generate password
        auto_generate = request.form.get('auto_generate', 'no')

        # Create a new instance of the Storage model
        if auto_generate == "yes":
            password = strong_password_generator(16)
            new_password = Storage(username=username, 
                                   password=generate_password_hash(password), 
                                   website=website, 
                                   user_id=current_user.id)
        else:
            password = request.form['password']
            new_password = Storage(username=username, 
                                   password=generate_password_hash(password), 
                                   website=website, 
                                   user_id=current_user.id)    

        # Add the new instance to the database session
        db.session.add(new_password)

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for('views.profile')) 