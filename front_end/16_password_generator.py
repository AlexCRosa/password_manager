import string
import random
import time

def main():

    # Get requirements from user to create the password
    def password_length():
        while True:
            amount_characters = input("How many characters the password must have? ")
            # Making sure the user's input is an integer
            try:
                return int(amount_characters)
            except ValueError:
                print("Please type only integer numbers.")
            
    def password_strength():
        while True:
            check_answer = input("Do you want a WEAK or STRONG password? ").lower()
            # Check wether the user's input is "WEAK" or "STRONG"
            if check_answer in ["weak", "strong"]:
                return check_answer
            else:
                print("Please type [WEAK] for simple password or [STRONG] for advanced password.")

    def include_symbols():
        while True:
            special = input("Do you want to include special characters [YES] or [NO]? ").lower()
            # Check wether the user's input is "YES" or "NO"
            if special in ["yes", "no"]:
                return special
            else:
                print("Please type [YES] or [NO] for including special characters.")

    # Generator of a random word logic
    def weak_random_word():
        # Defined two random lists to help with 'EXTRA' requirement
        list1 = ["pug", "heeler", "husky", "collie", "poodle", "hound"]
        list2 = ["red", "blue", "green", "black", "gray", "pink", "white"]

        defining_list = random.randint(1, 2)

        if defining_list == 1:
            temp_list = random.choices(list1)
            # Since 'random.choices' return a list, I must convert the list into a string
            random_word = ""
            for i in temp_list:
                random_word += i
            return random_word.capitalize()
        else:
            temp_list = random.choices(list2)
            # Since 'random.choices' return a list, I must convert the list into a string
            random_word = ""
            for i in temp_list:
                random_word += i
            return random_word.capitalize()

    # Generator WEAK PASSWORD
    def weak_password_generator(random_word):
        characters_counter = len(random_word)
        weak_password = random_word

        # Ask user wheter include symbols or not
        special = include_symbols()

        # a-z, A-Z, 0-9
        while characters_counter < amount_characters:
            if special.startswith("y"):
                weak_password += random.choice(string.digits + string.punctuation)
            else:
                weak_password += random.choice(string.digits)
            characters_counter += 1

        return weak_password

    # Generator STRONG PASSWORD logic
    def strong_password_generator():
        characters_counter = 0
        password = ""

        # a-z, A-Z, 0-9
        while characters_counter < amount_characters:
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
            characters_counter += 1

        return password

    def check_path(password_type):
        if password_type.lower() == "weak":
            random_word = weak_random_word()
            weak_password = weak_password_generator(random_word)
            print("Ok. Wait a second while I create a WEAK PASSWORD...")
            time.sleep(2)
            print(weak_password)
        else:
            strong_password = strong_password_generator()
            print("Ok. Wait a second while I create a STRONG PASSWORD...")
            time.sleep(2)
            print(strong_password)

    amount_characters = password_length()
    password_type = password_strength()
    check_path(password_type)

if __name__ == "__main__":
    main()