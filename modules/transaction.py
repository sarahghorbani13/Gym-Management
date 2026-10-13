from datetime import datetime


# زمان حال رو به شکل متن برمی‌گردونیم
def f_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Transaction:

    def __init__(self, type_tx, amount, comment, tracking_number):
        # اطلاعات تراکنش رو ذخیره می‌کنیم
        self.__type = type_tx
        self.__amount = amount
        self.__date = f_now()
        self.__comment = comment
        self.__tracking_number = tracking_number

    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount

    def get_date(self):
        return self.__date

    def get_comment(self):
        return self.__comment

    def get_tracking_number(self):
        return self.__tracking_number

    def __str__(self):
        # تراکنش رو به شکل متن قابل چاپ برمی‌گردونیم
        return (f"[{self.__date}] {self.__type} , "
                f"amount: {self.__amount} , "
                f"tracking: {self.__tracking_number} , "
                f"{self.__comment}")