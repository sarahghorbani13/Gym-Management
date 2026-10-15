from models.user import User
from utils.validators import validate_password, validate_email, is_username_unique


def add_user(users):
    username = input("Username (0 to return): ").strip()

    if username == "0":
        return

    if not is_username_unique(username, users):
        print("Username already exists.")
        return

    password = input("Password: ").strip()
    email = input("Email: ").strip()

    if not validate_password(password) or not validate_email(email):
        print("Invalid password or email.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Invalid name.")
        return

    users.append(User(name, username, password, email, True))
    print("User added successfully.")


def edit_user(users):
    username = input("Username: ").strip()

    for user in users:
        if user.username == username:
            email = input("New email: ").strip()
            if validate_email(email):
                user.email = email
                print("Email updated.")
            else:
                print("Invalid email.")

            password = input("New password: ").strip()
            if validate_password(password):
                user.password = password
                print("Password updated.")
            else:
                print("Invalid password.")
            return

    print("User not found.")


def toggle_user(users):
    username = input("Username: ").strip()

    for user in users:
        if user.username == username:
            user.is_active = not user.is_active
            print("Status changed.")
            return

    print("User not found.")


def view_users(users):
    if not users:
        print("No users.")
        return

    for user in users:
        print(f"{user.username} | {user.email} | active: {user.is_active}")