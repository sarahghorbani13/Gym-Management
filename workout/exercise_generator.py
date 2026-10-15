

def iter_exercises(exercises, min_sets=1):

    for exercise in exercises:
        
        if exercise["sets"] >= min_sets:
            yield exercise


if __name__ == "__main__":

    sample_exercises = [
        {"name": "Squat", "sets": 3, "reps": 12, "rest": 60, "description": ""},
        {"name": "Plank", "sets": 1, "reps": 1, "rest": 30, "description": ""},
        {"name": "Push-up", "sets": 4, "reps": 10, "rest": 45, "description": ""},
    ]

    for exercise in iter_exercises(sample_exercises, min_sets=3):
        print(f"{exercise['name']}: {exercise['sets']} ست")
