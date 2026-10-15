import random
from datetime import datetime


def _current_shamsi_year():
    # سال شمسی رو از میلادی حساب می‌کنیم (تقریبی)
    return datetime.now().year - 621


def _current_shamsi_month():
    # ماه میلادی و روز رو می‌گیریم
    month = datetime.now().month
    day = datetime.now().day

    # اگه قبل از ۲۱ مارس باشیم، هنوز توی سال شمسی قبلیم
    # چون سال شمسی از ۱ فروردین (تقریباً ۲۱ مارس) شروع می‌شه
    if (month, day) < (3, 21):
        # ژانویه (1) → دی (10) ، فوریه (2) → بهمن (11) ، مارس (3) → اسفند (12)
        return month + 9

    # آوریل (4) → فروردین (1) ، می (5) → اردیبهشت (2) ، ... ، دسامبر (12) → آذر (9)
    return (month - 3) % 12

class API:

    def __init__(self):
        pass

    def validate(self, card, exp_month, exp_year, password, cvv2):
        current_year = _current_shamsi_year()
        current_month = _current_shamsi_month()

        if len(str(card)) != 16 or not str(card).isnumeric():
            return False
        if not (1 <= exp_month <= 12):
            return False
        if exp_year < current_year or exp_year > current_year + 5:
            return False
        if exp_year == current_year and exp_month < current_month:
            return False
        if len(str(password)) != 6:
            return False
        if len(str(cvv2)) != 3:
            return False
        return True

    def generate_payment_id(self, amount, card):
        return f'{card}{amount}{random.randint(100000, 999999)}'

    def pay(self, card, exp_month, exp_year, password, cvv2, amount):
        if self.validate(card, exp_month, exp_year, password, cvv2):
            return self.generate_payment_id(amount, card)
        else:
            raise ValueError('Invalid payment details.')
