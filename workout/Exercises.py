from Exceptions import validation_error


class Exercise:

    def __init__(self, name, sets, reps, rest, description=""):
        if name.strip() == "" or sets <= 0 or reps <= 0 or rest < 0:
            raise validation_error()

        self.name = name.strip()
        self.sets = sets
        self.reps = reps
        self.rest = rest
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "rest": self.rest,
            "description": self.description,
        }