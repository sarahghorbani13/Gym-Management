from modules.member_subscription import MemberSubscription

def manager_activate_subscription(wallets, catalog):

    # اگه هیچ عضوی نبود، پیام مناسب می‌دیم
    if len(wallets) == 0:
        print("No members registered.")
        return

    # لیست اعضا رو چاپ می‌کنیم
    print(f"\n{10 * '-*-'}\nMembers\n{10 * '-*-'}")
    i = 1
    for w in wallets:
        print(f"{i}. {w.get_username()}")
        i = i + 1
    print(f"{10 * '-*-'}")

    # شماره‌ی عضو رو از مدیر می‌گیریم
    try:
        choice = int(input("Choose a member number : "))
    except ValueError:
        print("Invalid input !")
        return

    # اعتبارسنجی شماره
    if choice < 1 or choice > len(wallets):
        print("Invalid choice !")
        return

    # عضو انتخاب‌شده رو بیرون می‌کشیم
    wallet = wallets[choice - 1]

    # اگه کاتالوگ خالی بود، پیام مناسب می‌دیم
    if len(catalog) == 0:
        print("No subscriptions available.")
        return

    # لیست پلن‌ها رو چاپ می‌کنیم
    print(f"\n{10 * '-*-'}\nSubscriptions\n{10 * '-*-'}")
    i = 1
    for subs in catalog:
        print(f"{i}. {subs.get_name()} | {subs.get_time()} months | price: {subs.get_price()}")
        i = i + 1
    print(f"{10 * '-*-'}")

    # شماره‌ی پلن رو از مدیر می‌گیریم
    try:
        choice = int(input("Choose a subscription number : "))
    except ValueError:
        print("Invalid input !")
        return

    if choice < 1 or choice > len(catalog):
        print("Invalid choice !")
        return

    # پلن انتخاب‌شده و مدت اون رو بیرون می‌کشیم
    selected = catalog[choice - 1]
    duration = int(selected.get_time())

    # اگه عضو اشتراک فعال داشت، تمدید می‌کنیم
    # وگرنه یه اشتراک جدید براش می‌سازیم
    current = wallet.get_subscription()
    if current is not None and current.is_active():
        current.renew(duration)
        print(f"Subscription renewed for {wallet.get_username()} ! "
              f"New end : {current.get_end_date()}")
    else:
        new_subs = MemberSubscription(
            name=selected.get_name(),
            duration_months=duration,
            price=float(selected.get_price()),
            )
        wallet.set_subscription(new_subs)
        print(f"Subscription activated for {wallet.get_username()} ! "
              f"End : {new_subs.get_end_date()}")


def show_all_active_subscriptions(wallets):

    # اشتراک‌های فعال رو جمع می‌کنیم
    actives = []

    for w in wallets:
        subs = w.get_subscription()
        if subs is not None and subs.is_active():
            actives.append((w.get_username(), subs))

    # اگه هیچ اشتراک فعالی نبود، پیام مناسب می‌دیم
    if len(actives) == 0:
        print("No active subscriptions.")
        return []

    # اطلاعات هر اشتراک فعال رو چاپ می‌کنیم
    print(f"\n{10 * '-*-'}\nActive Subscriptions\n{10 * '-*-'}")
    for username, subs in actives:
        print(f"User        : {username}")
        print(f"Name        : {subs.get_name()}")
        print(f"End date    : {subs.get_end_date()}")
        print(f"Remaining   : {subs.remaining_time()}")
        print(f"{10 * '-*-'}")

    return actives


def show_income_by_subscription_type(wallets):

    # یه دیکشنری خالی برای جمع درآمد هر پلن می‌سازیم
    income = {}

    # همه‌ی تراکنش‌های همه‌ی اعضا رو بررسی می‌کنیم
    for w in wallets:
        for tx in w.get_transactions():
            # فقط تراکنش‌های خرید و تمدید رو حساب می‌کنیم
            if tx.get_type() == "Purchase" or tx.get_type() == "Renew":
                # اسم اشتراک رو از comment بیرون می‌کشیم
                comment = tx.get_comment()
                parts = comment.split(":")
                if len(parts) > 1:
                    name = parts[1].split("(")[0].strip()
                else:
                    name = "Unknown"

                # مبلغ رو به جمع اون پلن اضافه می‌کنیم
                if name in income: #برای وقتی که در دیکشنری وجود داره
                    income[name] = income[name] + float(tx.get_amount())
                else:              # برای وقتی که برای بار اول تو دیکشنری ذخیرش می کنیم
                    income[name] = float(tx.get_amount())

    # اگه هیچ درآمدی نبود، پیام مناسب می‌دیم
    if len(income) == 0:
        print("No subscription income yet.")
        return {}

    # درآمد هر پلن رو چاپ می‌کنیم
    print(f"\n{10 * '-*-'}\nIncome by Subscription Type\n{10 * '-*-'}")

    # بیشترین درآمد رو هم پیدا می‌کنیم
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

    # مجموع رو از صفر شروع می‌کنیم
    total = 0

    # همه‌ی تراکنش‌های همه‌ی اعضا رو بررسی می‌کنیم
    for w in wallets:
        for tx in w.get_transactions():
            # فقط خرید و تمدید اشتراک رو درآمد حساب می‌کنیم
            if tx.get_type() == "Purchase" or tx.get_type() == "Renew":
                total += float(tx.get_amount())

    # درآمد کل رو چاپ می‌کنیم
    print(f"\n{10 * '-*-'}\nTotal Income\n{10 * '-*-'}")
    print(f"Total income : {total}")
    print(f"{10 * '-*-'}")

    return total
