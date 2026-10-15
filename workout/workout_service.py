from copy import deepcopy
from .workout_plan import WorkoutPlan
from .workout_storage import get_workout_plan, save_workout_plan
from .exercises import create_exercise

def validate_exercises(exercises):

    if not isinstance(exercises, list) or not exercises:
        raise ValueError("A workout plan must contain at least one exercise.")

    validated = []
    for exercise in exercises:
        if not isinstance(exercise, dict):
            raise ValueError("Each exercise must be a dictionary.")
        try:
            validated.append(create_exercise(
                exercise["name"],
                exercise["sets"],
                exercise["reps"],
                exercise["rest"],
                exercise.get("description", ""),
            ))
        except (KeyError, TypeError, AttributeError) as exc:
            raise ValueError("Invalid exercise data.") from exc
    return validated

def load_plan(class_id, member_id):

    return get_workout_plan(class_id, member_id)

def save_plan(class_id, member_id, exercises, *, access_check):

    if class_id is None or member_id is None:
        raise ValueError("Class ID and member ID are required.")
    if not callable(access_check) or access_check(class_id, member_id) is not True:
        raise PermissionError("Not authorized to manage this workout plan.")

    validated = validate_exercises(exercises)
    plan = WorkoutPlan(class_id, member_id, deepcopy(validated))
    save_workout_plan(plan)
    return plan
