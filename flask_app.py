from flask import *
from functions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

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

@app.route('/password-creator', methods=['POST'])
def password_creator():
    # Check if password length is number
    try:
        input_data = int(request.form['length_data'])
    except ValueError:
        flash("Invalid input.")
        return redirect('main')
    
    # Need to fix it
    if input_data == None:
        flash("Password length missing.")
        return redirect('main')
    if request.form['strength_data'] == None:
        flash("Decide between include symbols or not.")
        return redirect('main')
    
    symbols_question = request.form['strength_data']

    if  symbols_question == "yes":
        generated_password = strong_password_generator(input_data)
    elif symbols_question == "no":
        generated_password = weak_password_generator(input_data)

    return render_template('password-creator.html', password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)
