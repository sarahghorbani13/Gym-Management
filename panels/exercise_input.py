"""دریافت و اعتبارسنجی اطلاعات حرکات تمرینی در رابط متنی باشگاه."""


# قرارداد این ماژول: وارد کردن 0 در هر ورودی به معنی انصراف است.
# بنابراین زمان استراحت در این نسخه باید یک عدد صحیح مثبت باشد.


def get_text(prompt, required=True):
    """یک متن معتبر دریافت می‌کند؛ در صورت انصراف None برمی‌گرداند."""
    while True:
        # strip فاصله‌های اضافی ابتدا و انتهای متن را حذف می‌کند.
        value = input(prompt).strip()

        if value == "0":
            return None

        # توضیحات می‌تواند خالی باشد؛ نام حرکت نمی‌تواند خالی باشد.
        if value or not required:
            return value

        print("این قسمت نمی‌تواند خالی باشد. دوباره تلاش کنید.")


def get_positive_int(prompt):
    """یک عدد صحیح مثبت دریافت می‌کند؛ در صورت انصراف None برمی‌گرداند."""
    while True:
        raw_value = input(prompt).strip()

        # پیش از تبدیل به عدد، فرمان انصراف بررسی می‌شود.
        if raw_value == "0":
            return None

        try:
            number = int(raw_value)
        except ValueError:
            # مثلاً abc قابل تبدیل به عدد صحیح نیست.
            print("لطفاً یک عدد صحیح وارد کنید.")
            continue

        if number > 0:
            return number

        print("عدد باید بزرگ‌تر از صفر باشد.")


def get_exercise():
    """اطلاعات یک حرکت را می‌گیرد و دیکشنری حرکت یا None برمی‌گرداند."""
    # با هر انصراف، بدون ساختن حرکت ناقص از تابع خارج می‌شویم.
    name = get_text("نام حرکت (0: انصراف): ")
    if name is None:
        return None

    sets = get_positive_int("تعداد ست (0: انصراف): ")
    if sets is None:
        return None

    reps = get_positive_int("تعداد تکرار (0: انصراف): ")
    if reps is None:
        return None

    rest = get_positive_int("استراحت به ثانیه (0: انصراف): ")
    if rest is None:
        return None

    description = get_text("توضیحات (اختیاری، 0: انصراف): ", required=False)
    if description is None:
        return None

    # ساخت حرکت فقط در صورت تکمیل همه ورودی‌ها انجام می‌شود.
    # هیچ داده‌ای در این تابع داخل فایل ذخیره نمی‌شود.
    return {
        "name": name,
        "sets": sets,
        "reps": reps,
        "rest": rest,
        "description": description,
    }


def get_exercises():
    """چند حرکت دریافت می‌کند؛ خروجی لیست حرکات یا None در صورت لغو کل عملیات."""
    exercises = []

    while True:
        print("\n1: افزودن حرکت | 2: پایان و دریافت فهرست | 0: لغو کل عملیات")
        choice = input("گزینه: ").strip()

        if choice == "0":
            # داده‌های این مرحله ذخیره نشده‌اند؛ فهرست موقت کنار گذاشته می‌شود.
            return None

        if choice == "2":
            if not exercises:
                print("ابتدا دست‌کم یک حرکت اضافه کنید.")
                continue
            return exercises

        if choice == "1":
            exercise = get_exercise()
            if exercise is None:
                # انصراف از همین حرکت، نه لغو حرکت‌های تکمیل‌شده قبلی.
                print("دریافت این حرکت لغو شد.")
                continue
            exercises.append(exercise)
            print("حرکت به فهرست موقت افزوده شد.")
            continue

        print("گزینه نامعتبر است.")


if __name__ == "__main__":
    # این بخش فقط هنگام اجرای مستقیم ماژول اجرا می‌شود، نه هنگام import.
    result = get_exercises()
    if result is None:
        print("عملیات لغو شد؛ اطلاعاتی ذخیره نشد.")
    else:
        print("فهرست حرکات آماده است:")
        for index, exercise in enumerate(result, start=1):
            print(f"{index}. {exercise}")
