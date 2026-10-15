from services.subscription import MemberSubscription


def manager_activate_subscription(wallets, catalog):

    if len(wallets) == 0:
        print("No members registered.")
        return

    print(f"\n{10 * '-*-'}\nMembers\n{10 * '-*-'}")
    i = 1
    for w in wallets:
        print(f"{i}. {w.username}")
        i = i + 1
    print(f"{10 * '-*-'}")

    try:
        choice = int(input("Choose a member number : "))
    except ValueError:
        print("Invalid input !")
        return

    if choice < 1 or choice > len(wallets):
        print("Invalid choice !")
        return

    wallet = wallets[choice - 1]

    if len(catalog) == 0:
        print("No subscriptions available.")
        return

    print(f"\n{10 * '-*-'}\nSubscriptions\n{10 * '-*-'}")
    i = 1
    for subs in catalog:
        print(f"{i}. {subs.name} | {subs.time} months | price: {subs.price}")
        i = i + 1
    print(f"{10 * '-*-'}")

    try:
        choice = int(input("Choose a subscription number : "))
    except ValueError:
        print("Invalid input !")
        return

    if choice < 1 or choice > len(catalog):
        print("Invalid choice !")
        return

    selected = catalog[choice - 1]
    duration = int(selected.time)

    current = wallet.subscription
    if current is not None and current.is_active:
        current.renew(duration)
        print(f"Subscription renewed for {wallet.username} ! "
              f"New end : {current.end_date}")
    else:
        new_subs = MemberSubscription(
            name=selected.name,
            duration_months=duration,
            price=float(selected.price),
        )
        wallet.subscription = new_subs
        print(f"Subscription activated for {wallet.username} ! "
              f"End : {new_subs.end_date}")


def show_all_active_subscriptions(wallets):

    actives = []

    for w in wallets:
        subs = w.subscription
        if subs is not None and subs.is_active:
            actives.append((w.username, subs))

    if len(actives) == 0:
        print("No active subscriptions.")
        return []

    print(f"\n{10 * '-*-'}\nActive Subscriptions\n{10 * '-*-'}")
    for username, subs in actives:
        print(f"User        : {username}")
        print(f"Name        : {subs.name}")
        print(f"End date    : {subs.end_date}")
        print(f"Remaining   : {subs.remaining_time}")
        print(f"{10 * '-*-'}")

    return actives


def show_income_by_subscription_type(wallets):

    income = {}

    for w in wallets:
        for tx in w.transactions:
            if tx.type == "Purchase" or tx.type == "Renew":
                name = tx.subscription_name
                if name is None:
                    name = "Unknown"

                if name in income:
                    income[name] = income[name] + float(tx.amount)
                else:
                    income[name] = float(tx.amount)

    if len(income) == 0:
        print("No subscription income yet.")
        return {}

    print(f"\n{10 * '-*-'}\nIncome by Subscription Type\n{10 * '-*-'}")

    top_name = None
    top_value = 0

    for name in income:
        print(f"{name} : {income[name]}")
        if income[name] > top_value:
            top_value = income[name]
            top_name = name

    print(f"{10 * '-*-'}")
    print(f"Top subscription : {top_name} with {top_value}")
    return income


def show_total_income(wallets):

    total = 0

    for w in wallets:
        for tx in w.transactions:
            if tx.type == "Purchase" or tx.type == "Renew":
                total += float(tx.amount)

    print(f"\n{10 * '-*-'}\nTotal Income\n{10 * '-*-'}")
    print(f"Total income : {total}")
    print(f"{10 * '-*-'}")

    return total