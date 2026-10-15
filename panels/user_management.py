from models import User
from validators import validate_password, validate_email, is_username_unique

def add_user(users):
    username = input("Username (0 to return): ")

    if username == "0":
        return
    
    if not is_username_unique(username, users):
        print("Username already exists.")
        return
    
    password = input("Password: ")
    email = input("Email: ")

    if not validate_password(password) or not validate_email(email):
        print("Invalid password or email.")
        return
    
    users.append(User(username, password, email, True))

    print("User added successfully.")

def edit_user(users):
    
    username = input("Username: ")
    for user in users:
        if user.username == username:
            email = input("New email: ")
            if validate_email(email):
                user.email = email
                print("User updated.")
            else:
                print("Invalid email.")
            password = input("New password: ")
            if validation_password(password):
                user.password = password
                print("Password updated.")
            else:
                print("Invalid password.")
            return
    print("User not found.")
def toggle_user(users):
    username = input("Username: ")
    for user in users:
        if user.username == username:
            user.is_active = not user.is_active
            print("Status changed.")
            return
    print("User not found.")
def view_users(users):
    for user in users:
        print(user.username, user.email, user.is_active)
