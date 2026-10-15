from copy import deepcopy

from .exercise_input import get_exercise, get_positive_int, get_text


def show_exercises(exercises):

    if not exercises:
        print("No exercise in the list")
        return

    for number, exercise in enumerate(exercises, start=1):
        print(
            f"{number}. {exercise['name']} | "
            f"Set: {exercise['sets']} | Rep: {exercise['reps']} | "
            f"Rest: {exercise['rest']} seconds | "
            f"تDescription: {exercise['description'] or '-'}"
        )


def choose_exercise(exercises):

    if not exercises:
        print("No exercise to be selected.")
        return None

    while True:
        show_exercises(exercises)
        raw = input("Enter exercise number (0: Return): ").strip()

        if raw == "0":
            return None

        try:
            number = int(raw)
        except ValueError:
            print("Number must be integer")
            continue

        if 1 <= number <= len(exercises):

            return number - 1

        print("Entered number is not in the list.")


def edit_exercise(exercise):

    updated = exercise.copy()

    while True:
        print("\nEdit exercise:", updated['name'])
        print("1: Name | 2: Set | 3: Repition | 4: Rest | 5: Descriotion")
        print("6: Confirm edition | 0: Cancel edition")
        choice = input("Option: ").strip()

        if choice == "0":
            return None

        if choice == "6":
            return updated

        if choice == "1":
            value = get_text("New Name (0: cancel): ")
            key = "name"
        elif choice == "2":
            value = get_positive_int("New Set (0: cancel): ")
            key = "sets"
        elif choice == "3":
            value = get_positive_int("تکرار جدید (0: cancel): ")
            key = "reps"
        elif choice == "4":
            value = get_positive_int("New rest duration (0: cancel): ")
            key = "rest"
        elif choice == "5":
            value = get_text("New description (can be empty، 0: Cancel): ", required=False)
            key = "description"
        else:
            print("Invalid option")
            continue

        if value is None:

            print("Edition cancelled")
            continue

        updated[key] = value
        print("The new value has been temporarily recorded; press 6 to confirm.")


def manage_exercises(existing=None):

    exercises = deepcopy(existing) if existing is not None else []

    while True:
        print("\n--- Training Program Exercises Management ---")
        print("1: View | 2: Add: Edit | 4: Delete")
        print("5: Confirm List | 0: Cancel all editions")
        choice = input("Option: ").strip()

        if choice == "0":
            return None

        if choice == "1":
            show_exercises(exercises)
            continue

        if choice == "2":
            exercise = get_exercise()
            if exercise is not None:
                exercises.append(exercise)
                print("Exercise added (not yet saved to the file).")
            continue

        if choice == "3":
            index = choose_exercise(exercises)
            if index is None:
                continue
            updated = edit_exercise(exercises[index])
            if updated is not None:
                exercises[index] = updated
                print("ویرایش حرکت تأیید شد.")
            continue

        if choice == "4":
            index = choose_exercise(exercises)
            if index is None:
                continue
            confirm = input("To delete the move, enter y: ").strip().lower()
            if confirm == "y":
                removed = exercises.pop(index)
                print(f"Exercise {removed['name']} Removed (only from the temporary list).")
            else:
                print("Deletion cancelled")
            continue

        if choice == "5":
            if not exercises:
                print("The program must have at least one exercise.")
                continue
            return exercises

        print("Invalid option")


if __name__ == "__main__":

    result = manage_exercises()
    if result is None:
        print("تغییرات لغو شد؛ داده‌ای ذخیره نشد.")
    else:
        print("فهرست نهایی آماده ارسال به بخش ذخیره‌سازی است:")
        show_exercises(result)
