from modules.reports import (
    manager_activate_subscription,
    show_all_active_subscriptions,
    show_income_by_subscription_type,
    show_total_income,
)


def manager_panel(wallets, catalog):

    while True:
        # منوی گزینه‌ها رو چاپ می‌کنیم
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

        # انتخاب مدیر رو می‌گیریم
        choice = input("Please enter your chosen section:")

        # بر اساس انتخاب، تابع مربوطه رو صدا می‌زنیم
        if choice == "1":
                print("User Managment Section\nPlease enter the user type chosen:")
        #محل فراخوانی User management و view users

        elif choice == "2":
            print("Venue Managment Section\nPlease enter your chosen section")
        #محل فراخوانی Hall management

        elif choice == "3":
            print("Course Management Section\nPlease enter your chosen section:")
        #محل فراخوانی class managment

        elif choice == "4":
            print("Subscriptions & Payments Management Section\nPlease enter your chosen section:")
        #محل فراخوانی اشتراک ها

        elif choice == "5":
            print("Reports Section\nPlease enter your chosen section:")
        #محل فراخوانی گزارش 
            
        # در صورت انتخاب عدد شش به منوی اصلی باز میگردد
        elif choice == "6":
            return
                
        else:
            print("Invalid Option! Please enter a number between 1 to 6.")