import os
import tempfile
from pathlib import Path
from models.exercise import create_exercise
from models.workout_plan import workout_plan
from utils.Exceptions import storage_error, validation_error

FILE_PATH = Path(__file__).resolve().parent.parent / "workout_plans.txt"


def read_lines():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return [line for line in file.read().splitlines() if line.strip()]
    except FileNotFoundError:
        return []
    except OSError as error:
        raise storage_error() from error


def write_lines_safely(lines):
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=FILE_PATH.parent,
            prefix="workout_", delete=False
        ) as file:
            temporary_path = file.name
            for line in lines:
                file.write(line + "\n")
        os.replace(temporary_path, FILE_PATH)
    except OSError as error:
        if temporary_path and os.path.exists(temporary_path):
            os.unlink(temporary_path)
        raise storage_error() from error


def clean(text):
    return str(text).replace("|", "/")


def parsed_parts(line):
    parts = line.split("|")
    if len(parts) != 7:
        raise storage_error()
    return parts


def get_workout_plan(class_id, member_id):
    plan = None
    try:
        for line in read_lines():
            parts = parsed_parts(line)
            if parts[0] == str(class_id) and parts[1] == str(member_id):
                if plan is None:
                    plan = workout_plan(class_id, member_id)
                exercise = create_exercise(parts[2], int(parts[3]), int(parts[4]), int(parts[5]), parts[6])
                plan.exercises.append(exercise)
    except ValueError:
        raise storage_error()
    return plan


def save_workout_plan(plan):
    if not plan.exercises:
        raise validation_error()

    new_lines = []

    for line in read_lines():
        parts = parsed_parts(line)
        if parts[0] == str(plan.class_id) and parts[1] == str(plan.member_id):
            continue
        new_lines.append(line)

    for e in plan.exercises:
        try:
            exercise = create_exercise(e["name"], e["sets"], e["reps"], e["rest"], e["description"])
        except (KeyError, TypeError, AttributeError):
            raise validation_error()
        line = "|".join([
            str(plan.class_id),
            str(plan.member_id),
            clean(exercise["name"]),
            str(exercise["sets"]),
            str(exercise["reps"]),
            str(exercise["rest"]),
            clean(exercise["description"]),
        ])
        new_lines.append(line)

    write_lines_safely(new_lines)
