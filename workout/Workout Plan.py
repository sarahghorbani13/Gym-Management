class WorkoutPlan:

    def __init__(self, class_id, member_id, exercises=None):
        self.class_id = class_id
        self.member_id = member_id
        if exercises is None:
            exercises = []
        self.exercises = exercises