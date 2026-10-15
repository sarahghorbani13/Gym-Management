from services.halls_management import Halls
from models.coach import CoachManager


class Classes:
    def __init__(self,halls):
        self.halls = halls
        self.classes_list = []

    def add(self, name, sport, coach_id, hall, day, time, capacity):
        for cls in self.classes_list:
            if cls["name"] == name:
                print("\nthis class already exists!\n")
                return

        if hall not in self.halls.enable_halls():
            print(f"\n{hall} does not exist or is not enable!\n")
            return

        try:
            coach = CoachManager().get_by_id(coach_id)
        except LookupError:
            print(f"\ncoach {coach_id} not found!\n")
            return

        if not coach.is_active:
            print("\ncoach is not enable.\n")
            return

        try:
            capacity = int(capacity)
        except (TypeError, ValueError):
            print("\ninvalid capacity!\n")
            return

        new_cls = {
            "name": name,
            "sport": sport,
            "coach": coach.name,
            "coach_id": coach.coach_id,
            "hall": hall,
            "day": day,
            "time": time,
            "capacity": capacity,
            "register": 0,
            "status": True,
        }
        self.classes_list.append(new_cls)

    def edit(self):
        if not self.classes_list:
            print("\nno classes!\n")
            return

        edit_name = input("\nname of class to edit : ").strip()
        for cls in self.classes_list:
            if cls["name"] == edit_name:
                new_name = input("\nnew name : ").strip()
                new_sport = input("\nnew sport : ").strip()
                new_coach = input("\nnew coach id : ").strip()

                try:
                    coach = CoachManager().get_by_id(new_coach)
                except LookupError:
                    print(f"\ncoach {new_coach} not found!\n")
                    return

                if not coach.is_active:
                    print("\ncoach is not enable.\n")
                    return

                new_hall = input("\nnew hall : ").strip()
                hall_method = Halls()
                if new_hall not in hall_method.enable_halls():
                    print(f"\n{new_hall} does not exist or is not enable!\n")
                    return

                new_day = input("\nnew day : ").strip()
                new_time = input("\nnew time : ").strip()
                new_capacity = input("\nnew capacity : ").strip()

                try:
                    new_capacity = int(new_capacity)
                except (TypeError, ValueError):
                    print("\ninvalid capacity!\n")
                    return

                cls["name"] = new_name
                cls["sport"] = new_sport
                cls["coach"] = coach.name
                cls["coach_id"] = coach.coach_id
                cls["hall"] = new_hall
                cls["day"] = new_day
                cls["time"] = new_time
                cls["capacity"] = new_capacity
                return

        print(f"\n{edit_name} is not in classes\n")

    def view(self):
        if not self.classes_list:
            print("\nno classes!\n")
            return

        for cls in self.classes_list:
            if cls["status"]:
                remain_capacity = int(cls["capacity"]) - int(cls["register"])
                print(
                    f"\nname:{cls['name']}\n"
                    f"sport:{cls['sport']}\n"
                    f"coach:{cls['coach']}\n"
                    f"hall:{cls['hall']}\n"
                    f"day:{cls['day']}\n"
                    f"time:{cls['time']}\n"
                    f"capacity:{cls['capacity']}\n"
                    f"remaincapacity:{remain_capacity}\n"
                    f"status:{cls['status']}\n"
                )

    def classes_status(self):
        if not self.classes_list:
            print("\nno classes!\n")
            return

        name_to_toggle = input("\nwhich class do you want to enable/disable? ").strip()
        for cls in self.classes_list:
            if cls["name"] == name_to_toggle:
                cls["status"] = not cls["status"]
                text = "Enabled" if cls["status"] else "Disabled"
                print(f"\n{cls['name']} is {text}\n")
                return

        print(f"\n{name_to_toggle} is not in classes\n")

    def enable_classes(self):
        enable_list = []
        for cls in self.classes_list:
            if cls["status"]:
                enable_list.append(cls["name"])
        return enable_list