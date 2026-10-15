from copy import deepcopy
from panels.exercise_input import get_exercise, get_positive_int, get_text


def show_exercises(exercises):
    if not exercises:
        print("No exercises in the list yet.")
        return

    for number, exercise in enumerate(exercises, start=1):
        print(
            f"{number}. {exercise['name']} | "
            f"sets: {exercise['sets']} | reps: {exercise['reps']} | "
            f"rest: {exercise['rest']} sec | "
            f"description: {exercise['description'] or '-'}"
        )


def choose_exercise(exercises):
    if not exercises:
        print("No exercises to choose from.")
        return None

    while True:
        show_exercises(exercises)
        raw = input("Enter exercise number (0: back): ").strip()

        if raw == "0":
            return None

        try:
            number = int(raw)
        except ValueError:
            print("Number must be an integer.")
            continue

        if 1 <= number <= len(exercises):
            return number - 1

        print("That number is not in the list.")


def edit_exercise(exercise):
    updated = exercise.copy()

    while True:
        print(f"\nEditing exercise: {updated['name']}")
        print("1: name | 2: sets | 3: reps | 4: rest | 5: description")
        print("6: confirm | 0: cancel")
        choice = input("Choice: ").strip()

        if choice == "0":
            return None

        if choice == "6":
            return updated

        if choice == "1":
            value = get_text("New name (0: cancel): ")
            key = "name"
        elif choice == "2":
            value = get_positive_int("New sets (0: cancel): ")
            key = "sets"
        elif choice == "3":
            value = get_positive_int("New reps (0: cancel): ")
            key = "reps"
        elif choice == "4":
            value = get_positive_int("New rest in seconds (0: cancel): ")
            key = "rest"
        elif choice == "5":
            value = get_text("New description (0: cancel): ", required=False)
            key = "description"
        else:
            print("Invalid option.")
            continue

        if value is None:
            print("Field was not changed.")
            continue

        updated[key] = value
        print("Value stored temporarily; press 6 to confirm.")


def manage_exercises(existing=None):
    exercises = deepcopy(existing) if existing is not None else []

    while True:
        print("\n--- Workout Exercise Manager ---")
        print("1: view | 2: add | 3: edit | 4: remove")
        print("5: confirm list | 0: cancel all changes")
        choice = input("Choice: ").strip()

        if choice == "0":
            return None

        if choice == "1":
            show_exercises(exercises)
            continue

        if choice == "2":
            exercise = get_exercise()
            if exercise is not None:
                exercises.append(exercise)
                print("Exercise added (not saved yet).")
            continue

        if choice == "3":
            index = choose_exercise(exercises)
            if index is None:
                continue
            updated = edit_exercise(exercises[index])
            if updated is not None:
                exercises[index] = updated
                print("Exercise edit confirmed.")
            continue

        if choice == "4":
            index = choose_exercise(exercises)
            if index is None:
                continue
            confirm = input("Type y to delete: ").strip().lower()
            if confirm == "y":
                removed = exercises.pop(index)
                print(f"Exercise {removed['name']} removed (temporary only).")
            else:
                print("Removal cancelled.")
            continue

        if choice == "5":
            if not exercises:
                print("A plan must have at least one exercise.")
                continue
            return exercises

        print("Invalid option.")


if __name__ == "__main__":
    result = manage_exercises()
    if result is None:
        print("Changes cancelled; nothing saved.")
    else:
        print("Final list ready for storage:")
        show_exercises(result)