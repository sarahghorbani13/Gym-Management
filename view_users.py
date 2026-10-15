def view_users(users):
    with open("users.txt", "w", encoding="utf-8") as file:
        for user in users:
            file.write(f"Username: {user.username}\n")
            file.write(f"Email: {user.email}\n")
            file.write(f"Active: {user.is_active}\n")
            file.write("--------------------\n")
    with open("users.txt", "r", encoding="utf-8") as file:
        print(file.read())