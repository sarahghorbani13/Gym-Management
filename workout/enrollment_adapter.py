from member.enrollments import active_member_ids, is_enrolled
from .workout_manager import _field, _coach_owns_class, make_workout_handler


def eligible_members(coach, gym_class, users):

    if not _coach_owns_class(coach, gym_class):
        return []
    class_id = _field(gym_class, 'class_id')
    if class_id is None:
        return []
    ids = set(active_member_ids(class_id))
    return [user for user in users
            if _field(user, 'role') == 'member'
            and _field(user, 'is_active') is True
            and _field(user, 'user_id') is not None
            and str(_field(user, 'user_id')) in ids]


def can_manage_workout(coach, class_id, member_id, classes, users):

    member_is_active = any(
        _field(user, 'role') == 'member'
        and _field(user, 'is_active') is True
        and _field(user, 'user_id') is not None
        and str(_field(user, 'user_id')) == str(member_id)
        for user in users
    )
    return bool(member_is_active and is_enrolled(member_id, class_id) and any(
        str(_field(gym_class, 'class_id')) == str(class_id)
        and _coach_owns_class(coach, gym_class)
        for gym_class in classes
    ))


def build_coach_workout_handler(classes, users):

    return make_workout_handler(
        eligible_members=lambda coach, gym_class: eligible_members(coach, gym_class, users),
        access_check=lambda coach, class_id, member_id: can_manage_workout(
            coach, class_id, member_id, classes, users
        ),
    )