from Coach import Coach, CoachManager


def seed_coaches():
    manager = CoachManager()

    if manager.get_all():
        print("اطلاعات مربی‌ها از قبل وجود دارد")
        return

    coaches = [
        Coach(1, "Ali Ahmadi", "Bodybuilding"),
        Coach(2, "Sara Mohammadi", "Fitness"),
    ]

    for coach in coaches:
        manager.add(coach)

    print("اطلاعات اولیه مربی‌ها ساخته شد")


if __name__ == "__main__":
    seed_coaches()