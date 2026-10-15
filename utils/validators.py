import re


def validate_password(password):
    if not isinstance(password, str):
        return False

    has_letter = re.search(r"[A-Za-z]", password)
    has_number = re.search(r"[0-9]", password)
    has_symbol = re.search(r"[@&]", password)

    return bool(has_letter and has_number and has_symbol)


def validate_email(email):
    if not isinstance(email, str):
        return False

    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


def is_username_unique(username, users):
    if not isinstance(username, str):
        return False

    for user in users:
        if user.username == username:
            return False

    return True