
from .exercise_editor import show_exercises
from .workout_service import load_plan
from member.enrollments import active_class_ids, is_enrolled


def _get(item, key):
    return item.get(key) if isinstance(item, dict) else getattr(item, key, None)


def _choose_class(classes):
    while True:
        print('\nYour active classes:')
        for index, gym_class in enumerate(classes, 1):
            print(f"{index}. {_get(gym_class, 'name') or 'Unnamed class'}")
        raw = input('Select a class (0: Back): ').strip()
        if raw == '0':
            return None
        if raw.isdecimal() and 1 <= int(raw) <= len(classes):
            return classes[int(raw) - 1]
        print('Invalid class selection.')


def view_my_workout_plans(member, classes):

    if _get(member, 'role') != 'member' or _get(member, 'is_active') is not True:
        raise PermissionError('An active member account is required.')
    member_id = _get(member, 'user_id')
    if member_id is None:
        raise ValueError('Member account has no stable user ID.')

    class_ids = set(active_class_ids(member_id))
    visible = [gym_class for gym_class in classes
               if (str(_get(gym_class, 'class_id')) in class_ids
                   and _get(gym_class, 'status') is True)]
    if not visible:
        print('You have no active class enrollments.')
        return

    while True:
        gym_class = _choose_class(visible)
        if gym_class is None:
            return
        class_id = _get(gym_class, 'class_id')

        if not is_enrolled(member_id, class_id):
            print('Your enrollment is no longer active.')
            continue
        try:
            plan = load_plan(class_id, member_id)
        except (ValueError, OSError) as error:
            print(f'Unable to load workout plan: {error}')
            continue
        if plan is None:
            print('No workout plan has been assigned for this class.')
        else:
            print('\nYour workout plan:')
            show_exercises(plan.exercises)
