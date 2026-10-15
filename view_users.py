def view_users(users):
    with open("users.txt", "w", encoding="utf-8") as file:
        for user in users:
            file.write(
                f"Name: {user.name} | Username: {user.username} | "
                f"Role: {user.role} | Email: {user.email} | Active: {user.is_active}\n"
            )
    with open("users.txt", "r", encoding="utf-8") as file:
        print(file.read())
