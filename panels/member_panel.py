def member_panel(wallet, catalog):
    while True:
        print(f"\n{10 * '='}\n Member Panel - {wallet.username} \n{10 * '='}")
        print("1. Show balance")
        print("2. Deposit wallet")
        print("3. Show transactions")
        print("4. Show my subscription status")
        print("5. Buy / Renew subscription")
        print("6. Back")
        print(f"{10 * '='}")

        try:
            choice = input("Enter your choice : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        try:
            if choice == "1":
                wallet.show_balance()
            elif choice == "2":
                wallet.deposit_wallet()
            elif choice == "3":
                wallet.show_transactions()
            elif choice == "4":
                wallet.show_subscription_status()
            elif choice == "5":
                wallet.pur_ren_subs(catalog)
            elif choice == "6":
                return
            else:
                print("Invalid choice !")
        except Exception as error:
            print(f"Unexpected error: {error}")
            print("Returning to member panel...")