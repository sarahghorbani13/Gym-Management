from models import User
from validators import validate_password, validate_email, is_username_unique
def add_user(users):
    while True:
        username = input("Username (0 to cancel): ").strip()
        if username == "0":
            return
        if not is_username_unique(username, users):
            print("Username already exists.")
        else:
            break
    while True:
        password = input("Password: ")
        if not validate_password(password):
            print("Invalid password.")
        else:
            break
    while True:
        email = input("Email: ").strip()
        if not validate_email(email):
            print("Invalid email.")
        else:
            break
    users.append(User(username, password, email, True))
    print("User added successfully.")
def edit_user(users):
    username = input("Username: ")
    for user in users:
        if user.username == username:
            new_name = input("New name (blank to keep): ").strip()
            if new_name:
                user.name = new_name
            new_email = input("New email (blank to keep): ").strip()
            if new_email:
                if validate_email(new_email):
                    user.email = new_email
                    print("Email updated.")
                else:
                    print("Invalid email.")
                    return
            new_password = input("New password (blank to keep): ")
            if new_password:
                if validate_password(new_password):
                    user.password = new_password
                    print("Password updated.")
                else:
                    print("Invalid password.")
                    return
            print("User updated.")
            return
    print("User not found.")
def set_user_status(users):
    username = input("Username: ")
    for user in users:
        if user.username == username:
            status = input("Enter active or inactive: ").lower()
            if status == "active":
                user.is_active = True
            elif status == "inactive":
                user.is_active = False
            else:
                print("Invalid status.")
                return
            print("Status changed.")
            return
    print("User not found.")
def view_users(users):
    for user in users:
        print(user.username, user.email, user.is_active)
