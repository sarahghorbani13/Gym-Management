from Exceptions import validation_error


def create_exercise(name, sets, reps, rest, description=""):
    if name.strip() == "" or sets <= 0 or reps <= 0 or rest < 0:
        raise validation_error()

    return {
        "name": name.strip(),
        "sets": sets,
        "reps": reps,
        "rest": rest,
        "description": description,
    }