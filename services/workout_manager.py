from .exercise_editor import manage_exercises, show_exercises
from .workout_service import load_plan, save_plan


def _field(item, *names):

    for name in names:
        if isinstance(item, dict) and name in item:
            return item[name]
        if not isinstance(item, dict) and hasattr(item, name):
            return getattr(item, name)
    return None


def _choose(items, title, describe):

    if not items:
        print("No available items.")
        return None
    while True:
        print(f"\n{title}")
        for number, item in enumerate(items, 1):
            print(f"{number}. {describe(item)}")
        raw = input("Choose a number (0: Back): ").strip()
        if raw == "0":
            return None
        try:
            number = int(raw)
        except ValueError:
            print("Enter a valid number.")
            continue
        if 1 <= number <= len(items):
            return items[number - 1]
        print("That number is not on the list.")


def _coach_owns_class(coach, gym_class):

    if _field(coach, "is_active") is not True:
        return False
    if _field(gym_class, "status") is not True:
        return False
    assigned = _field(gym_class, "coach_id", "coach")
    identities = (_field(coach, "coach_id", "user_id"), _field(coach, "name"))
    if assigned is None:
        return False
    return any(
        identity is not None
        and str(assigned).strip().casefold() == str(identity).strip().casefold()
        for identity in identities
    )


def run_workout_manager(coach, classes, members, *, eligible_members, access_check):

    if not callable(eligible_members) or not callable(access_check):
        raise TypeError("Enrollment and authorization callbacks are required.")

    permitted = [item for item in classes if _coach_owns_class(coach, item)]
    while True:
        gym_class = _choose(
            permitted, "Your active classes",
            lambda item: str(_field(item, "name", "title") or "Unnamed class"),
        )
        if gym_class is None:
            return
        class_id = _field(gym_class, "class_id", "id")
        if class_id is None:
            print("This class has no stable class ID. Contact the class manager.")
            continue

        enrolled = eligible_members(coach, gym_class)
        enrolled = list(enrolled) if enrolled is not None else []
        enrolled = [m for m in enrolled if _field(m, "member_id", "user_id", "id") is not None]
        member = _choose(
            enrolled, "Active enrolled members",
            lambda m: str(_field(m, "name", "username") or _field(m, "member_id", "user_id", "id")),
        )
        if member is None:
            continue
        member_id = _field(member, "member_id", "user_id", "id")

        def authorized(selected_class_id, selected_member_id):
            return (
                _coach_owns_class(coach, gym_class)
                and selected_class_id == class_id
                and selected_member_id == member_id
                and access_check(coach, selected_class_id, selected_member_id) is True
            )

        if not authorized(class_id, member_id):
            print("Access denied: enrollment or class ownership is not valid.")
            continue

        while True:
            print("\n1. View workout plan")
            print("2. Create or edit workout plan")
            print("0. Back to member selection")
            choice = input("Choose an option: ").strip()
            if choice == "0":
                break
            if choice not in ("1", "2"):
                print("Invalid option.")
                continue
            try:
                if not authorized(class_id, member_id):
                    print("Access denied: authorization has changed.")
                    break
                plan = load_plan(class_id, member_id)
                if choice == "1":
                    if plan is None:
                        print("No workout plan exists for this member in this class.")
                    else:
                        show_exercises(plan.exercises)
                    continue
                updated = manage_exercises(plan.exercises if plan else None)
                if updated is None:
                    print("Changes cancelled; nothing was saved.")
                    continue
                save_plan(class_id, member_id, updated, access_check=authorized)
                print("Workout plan saved successfully.")
            except (ValueError, PermissionError, OSError) as error:
                print(f"Operation failed: {error}")


def make_workout_handler(*, eligible_members, access_check):

    if not callable(eligible_members) or not callable(access_check):
        raise TypeError("Both callbacks must be callable.")

    def handler(coach, classes, members):
        return run_workout_manager(
            coach, classes, members,
            eligible_members=eligible_members,
            access_check=access_check,
        )

    return handler
