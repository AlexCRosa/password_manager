from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        input_data = int(request.form['input_data'])
    except ValueError:
        return render_template('index.html', message="Please use only numbers.")

    processed_result = your_python_function(input_data)
    return render_template('result.html', result=processed_result)

def your_python_function(data):
    # Your Python logic here
    # Return the processed result
    data = data * data
    return data

if __name__ == '__main__':
    app.run(debug=True)
