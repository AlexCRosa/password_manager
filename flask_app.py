from flask import *
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Check if password length is number
    try:
        input_data = int(request.form['length_data'])
    except ValueError:
        flash("Invalid input.")
        return redirect('/')

    # Verify if symbols should be included
    if request.form['strength_data'] == "yes":
        generated_password = strong_password_generator(input_data)
        include_symbols = "Yes"
    elif request.form['strength_data'] == "no":
        generated_password = weak_password_generator(input_data)
        include_symbols = "No"

    return render_template('index.html', password=generated_password, symbols=include_symbols)

def strong_password_generator(length):
    amount_characters = length
    characters_counter = 0
    password = ""

    # letters(lowercase + uppercase), numbers, and symbols
    while characters_counter < amount_characters:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        characters_counter += 1

    return f"The generated password is: {password}"

def weak_password_generator(length):
    amount_characters = length
    characters_counter = 0
    password = ""

    # letters(lowercase + uppercase) and numbers
    while characters_counter < amount_characters:
        password += random.choice(string.ascii_letters + string.digits)
        characters_counter += 1

    return f"The generated password is: {password}"

if __name__ == '__main__':
    app.run(debug=True)
