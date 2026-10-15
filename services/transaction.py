from datetime import datetime


def f_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Transaction:

    def __init__(self, type_tx, amount, comment, tracking_number, subscription_name=None):
        self.__type = type_tx
        self.__amount = amount
        self.__date = f_now()
        self.__comment = comment
        self.__tracking_number = tracking_number
        self.__subscription_name = subscription_name

    @property
    def type(self):
        return self.__type

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def comment(self):
        return self.__comment

    @property
    def tracking_number(self):
        return self.__tracking_number

    @property
    def subscription_name(self):
        return self.__subscription_name

    def to_row(self):
        return [
            self.__type,
            self.__amount,
            self.__date,
            self.__comment,
            self.__tracking_number,
            self.__subscription_name if self.__subscription_name else "-",
        ]

    def __str__(self):
        return (f"[{self.__date}] {self.__type} , "
                f"amount: {self.__amount} , "
                f"tracking: {self.__tracking_number} , "
                f"{self.__comment}")