from utils.Exceptions import storage_error


def export_users(users, path="users.txt"):
    try:
        with open(path, "w", encoding="utf-8") as file:
            for user in users:
                file.write(f"Username: {user.username}\n")
                file.write(f"Email: {user.email}\n")
                file.write(f"Active: {user.is_active}\n")
                file.write("-" * 20 + "\n")
    except OSError as error:
        raise storage_error() from error

    try:
        with open(path, "r", encoding="utf-8") as file:
            print(file.read())
    except OSError as error:
        raise storage_error() from error