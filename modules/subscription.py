class Subscription:

    def __init__(self, name, time, price):
        # اطلاعات پلن رو ذخیره می‌کنیم
        self.__name = name
        self.__time = time
        self.__price = price

    def get_name(self):
        return self.__name

    def get_time(self):
        return self.__time

    def get_price(self):
        return self.__price


# لیست پلن‌های پیش‌فرض رو تعریف می‌کنیم
catalog = [
    Subscription("GOLD", "6", "900000"),
    Subscription("SILVER", "3", "500000"),
    Subscription("BRONZE", "1", "200000"),
]