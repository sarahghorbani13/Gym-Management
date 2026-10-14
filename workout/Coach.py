from Exceptions import (
    duplicate_error,
    inactive_account_error,
    not_found_error,
    storage_error,
)
from Storage import Storage


def log_action(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            with open("gym.log", "a", encoding="utf-8") as file:
                file.write(f"{func.__name__}: successful\n")
            return result
        except Exception:
            try:
                with open("gym.log", "a", encoding="utf-8") as file:
                    file.write(f"{func.__name__}: failed\n")
            except OSError:
                pass
            raise

    return wrapper


class Coach:
    def __init__(self, coach_id, name, specialty, is_active=True):
        self.coach_id = int(coach_id)
        self.name = name
        self.specialty = specialty
        self.is_active = is_active

    def get_info(self):
        return {
            "coach_id": self.coach_id,
            "name": self.name,
            "specialty": self.specialty,
            "is_active": self.is_active,
        }

    def to_row(self):
        return [
            self.coach_id,
            self.name,
            self.specialty,
            self.is_active,
        ]

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False


class CoachManager:
    def __init__(self, file_path="coaches.txt"):
        self.storage = Storage(file_path)

    def get_all(self):
        coaches = []

        for row in self.storage.load():
            if len(row) != 4:
                raise storage_error()

            coach_id, name, specialty, is_active = row

            try:
                coaches.append(
                    Coach(
                        coach_id,
                        name,
                        specialty,
                        is_active.strip().lower() == "true",
                    )
                )
            except (TypeError, ValueError) as error:
                raise storage_error() from error

        return coaches

    def get_by_id(self, coach_id):
        for coach in self.get_all():
            if coach.coach_id == int(coach_id):
                return coach

        raise not_found_error()

    def add(self, coach):
        coaches = self.get_all()

        if any(item.coach_id == coach.coach_id for item in coaches):
            raise duplicate_error()

        coaches.append(coach)
        self.storage.save([item.to_row() for item in coaches])

    def update_status(self, coach_id, is_active):
        coaches = self.get_all()

        for coach in coaches:
            if coach.coach_id == int(coach_id):
                if is_active:
                    coach.activate()
                else:
                    coach.deactivate()

                self.storage.save([item.to_row() for item in coaches])
                return coach

        raise not_found_error()


class CoachPanel:
    def __init__(
        self,
        coach,
        class_manager,
        members=None,
        workout_handler=None,
    ):
        self.coach = coach
        self.class_manager = class_manager
        self.members = members if members is not None else []
        self.workout_handler = workout_handler

    def _get_all_classes(self):
        if hasattr(self.class_manager, "classes_list"):
            return self.class_manager.classes_list

        if isinstance(self.class_manager, list):
            return self.class_manager

        return []

    def _is_my_class(self, gym_class):
        assigned_coach = gym_class.get("coach_id", gym_class.get("coach"))

        if assigned_coach is None:
            return False

        return (
            str(assigned_coach).strip().lower()
            in {
                str(self.coach.coach_id).strip().lower(),
                str(self.coach.name).strip().lower(),
            }
        )

    def _my_classes(self):
        return [
            gym_class
            for gym_class in self._get_all_classes()
            if self._is_my_class(gym_class)
            and gym_class.get("status", True)
        ]

    def _find_member(self, member_id):
        for member in self.members:
            current_id = member.get("member_id", member.get("id"))

            if str(current_id) == str(member_id):
                return member

        return None

    def _show_members(self, gym_class):
        registered = gym_class.get(
            "member_ids",
            gym_class.get("registered_members", gym_class.get("members")),
        )

        if registered is not None:
            if not registered:
                print("عضوی برای این کلاس ثبت‌نام نکرده است.")
                return

            for item in registered:
                if isinstance(item, dict):
                    print(
                        f"- {item.get('name', item.get('member_id', 'عضو ناشناس'))}"
                    )
                    continue

                member = self._find_member(item)

                if member:
                    print(f"- {member.get('name', 'نامشخص')}")
                else:
                    print(f"- شناسه عضو: {item}")

            return

        print(f"تعداد ثبت‌نام‌شده‌ها: {gym_class.get('register', 0)}")
        print("فهرست نام اعضا در اطلاعات فعلی کلاس موجود نیست.")

    @log_action
    def show_classes(self):
        classes = self._my_classes()

        if not classes:
            print("کلاسی برای شما ثبت نشده است.")
            return

        for gym_class in classes:
            print("-" * 35)
            print(
                f"عنوان: {gym_class.get('name', gym_class.get('title', 'نامشخص'))}"
            )
            print(
                f"نوع ورزش: {gym_class.get('sport', gym_class.get('sport_type', 'نامشخص'))}"
            )
            print(f"روز: {gym_class.get('day', 'نامشخص')}")
            print(f"ساعت: {gym_class.get('time', 'نامشخص')}")
            print(f"سالن: {gym_class.get('hall', 'نامشخص')}")
            print(f"ظرفیت: {gym_class.get('capacity', 'نامشخص')}")
            self._show_members(gym_class)

    def manage_workout_plans(self):
        if self.workout_handler is None:
            print("بخش برنامه تمرینی هنوز به پنل مربی متصل نشده است")
            return

        self.workout_handler(self.coach, self._my_classes(), self.members)

    def run(self):
        if not self.coach.is_active:
            raise inactive_account_error()

        while True:
            print("\n--- پنل مربی ---")
            print("1. مشاهده کلاس‌های خود")
            print("2. مدیریت برنامه تمرینی اعضا")
            print("3. خروج")

            choice = input("انتخاب شما: ").strip()

            if choice == "1":
                self.show_classes()
            elif choice == "2":
                self.manage_workout_plans()
            elif choice == "3":
                print("بازگشت به منوی شروع")
                break
            else:
                print("گزینه نامعتبر است")