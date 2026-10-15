def get_text(prompt, required=True):
    while True:
        value = input(prompt).strip()

        if value == "0":
            return None

        if value or not required:
            return value

        print("This field cannot be empty. Try again.")


def get_positive_int(prompt):
    while True:
        raw_value = input(prompt).strip()

        if raw_value == "0":
            return None

        try:
            number = int(raw_value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if number > 0:
            return number

        print("Number must be greater than zero.")


def get_exercise():
    name = get_text("Exercise name (0: cancel): ")
    if name is None:
        return None

    sets = get_positive_int("Sets (0: cancel): ")
    if sets is None:
        return None

    reps = get_positive_int("Reps (0: cancel): ")
    if reps is None:
        return None

    rest = get_positive_int("Rest in seconds (0: cancel): ")
    if rest is None:
        return None

    description = get_text("Description (optional, 0: cancel): ", required=False)
    if description is None:
        return None

    return {
        "name": name,
        "sets": sets,
        "reps": reps,
        "rest": rest,
        "description": description,
    }


def get_exercises():
    exercises = []

    while True:
        print("\n1: Add exercise | 2: Finish | 0: Cancel all")
        choice = input("Choice: ").strip()

        if choice == "0":
            return None

        if choice == "2":
            if not exercises:
                print("Add at least one exercise first.")
                continue
            return exercises

        if choice == "1":
            exercise = get_exercise()
            if exercise is None:
                print("Exercise input cancelled.")
                continue
            exercises.append(exercise)
            print("Exercise added to the temporary list.")
            continue

        print("Invalid option.")


if __name__ == "__main__":
    result = get_exercises()
    if result is None:
        print("Operation cancelled; nothing was saved.")
    else:
        print("Exercise list is ready:")
        for index, exercise in enumerate(result, start=1):
            print(f"{index}. {exercise}")