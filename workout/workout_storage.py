import os
from utils.Exceptions import storage_error, validation_error
from workout_plan import workout_plan
FILE_PATH = "workout_plans.txt"


def read_lines():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def clean(text):
    return str(text).replace("|", "/")


def get_workout_plan(class_id, member_id):
    plan = None
    try:
        for line in read_lines():
            parts = line.split("|")
            if len(parts) != 7:
                raise storage_error()
            if parts[0] == str(class_id) and parts[1] == str(member_id):
                if plan is None:
                    plan = workout_plan(class_id, member_id)
                exercise = create_exercise(parts[2], int(parts[3]), int(parts[4]), int(parts[5]), parts[6])
                plan.exercises.append(exercise.to_dict())
    except ValueError:
        raise storage_error()
    return plan


def save_workout_plan(plan):
    new_lines = []

    for line in read_lines():
        parts = line.split("|")
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
            clean(exercise.name),
            str(exercise.sets),
            str(exercise.reps),
            str(exercise.rest),
            clean(exercise.description),
        ])
        new_lines.append(line)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line + "\n")