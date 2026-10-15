def workout_plan(class_id, member_id, exercises=None):
    if exercises is None:
        exercises = []

    return {
        "class_id": class_id,
        "member_id": member_id,
        "exercises": exercises
    }