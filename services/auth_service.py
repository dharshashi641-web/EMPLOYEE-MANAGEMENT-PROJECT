import json
from models.admin import Admin
def register():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    admin = Admin(username, password)

    user_data = {
        "username": admin.username,
        "password": admin.get_password()
    }

    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)

    except:
        data = []

    for user in data:

        if user["username"] == username:
            print("Username Already Exists")
            return

    data.append(user_data)

    with open("data/users.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Registration Successful")
def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)

        for user in data:

            if user["username"] == username and user["password"] == password:

                print("Login Successful")
                return True

        print("Invalid Username or Password")
        return False

    except FileNotFoundError:
        print("User File Not Found")
        return False

    except json.JSONDecodeError:
        print("JSON File Error")
        return False