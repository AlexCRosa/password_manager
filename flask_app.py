from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        input_data = int(request.form['input_data'])
    except ValueError:
        flash("Invalid input.")
        return redirect('/')

    processed_result = your_python_function(input_data)
    return render_template('index.html', password=processed_result)

def your_python_function(data):
    # Your Python logic here
    # Return the processed result
    data = data * data
    return f"The password generated is: {data}"

if __name__ == '__main__':
    app.run(debug=True)
