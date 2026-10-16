from panels.manager_panel import manager_panel
from panels.member_panel import member_panel
from services.wallet import Wallet
from data.subscription_catalog import catalog
from models.coach import CoachPanel, CoachManager
from services.classes_management import Classes
from services.halls_management import Halls
from models.user import Manager, Trainer, Member


def manager_cp(wallets, users, halls, classes):
    try:
        manager_panel(wallets, catalog, halls, classes, users)
    except (EOFError, KeyboardInterrupt):
        print("\nReturning to main menu.")
        return


def trainer_cp(class_manager, members):
    try:
        coach_manager = CoachManager()
        coaches = coach_manager.get_all()

        if not coaches:
            print("No coaches available.")
            return

        print("\n--- Coaches ---")
        for i, coach in enumerate(coaches, 1):
            print(f"{i}. {coach.name} ({coach.specialty})")

        raw = input("Choose a coach number (0: back): ").strip()
        if raw == "0":
            return

        try:
            index = int(raw)
        except ValueError:
            print("Invalid input !")
            return

        if index < 1 or index > len(coaches):
            print("Invalid choice !")
            return

        coach = coaches[index - 1]
        panel = CoachPanel(coach, class_manager, members)
        panel.run()

    except (EOFError, KeyboardInterrupt):
        print("\nReturning to main menu.")
        return
    except Exception as error:
        print(f"Unexpected error: {error}")


def member_dashboard(wallets,user):
    member_Wallet = None
    for w in wallets:
        if w.username == user.username:
            member_Wallet = w
            break

    if not member_Wallet:
        print("No wallet found for this member!")
        return

    try:
        member_panel(member_Wallet,catalog)
    except(EOFError, KeyboardInterrupt):
        print("\nReturning to main menu")
        return
    except Exception as error:
        print(f"Unexpected error: {error}")
    

def login(users, role):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            username = input("\nUsername: ").strip()
            password = input("\nPassword: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return None

        for user in users:
            if user.username == username and user.password == password:

                if user.role == role:
                    print(f"\nWelcome, {user.name}!\n")
                    return user
                else:
                    print(f"\nYou are not a {role}!")
                    return None

        remaining_attempts = max_attempts - attempt - 1
        if remaining_attempts > 0:
            print(f"\nInvalid Entry! you have {remaining_attempts} attempts left.")
        else:
            print("\nToo many failed attempts.")
            return None

    return None

def main_menu():
    users = [
        Manager("Manager", "manager", "Manager@1", "manager@gym.com"),
        Trainer("Trainer", "trainer", "Trainer@1", "trainer@gym.com"),
        Member("Member", "member", "Member@1", "member@gym.com"),
    ]

    wallets = [
        Wallet(3, "member", 1000000),
    ]

    halls = Halls()
    halls.add("red", "10", "dumbbell , mat")
    halls.add("green", "15", "mat, treadmill")
    halls.add("blue", "20", "yoga block, mat")

    classes = Classes(halls)

    while True:
        print("""
                ***** Welcome to Quera Gym! ***
                ------------------------------------
                1: Management
                2: Trainers
                3: Members
                4: Exit
                ------------------------------------
                """)

        try:
            choice = input("Please enter the chosen panel number: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting the program. Hope to see you again soon!")
            return

        try:
            if choice == "1":
                user = login(users,"manager")
                if user:
                    manager_cp(wallets, users, halls, classes)

            elif choice == "2":
                user = login(users,"trainer")
                if user:
                    trainer_cp(classes, users)

            elif choice == "3":
                user = login(users,"member")
                if user:
                    member_dashboard(wallets,user
                                     )
            elif choice == "4":
                print("Exiting the program, Hope to see you again soon!")
                return
            
            else:
                print("Invalid choice! Please enter a number between 1 to 4.")

        except Exception as error:
            print(f"Unexpected error: {error}")
            print("Returning to main menu...")
