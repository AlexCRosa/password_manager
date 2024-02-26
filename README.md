# Password Manager
The Password Manager is a tool for safely store and manage passwords.

## Local Setup

Python 3.11 or newer is required. You can download it [here](https://www.python.org/downloads/). Verify that it installed by running `python --version` (you might have to use the `python3` or `python3.11` command instead if you have another version installed).

This application uses Flask for web development. The documentation can be verified [here](https://flask.palletsprojects.com/en/3.0.x/).

SQLAlchemy is required for the database. The documentation and an overview about Key Features can be verified [here](https://www.sqlalchemy.org/). 

Flask-Login was used to manage Login and user's session. The documentation can be verified [here](https://flask-login.readthedocs.io/en/latest/).

1. Clone the repository to your local machine.
2. `cd` into the project directory.
3. `python -m venv env` to create a virtual environment.
4. `pip install -r requirements.txt` to install the necessary dependencies.
5. Run the `main.py` file to stark Flask app. 
6. By default, Flask will run on the following URL (http://127.0.0.1:5000).