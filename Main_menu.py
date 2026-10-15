def manager_cp(): # cp = control panel

    while True:
        print("Dear Manager! Welcome to your panel!")
        print("""
***** Manager Control Panel ***
------------------------------------
1: Manage Users
2: Manage Venues
3: Manage Courses
4: Subscriptions & Payments
5: Reports
6: Back to Main Menu
------------------------------------
""")
        choice = input("Please enter your chosen section:")

        if choice == "1":
            print("User Managment Section\nPlease enter the user type chosen:")

        elif choice == "2":
            print("Venue Managment Section\nPlease enter your chosen section")

        elif choice == "3":
            print("Course Management Section\nPlease enter your chosen section:")

        elif choice == "4":
            print("Subscriptions & Payments Management Section\nPlease enter your chosen section:")

        elif choice == "5":
            print("Reports Section\nPlease enter your chosen section:")

        elif choice == "6":
            return
        
        else:
            print("Invalid Option! Please enter a number between 1 to 6.")
                
        # if choice == "1":
        #     manager_activate_subscription(wallets, catalog)
        # elif choice == "2":
        #     show_all_active_subscriptions(wallets)
        # elif choice == "3":
        #     show_income_by_subscription_type(wallets)
        # elif choice == "4":
        #     show_total_income(wallets)
        # elif choice == "5":
        #     break
        # else:
        #     print("Invalid choice !")

def trainer_cp():
    
    while True:
            print("Dear Trainer! Welcome to your Panel!")
            print("""
    ***** Trainer Control Panel ***
    ------------------------------------
    1: View Courses
    2: Workout Plans
    3: Back to Main Menu
    ------------------------------------
    """)
            choice = input("Please enter your chosen section:")
    
            if choice == "1":
                print("Courses Section\nTo view your courses,Please enter your chosen course:")

            elif choice == "2":
                print("Workout Plans\nPlease enter your chosen section:")

            elif choice == "3":
                return
            
            else:
                print("Invalid Option! Please enter a number between 1 to 3.")

def member_dashboard():

    while True:
            print("Dear Member! Welcome to your panel!")
            print("""
    ***** Member Dashboard ***
    ------------------------------------
    1: Profile & Subscriptions
    2: Wallet
    3: Payments
    4: Courses
    5: Workout Plans
    6: Back to Main Menu
    ------------------------------------
    """)
            choice = input("Please enter your chosen section:")
    
            if choice == "1":
                print("Profile & Subscriptions")

            elif choice == "2":
                print("Wallet")

            elif choice == "3":
                print("Payments")

            elif choice == "4":
                print("Courses")

            elif choice == "5":
                print("Workout Plans")

            elif choice == "6":
                return
            
            else:
                print("Invalid Option! Please enter a number between 1 to 6.")

def main_menu():
    
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
        choice = input("Please enter the chosen panel number:")

        if choice == "1":
            manager_cp()
        elif choice == "2":
            trainer_cp()
        elif choice == "3":
            member_dashboard()
        elif choice == "4":
            print("Exiting the program, Hope to see you again soon!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 to 4.")

    main_menu()