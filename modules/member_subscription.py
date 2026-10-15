from datetime import datetime, timedelta


class MemberSubscription:

    def __init__(self, name, duration_months, price):
        # اطلاعات اشتراک رو ذخیره می‌کنیم
        self.__name = name
        self.__duration_months = int(duration_months)
        self.__price = float(price)

        # تاریخ شروع رو از همین الان می‌گیریم
        self.__start_date = datetime.now()

        # تاریخ پایان رو با اضافه کردن مدت اشتراک حساب می‌کنیم
        # (هر ماه رو ۳۰ روز در نظر می‌گیریم)
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
        # زمان حال رو با تاریخ پایان مقایسه می‌کنیم
        return datetime.now() < self.__end_date

    @property
    def status(self):
        # وضعیت اشتراک رو برمی‌گردونیم
        if self.is_active:
            return "Active"
        return "Expired"

    @property
    def remaining_time(self):
        # اگه اشتراک منقضی شده بود، پیام مناسب می‌دیم
        if not self.is_active:
            return "Subscription has ended"

        # زمان باقی‌مونده رو حساب می‌کنیم
        left = self.__end_date - datetime.now()
        days = left.days
        hours = left.seconds // 3600
        minutes = (left.seconds % 3600) // 60
        return f"{days} days , {hours} hours and {minutes} minutes left"
        
    def renew(self, duration_months):
        # اگه اشتراک فعال بود، از تاریخ پایان ادامه می‌دیم
        # وگرنه از امروز دوباره شروع می‌کنیم
        if self.is_active:    
            base = self.__end_date
        else:
            base = datetime.now()

        # تاریخ پایان و مجموع ماه‌ها رو به‌روز می‌کنیم
        self.__end_date = base + timedelta(days=30 * int(duration_months))
        self.__duration_months = self.__duration_months + int(duration_months)

    def __str__(self):
        # اشتراک رو به شکل متن قابل چاپ برمی‌گردونیم
        return (f"[{self.__name}] from {self.__start_date.strftime('%Y-%m-%d')} "
                f"to {self.__end_date.strftime('%Y-%m-%d')} | "
                f"status: {self.status}")    
