from models.coach import Coach, CoachManager


def seed_coaches():
    manager = CoachManager()

    if manager.get_all():
        print("Coach data already exists.")
        return

    coaches = [
        Coach(1, "Ali Ahmadi", "Bodybuilding"),
        Coach(2, "Sara Mohammadi", "Fitness"),
    ]

    for coach in coaches:
        manager.add(coach)

    print("Initial coach data created.")


if __name__ == "__main__":
    seed_coaches()
