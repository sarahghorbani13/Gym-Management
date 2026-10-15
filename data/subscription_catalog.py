class Subscription:
    def __init__(self, name, time, price):
        self.__name = name
        self.__time = time
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def time(self):
        return self.__time

    @property
    def price(self):
        return self.__price

    def to_row(self):
        return [self.__name, self.__time, self.__price]


catalog = [
    Subscription("GOLD", "6", "900000"),
    Subscription("SILVER", "3", "500000"),
    Subscription("BRONZE", "1", "200000"),
]