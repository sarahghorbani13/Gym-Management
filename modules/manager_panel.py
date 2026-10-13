from modules.reports import (
    manager_activate_subscription,
    show_all_active_subscriptions,
    show_income_by_subscription_type,
    show_total_income,
)


def manager_panel(wallets, catalog):

    while True:
        # منوی گزینه‌ها رو چاپ می‌کنیم
        print(f"\n{10 * '='}\n Manager Panel \n{10 * '='}")
        print("1. Activate subscription for member")
        print("2. Show all active subscriptions")
        print("3. Show income by subscription type")
        print("4. Show total income")
        print("5. Back")
        print(f"{10 * '='}")

        # انتخاب مدیر رو می‌گیریم
        choice = input("Enter your choice : ")

        # بر اساس انتخاب، تابع مربوطه رو صدا می‌زنیم
        if choice == "1":
            manager_activate_subscription(wallets, catalog)
        elif choice == "2":
            show_all_active_subscriptions(wallets)
        elif choice == "3":
            show_income_by_subscription_type(wallets)
        elif choice == "4":
            show_total_income(wallets)
        elif choice == "5":
            break
        else:
            print("Invalid choice !")