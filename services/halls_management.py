class Halls:
    def __init__(self):
        self.halls_list = []

    def add(self, name, capacity, equipment):
        for hall in self.halls_list:
            if hall["name"] == name:
                print("\nthis hall already exists!\n")
                return

        if capacity.isdigit() and int(capacity) >= 0:
            new_hall = {
                "name": name,
                "capacity": capacity,
                "equipment": equipment,
                "status": True,
            }
            self.halls_list.append(new_hall)
        else:
            print("\ninvalid type of capacity!\n")

    def edit(self):
        if not self.halls_list:
            print("\nno halls!\n")
            return

        edit_name = input("\nname of hall to edit : ").strip()
        for hall in self.halls_list:
            if hall["name"] == edit_name:
                new_capacity = input("\nnew capacity : ").strip()
                if new_capacity.isdigit() and int(new_capacity) >= 0:
                    new_equipment = input("\nnew equipment : ").strip()
                    hall["capacity"] = new_capacity
                    hall["equipment"] = new_equipment
                    return
                else:
                    print("\ninvalid type of capacity!\n")
                    return

        print(f"\n{edit_name} is not in halls\n")

    def view(self):
        if not self.halls_list:
            print("\nno halls!\n")
            return

        for hall in self.halls_list:
            print(
                f"\nname:{hall['name']}\n"
                f"capacity:{hall['capacity']}\n"
                f"equipment:{hall['equipment']}\n"
                f"status:{hall['status']}\n"
            )

    def halls_status(self):
        if not self.halls_list:
            print("\nno halls!\n")
            return

        name_to_toggle = input("\nwhich hall do you want to enable/disable? ").strip()
        for hall in self.halls_list:
            if hall["name"] == name_to_toggle:
                hall["status"] = not hall["status"]
                text = "Enabled" if hall["status"] else "Disabled"
                print(f"\n{hall['name']} is {text}\n")
                return

        print(f"\n{name_to_toggle} is not in halls\n")

    def enable_halls(self):
        enable_list = []
        for hall in self.halls_list:
            if hall["status"]:
                enable_list.append(hall["name"])
        return enable_list