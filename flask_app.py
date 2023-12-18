from flask import *
from functions import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.string(100))
    email = db.Column(db.string(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main', methods=['POST'])
def main():
    menu_option = request.form['menu_option']

    if menu_option == 'password_creator':
        return render_template('password-creator.html')
    elif menu_option == 'new_account':
        return render_template('create-account.html')

@app.route('/login')
def login():
    return render_template('login-page.html')

@app.route('/create-password')
def create_password():
    return render_template('password-creator.html')

@app.route('/new-account')
def new_account():
    return render_template('create-account.html')

@app.route('/my-account')
def my_account():
    return render_template('user-account.html')

@app.route('/password-creator', methods=['POST'])
def password_creator():
    # Check if password length is number
    try:
        input_data = int(request.form['length_data'])
        if input_data:
            pass
    except ValueError:
        flash("Password length invalid.")
        return render_template('password-creator.html') 

    try:
        include_symbols = request.form['strength_data']
        if include_symbols:
            pass
    except:
        flash("Decide between include symbols or not.")
        return render_template('password-creator.html') 

    if  include_symbols == "yes":
        generated_password = strong_password_generator(input_data)
    elif include_symbols == "no":
        generated_password = weak_password_generator(input_data)

    return render_template('password-creator.html', password=generated_password)

@app.route('/create-account', methods=['POST'])
def create_account():
    menu_option = request.form['menu_option']

    if menu_option == 'new_account':
        return render_template('create-account.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
