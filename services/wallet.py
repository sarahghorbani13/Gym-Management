from data.Bank import API
from services.transaction import Transaction
from services.subscription import MemberSubscription
from utils.Exceptions import validation_error, payment_error


class Wallet:

    def __init__(self, member_id, username, balance=0):
        self.member_id = member_id
        self.__username = username
        self.__balance = balance
        self.__transactions = []
        self.__subscription = None

    @property
    def username(self):
        return self.__username

    @property
    def balance(self):
        return self.__balance

    @property
    def transactions(self):
        return self.__transactions

    @property
    def subscription(self):
        return self.__subscription

    @subscription.setter
    def subscription(self, member_subscription):
        self.__subscription = member_subscription

    def show_balance(self):
        print(f"({self.__username}) your balance is equal to : {self.__balance}")

    def show_transactions(self):
        if len(self.__transactions) == 0:
            print("No transactions yet.")
            return
        for tx in self.__transactions:
            print(tx)

    def show_subscription_status(self):
        if self.__subscription is None:
            print("You have no subscription.")
            return

        s = self.__subscription
        print(f"\n{10 * '-*-'}\nSubscription Status\n{10 * '-*-'}")
        print(f"Name        : {s.name}")
        print(f"Start date  : {s.start_date}")
        print(f"End date    : {s.end_date}")
        print(f"Status      : {s.status}")
        print(f"Remaining   : {s.remaining_time}")
        print(f"{10 * '-*-'}")

    def deposit_wallet(self):
        print(f"Deposit Panel\n\n{10 * '-*-'}\n"
              f"please complete the following payment requirement...\n\n{10 * '-*-'}")

        try:
            deposit = float(input("Enter deposit amount: "))
            if not (deposit > 0):
                print("Deposit amount must be positive.")
                return None
            card = input("Enter your card number (16 digits) : ").strip()
            exp_month = int(input("Enter expiration month (1-12) : "))
            exp_year = int(input("Enter expiration year : "))
            password = input("Enter your password (6 digits) : ").strip()
            cvv2 = input("Enter your cvv2 (3 digits) : ").strip()
        except ValueError:
            print("Invalid input !")
            return None

        bank = API()
        try:
            payment_id = bank.pay(card, exp_month, exp_year, password, cvv2, deposit)
        except ValueError as e:
            print(f"Payment failed : {e}")
            return None

        self.__balance = self.__balance + deposit

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
        if len(catalog) == 0:
            print("No subscriptions available.")
            return None

        print(f"\n{10 * '-*-'}\nAvailable Subscriptions\n{10 * '-*-'}")
        i = 1
        for subs in catalog:
            print(f"{i}. {subs.name} | {subs.time} months | price: {subs.price}")
            i = i + 1
        print(f"{10 * '-*-'}")

        try:
            choice = int(input("Choose a subscription number : "))
        except ValueError:
            print("Invalid input !")
            return None

        if choice < 1 or choice > len(catalog):
            print("Invalid choice !")
            return None

        selected = catalog[choice - 1]

        try:
            price = float(selected.price)
            duration = int(selected.time)
        except ValueError:
            print("Subscription data is corrupted.")
            return None

        if price <= 0 or duration <= 0:
            print("Invalid subscription price or duration.")
            return None

        new_balance = self.__balance - price
        if new_balance < 0:
            print(f"Not enough balance ! Your balance : {self.__balance} , price : {price}")
            return None
        self.__balance = new_balance

        if self.__subscription is not None and self.__subscription.is_active:
            self.__subscription.renew(duration)
            action = "Renew"
            print(f"Subscription renewed ! New end date : "
                  f"{self.__subscription.end_date}")
        else:
            self.__subscription = MemberSubscription(
                name=selected.name,
                duration_months=duration,
                price=price,
            )
            action = "Purchase"
            print(f"Subscription purchased ! End date : "
                  f"{self.__subscription.end_date}")

        bank = API()
        tracking = bank.generate_payment_id(price, "0000000000000000")

        tx = Transaction(
            type_tx=action,
            amount=price,
            comment=f"Subscription: {selected.name} ({duration} months)",
            tracking_number=tracking,
            subscription_name=selected.name,
        )
        self.__transactions.append(tx)

        print(f"Tracking code : {tracking}")
        return self.__subscription