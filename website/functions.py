import string
import random
import time
from flask import *

# Generator WEAK PASSWORD
def weak_password_generator(length):
    amount_characters = length
    characters_counter = 0
    password = ""

    # letters(lowercase + uppercase) and numbers
    while characters_counter < amount_characters:
        password += random.choice(string.ascii_letters + string.digits)
        characters_counter += 1

    return password

# Generator STRONG PASSWORD logic
def strong_password_generator(length):
    amount_characters = length
    characters_counter = 0
    password = ""

    # letters(lowercase + uppercase), numbers, and symbols
    while characters_counter < amount_characters:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        characters_counter += 1

    return password
    
