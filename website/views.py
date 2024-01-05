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

# ---------- Manage Password Page ----------
@views.route('/manage-stored-passwords', methods=['GET', 'POST'])
@login_required
def manage_stored_passwords():      
        # Query stored passwords for the current user
        stored_passwords = Storage.query.filter_by(user_id=current_user.id).all()
        return render_template('user-account.html', user=current_user, stored_passwords=stored_passwords, manage_pwd_popup=True)

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
                                   password=password, 
                                   website=website, 
                                   user_id=current_user.id)
        else:
            password = request.form['password']
            new_password = Storage(username=username, 
                                   password=password, 
                                   website=website, 
                                   user_id=current_user.id)    

        # Add the new instance to the database session
        db.session.add(new_password)

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for('views.profile')) 

# ---------- Delete password button ----------
@views.route('/delete-password/<int:password_id>', methods=['POST'])
@login_required
def delete_password(password_id):
    # Query the password to be deleted
    password_to_delete = Storage.query.get_or_404(password_id)

    # Check if the password belongs to the current user
    if password_to_delete.user_id == current_user.id:
        # Delete the password from the database
        db.session.delete(password_to_delete)
        db.session.commit()

        flash("Password deleted successfully.", "success")

    return redirect(url_for('views.manage_stored_passwords'))

@views.route('/edit-password/<int:password_id>', methods=['GET', 'POST'])
@login_required
def edit_password(password_id):
    password_to_edit = Storage.query.get_or_404(password_id)

    # Check if the password belongs to the current user
    if password_to_edit.user_id == current_user.id:
        if request.method == 'POST':
            # Handle form submission to update the password details
            password_to_edit.username = request.form['edit_username']
            password_to_edit.password = request.form['edit_password']
            password_to_edit.website = request.form['edit_website']

            # Commit the changes to the database
            db.session.commit()

            flash("Password updated successfully.", "success")

            return redirect(url_for('views.manage_stored_passwords'))
        
        return render_template('edit-password.html', password=password_to_edit, user=current_user)
    
    return redirect(url_for('views.index'))
