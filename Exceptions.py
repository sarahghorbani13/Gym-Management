# ارور های قابل استفاده در بخش های مختلف پروژه

#اعتبارسنجی ناموفق
def validation_error():
    return ValueError("اعتبار سنجی ناموفق | Validation failed")

#نام کاربری تکراری
def duplicate_error():
    return ValueError("ورودی تکراری است | Duplicate input")

#نام کاربری یا رمزعبور
def authentication_error():
    return ValueError("نام کاربری یا رمز اشتباه است | Incorrect username or password")

#حساب غیرفعال
def inactive_account_error():
    return PermissionError("حساب کاربری غیرفعال است | User account is inactive")

#وجود نداشتن کاربر یا کلاس یا سالن
def not_found_error():
    return LookupError("کاربر, کلاس یا سالنی با این شناسه وجود ندارد | No user, class, or hall found with this ID")

#غیرفعال بودن سالن یا کلاس یا ووو
def inactive_error():
    return PermissionError("بخش موردنیاز یرفعال است | The required section is inactive")

#پر بودن کلاس یا سالن یا ووو
def capacity_full_error():
    return OverflowError("ظرفیت تکمیل است | Capacity is full")

#پرداخت ناموفق یا کمبود موجودی برای پرداخت
def payment_error():
    return ValueError("پرداخت ناموفق | Payment failed")

#بخش مدیریت فایل ها ووو
def storage_error():
    return OSError("فایل خراب یا نامعتبر است | File is corrupted or invalid")


#اگه ارور دیگه ای داخل کدتون نیاز بود یا خودتون اضافه کنید یا به من اطلاع بدید که اونو به فایل اضافه کنم