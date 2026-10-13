from Bank import API
from modules.transaction import Transaction
from modules.member_subscription import MemberSubscription


class Wallet:

    def __init__(self, username, balance=0):
        # اطلاعات پایه‌ی کیف پول رو ذخیره می‌کنیم
        self.__username = username
        self.__balance = balance
        self.__transactions = []
        self.__subscription = None

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def get_subscription(self):
        return self.__subscription

    def set_subscription(self, member_subscription):
        # اشتراک جدید رو برای این عضو ثبت می‌کنیم
        self.__subscription = member_subscription

    def show_balance(self):
        # موجودی فعلی کیف پول رو چاپ می‌کنیم
        print(f"({self.__username}) your balance is equal to : {self.__balance}")

    def show_transactions(self):
        # اگه هیچ تراکنشی نبود، پیام مناسب می‌دیم
        if len(self.__transactions) == 0:
            print("No transactions yet.")
            return
        # همه‌ی تراکنش‌ها رو چاپ می‌کنیم
        for tx in self.__transactions:
            print(tx)

    def show_subscription_status(self):
        # اگه اشتراکی نداشت، پیام مناسب می‌دیم
        if self.__subscription is None:
            print("You have no subscription.")
            return

        # اطلاعات کامل اشتراک رو چاپ می‌کنیم
        s = self.__subscription
        print(f"\n{10 * '-*-'}\nSubscription Status\n{10 * '-*-'}")
        print(f"Name        : {s.get_name()}")
        print(f"Start date  : {s.get_start_date()}")
        print(f"End date    : {s.get_end_date()}")
        print(f"Status      : {s.get_status()}")
        print(f"Remaining   : {s.remaining_time()}")
        print(f"{10 * '-*-'}")

    def deposit_wallet(self):
        # پنل واریز رو نشون می‌دیم و اطلاعات کارت رو از کاربر می‌گیریم
        print(f"Deposit Panel\n\n{10 * '-*-'}\n"
              f"please complete the following payment requirement...\n\n{10 * '-*-'}")

        # ورودی‌های عددی رو با try/except می‌گیریم که خطا ندیم
        try:
            deposit = float(input("Enter amount of deposit : "))
            card = input("Enter your card number (16 digits) : ")
            exp_month = int(input("Enter expiration month (1-12) : "))
            exp_year = int(input("Enter expiration year (1405-1410) : "))
            password = input("Enter your password (16 digits) : ")
            cvv2 = input("Enter your cvv2 (3/4 digits) : ")
        except ValueError:
            print("Invalid input !")
            return None

        # از API بانک برای انجام پرداخت استفاده می‌کنیم
        bank = API()
        try:
            payment_id = bank.pay(card, exp_month, exp_year, password, cvv2, deposit)
        except ValueError as e:
            print(f"Payment failed : {e}")
            return None

        # مبلغ واریزی رو به موجودی اضافه می‌کنیم
        self.__balance = self.__balance + deposit

        # یه تراکنش جدید می‌سازیم و به لیست تراکنش‌ها اضافه می‌کنیم
        tx = Transaction(
            type_tx="Deposit",
            amount=deposit,
            comment=f"Wallet deposit via bank for {self.__username}",
            tracking_number=payment_id,
        )
        self.__transactions.append(tx)

        print(f"Payment successful ! Tracking code : {payment_id}")
        return self.__balance

    def pur_ren_subs(self, catalog):
        # اگه کاتالوگ خالی بود، پیام مناسب می‌دیم
        if len(catalog) == 0:
            print("No subscriptions available.")
            return None

        # لیست پلن‌ها رو همراه با قیمت‌ها چاپ می‌کنیم
        print(f"\n{10 * '-*-'}\nAvailable Subscriptions\n{10 * '-*-'}")
        i = 1
        for subs in catalog:
            print(f"{i}. {subs.get_name()} | {subs.get_time()} months | price: {subs.get_price()}")
            i = i + 1
        print(f"{10 * '-*-'}")

        # شماره‌ی پلن رو از کاربر می‌گیریم
        try:
            choice = int(input("Choose a subscription number : "))
        except ValueError:
            print("Invalid input !")
            return None

        # شماره‌ی وارد شده رو اعتبارسنجی می‌کنیم
        if choice < 1 or choice > len(catalog):
            print("Invalid choice !")
            return None

        # پلن انتخابی رو از کاتالوگ بیرون می‌کشیم
        selected = catalog[choice - 1]

        # قیمت و مدت پلن رو به عدد تبدیل می‌کنیم
        try:
            price = float(selected.get_price())
            duration = int(selected.get_time())
        except ValueError:
            print("Subscription data is corrupted.")
            return None

        # موجودی کیف پول رو با قیمت پلن مقایسه می‌کنیم
        if self.__balance < price:
            print(f"Not enough balance ! Your balance : {self.__balance} , price : {price}")
            return None

        # مبلغ پلن رو از موجودی کم می‌کنیم
        self.__balance = self.__balance - price

        # اگه اشتراک فعال داشتیم، تمدید می‌کنیم
        # وگرنه یه اشتراک جدید می‌سازیم
        if self.__subscription is not None and self.__subscription.is_active():
            self.__subscription.renew(duration)
            action = "Renew"
            print(f"Subscription renewed ! New end date : "
                  f"{self.__subscription.get_end_date()}")
        else:
            self.__subscription = MemberSubscription(
                name=selected.get_name(),
                duration_months=duration,
                price=price,
                )
            action = "Purchase"
            print(f"Subscription purchased ! End date : "
                  f"{self.__subscription.get_end_date()}")

        # یه شماره پیگیری از بانک می‌گیریم
        bank = API()
        tracking = bank.generate_payment_id(price, "0000000000000000")

        # تراکنش خرید/تمدید رو ثبت می‌کنیم
        tx = Transaction(
            type_tx=action,
            amount=price,
            comment=f"Subscription: {selected.get_name()} ({duration} months)",
            tracking_number=tracking,
        )
        self.__transactions.append(tx)

        print(f"Tracking code : {tracking}")
        return self.__subscription