from services.reports import (
    manager_activate_subscription,
    show_all_active_subscriptions,
    show_income_by_subscription_type,
    show_total_income,
)
from services.user_management import add_user, edit_user, toggle_user, view_users
from services.view_users import export_users


def manager_panel(wallets, catalog, halls, classes, users):
    while True:
        print("\n***** Manager Control Panel ***")
        print("------------------------------------")
        print("1: Manage Users")
        print("2: Manage Halls")
        print("3: Manage Classes")
        print("4: Subscriptions & Payments")
        print("5: Reports")
        print("6: Back to Main Menu")
        print("------------------------------------")

        try:
            choice = input("Please enter your chosen section: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        try:
            if choice == "1":
                _manage_users(users)
            elif choice == "2":
                _manage_halls(halls)
            elif choice == "3":
                _manage_classes(classes)
            elif choice == "4":
                _manage_subscriptions(wallets, catalog)
            elif choice == "5":
                _manage_reports(wallets)
            elif choice == "6":
                return
            else:
                print("Invalid Option! Please enter a number between 1 to 6.")
        except Exception as error:
            print(f"Unexpected error: {error}")
            print("Returning to manager panel...")


def _manage_users(users):
    while True:
        print("\n--- User Management ---")
        print("1: Add user")
        print("2: Edit user")
        print("3: Toggle active status")
        print("4: View users")
        print("5: Export users to file")
        print("6: Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_user(users)
        elif choice == "2":
            edit_user(users)
        elif choice == "3":
            toggle_user(users)
        elif choice == "4":
            view_users(users)
        elif choice == "5":
            export_users(users)
        elif choice == "6":
            return
        else:
            print("Invalid choice !")


def _manage_halls(halls):
    while True:
        print("\n--- Hall Management ---")
        print("1: Add hall")
        print("2: Edit hall")
        print("3: View halls")
        print("4: Enable / Disable hall")
        print("5: Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input("Hall name: ").strip()
            capacity = input("Capacity: ").strip()
            equipment = input("Equipment: ").strip()
            halls.add(name, capacity, equipment)
        elif choice == "2":
            halls.edit()
        elif choice == "3":
            halls.view()
        elif choice == "4":
            halls.halls_status()
        elif choice == "5":
            return
        else:
            print("Invalid choice !")


def _manage_classes(classes):
    while True:
        print("\n--- Class Management ---")
        print("1: Add class")
        print("2: Edit class")
        print("3: View classes")
        print("4: Enable / Disable class")
        print("5: Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input("Class name: ").strip()
            sport = input("Sport: ").strip()
            coach_id = input("Coach ID: ").strip()
            hall = input("Hall name: ").strip()
            day = input("Day: ").strip()
            time = input("Time: ").strip()
            capacity = input("Capacity: ").strip()
            classes.add(name, sport, coach_id, hall, day, time, capacity)
        elif choice == "2":
            classes.edit()
        elif choice == "3":
            classes.view()
        elif choice == "4":
            classes.classes_status()
        elif choice == "5":
            return
        else:
            print("Invalid choice !")


def _manage_subscriptions(wallets, catalog):
    while True:
        print("\n--- Subscriptions & Payments ---")
        print("1: Activate / Renew subscription for member")
        print("2: Show all active subscriptions")
        print("3: Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            manager_activate_subscription(wallets, catalog)
        elif choice == "2":
            show_all_active_subscriptions(wallets)
        elif choice == "3":
            return
        else:
            print("Invalid choice !")


def _manage_reports(wallets):
    while True:
        print("\n--- Reports ---")
        print("1: Income by subscription type")
        print("2: Total income")
        print("3: Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            show_income_by_subscription_type(wallets)
        elif choice == "2":
            show_total_income(wallets)
        elif choice == "3":
            return
        else:
            print("Invalid choice !")