import sqlite3

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT, 
               email TEXT UNIQUE, 
               password TEXT
               )''')

"""
Try to create a variable to store the input received from the 'create-account' page
data = [("User Full Name", "example@email.com", "P@55w0rd")]
try:
    cursor.executemany('''
        INSERT INTO users (name, email, password) VALUES (?, ?, ?)', data)
except sqlite3.IntegrityError: 
    print("Do something)
"""

try:
    cursor.executemany("""
        INSERT INTO users (name, email, password) VALUES (?, ?, ?)
    """, [
        ('Alex Cesar Rosa', 'alex_cesar20@hotmail.com', '123456'),
        ('Ana Flavia dos Santos Oliveira', 'anaflavia_soliveira@hotmail.com', '987654321'),
        ('Sofia Pereira Rosa', 'sofia@google.com', 'Sofi@123456')
    ])
    connection.commit()
except sqlite3.IntegrityError:
    print("User already exists.")

result = cursor.execute("SELECT id, name FROM users")
print(result.fetchall())

connection.close()
