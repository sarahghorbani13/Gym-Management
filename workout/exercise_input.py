def get_text(prompt, required=True):
    while True:

        value = input(prompt).strip()

        if value == "0":
            return None


        if value or not required:
            return value

        print("This field can not be empty. Try again.")


def get_positive_int(prompt):

    while True:
        raw_value = input(prompt).strip()


        if raw_value == "0":
            return None

        try:
            number = int(raw_value)
        except ValueError:

            print("Please enter an integer number.")
            continue

        if number > 0:
            return number

        print("The number must be positive")


def get_exercise():

    name = get_text("Exercise name (0 to cancel):")
    if name is None:
        return None

    sets = get_positive_int("Exercise sets (0 to cancel):")
    if sets is None:
        return None

    reps = get_positive_int("Exercise repitition (0 to cancel):")
    if reps is None:
        return None

    rest = get_positive_int("Exercise rest (0 to cancel):")
    if rest is None:
        return None

    description = get_text("description (0 to cancel):", required=False)
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
        print("\n1: Add exercise | 2: Finish and view the list | 0 : Cancel")
        choice = input("Option: ").strip()

        if choice == "0":

            return None

        if choice == "2":
            if not exercises:
                print("Please add at least 1 exercise")
                continue
            return exercises

        if choice == "1":
            exercise = get_exercise()
            if exercise is None:

                print("Operation cancelled")
                continue
            exercises.append(exercise)
            print("exercise added to the list.")
            continue

        print("Invalid option")


if __name__ == "__main__":

    result = get_exercises()
    if result is None:
        print("عملیات لغو شد؛ اطلاعاتی ذخیره نشد.")
    else:
        print("فهرست حرکات آماده است:")
        for index, exercise in enumerate(result, start=1):
            print(f"{index}. {exercise}")
