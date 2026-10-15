def validation_error():
    return ValueError("Validation failed")


def duplicate_error():
    return ValueError("Duplicate input")


def authentication_error():
    return ValueError("Incorrect username or password")


def inactive_account_error():
    return PermissionError("User account is inactive")


def not_found_error():
    return LookupError("No user, class, or hall found with this ID")


def inactive_error():
    return PermissionError("The required section is inactive")


def capacity_full_error():
    return OverflowError("Capacity is full")


def payment_error():
    return ValueError("Payment failed")


def storage_error():
    return OSError("File is corrupted or invalid")