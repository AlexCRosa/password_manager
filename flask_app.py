from flask import *
from functions import *

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

if __name__ == '__main__':
    app.run(debug=True)
