from utils.Exceptions import validation_error


def create_exercise(name, sets, reps, rest, description=""):
    if not isinstance(name, str) or not name.strip():
        raise validation_error()
    if any(type(x) is not int for x in (sets, reps, rest)):
        raise validation_error()
    if sets <= 0 or reps <= 0 or rest < 0:
        raise validation_error()
    if not isinstance(description, str):
        raise validation_error()

    return {
        "name": name.strip(),
        "sets": sets,
        "reps": reps,
        "rest": rest,
        "description": description,
    }