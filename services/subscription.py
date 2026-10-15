from datetime import datetime, timedelta


class MemberSubscription:

    def __init__(self, name, duration_months, price):
        self.__name = name
        self.__duration_months = int(duration_months)
        self.__price = float(price)

        self.__start_date = datetime.now()

        self.__end_date = self.__start_date + timedelta(days=30 * self.__duration_months)

    @property
    def name(self):
        return self.__name

    @property
    def duration_months(self):
        return self.__duration_months

    @property
    def price(self):
        return self.__price

    @property
    def start_date(self):
        return self.__start_date.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_date(self):
        return self.__end_date.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def is_active(self):
        return datetime.now() < self.__end_date

    @property
    def status(self):
        if self.is_active:
            return "Active"
        return "Expired"

    @property
    def remaining_time(self):
        if not self.is_active:
            return "Subscription has ended"

        left = self.__end_date - datetime.now()
        days = left.days
        hours = left.seconds // 3600
        minutes = (left.seconds % 3600) // 60
        return f"{days} days , {hours} hours and {minutes} minutes left"

    def renew(self, duration_months):
        if self.is_active:
            base = self.__end_date
        else:
            base = datetime.now()

        self.__end_date = base + timedelta(days=30 * int(duration_months))
        self.__duration_months = self.__duration_months + int(duration_months)

    def to_row(self):
        return [
            self.__name,
            self.__duration_months,
            self.__price,
            self.start_date,
            self.end_date,
        ]

    def __str__(self):
        return (f"[{self.__name}] from {self.start_date} "
                f"to {self.end_date} | status: {self.status}")