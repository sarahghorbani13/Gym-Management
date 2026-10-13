"""مدیریت حرکات یک برنامه تمرینی"""

from copy import deepcopy

from .exercise_input import get_exercise, get_positive_int, get_text


def show_exercises(exercises):
    """فهرست حرکات را با شماره قابل انتخاب نمایش می‌دهد."""
    if not exercises:
        print("هنوز حرکتی در فهرست نیست.")
        return

    for number, exercise in enumerate(exercises, start=1):
        print(
            f"{number}. {exercise['name']} | "
            f"ست: {exercise['sets']} | تکرار: {exercise['reps']} | "
            f"استراحت: {exercise['rest']} ثانیه | "
            f"توضیحات: {exercise['description'] or '-'}"
        )


def choose_exercise(exercises):
    """شماره حرکت را می‌گیرد و اندیس آن را برمی‌گرداند؛ انصراف: None."""
    if not exercises:
        print("حرکتی برای انتخاب وجود ندارد.")
        return None

    while True:
        show_exercises(exercises)
        raw = input("شماره حرکت را وارد کنید (0: بازگشت): ").strip()

        if raw == "0":
            return None

        try:
            number = int(raw)
        except ValueError:
            print("شماره باید عدد صحیح باشد.")
            continue

        if 1 <= number <= len(exercises):
            # شماره‌ها برای کاربر از ۱، ولی اندیس‌های لیست از ۰ شروع می‌شوند.
            return number - 1

        print("شماره انتخاب‌شده در فهرست وجود ندارد.")


def edit_exercise(exercise):
    """ویرایش یکی از مشخصات حرکت؛ خروجی نسخه ویرایش‌شده یا None هنگام انصراف."""
    # تا وقتی مربی تأیید نکرده، شیء اصلی تغییر نمی‌کند.
    updated = exercise.copy()

    while True:
        print("\nویرایش حرکت:", updated['name'])
        print("1: نام | 2: ست | 3: تکرار | 4: استراحت | 5: توضیحات")
        print("6: تأیید ویرایش | 0: لغو ویرایش")
        choice = input("گزینه: ").strip()

        if choice == "0":
            return None

        if choice == "6":
            return updated

        if choice == "1":
            value = get_text("نام جدید (0: لغو دریافت): ")
            key = "name"
        elif choice == "2":
            value = get_positive_int("تعداد ست جدید (0: لغو دریافت): ")
            key = "sets"
        elif choice == "3":
            value = get_positive_int("تکرار جدید (0: لغو دریافت): ")
            key = "reps"
        elif choice == "4":
            value = get_positive_int("استراحت جدید به ثانیه (0: لغو دریافت): ")
            key = "rest"
        elif choice == "5":
            value = get_text("توضیحات جدید (خالی مجاز، 0: لغو دریافت): ", required=False)
            key = "description"
        else:
            print("گزینه نامعتبر است.")
            continue

        if value is None:
            # صفر فقط ویرایش این فیلد را لغو می‌کند؛ دوباره به منوی ویرایش می‌رویم.
            print("تغییر این فیلد انجام نشد.")
            continue

        updated[key] = value
        print("مقدار جدید ثبت موقت شد؛ برای تأیید گزینه 6 را بزنید.")


def manage_exercises(existing=None):
    """افزودن/ویرایش/حذف حرکات؛ خروجی لیست نهایی یا None در صورت لغو کل عملیات."""
    # با کپی کار می‌کنیم تا انصراف، فهرست اولیه فراخواننده را تغییر ندهد.
    exercises = deepcopy(existing) if existing is not None else []

    while True:
        print("\n--- مدیریت حرکات برنامه تمرینی ---")
        print("1: مشاهده | 2: افزودن | 3: ویرایش | 4: حذف")
        print("5: تأیید فهرست | 0: لغو کل تغییرات")
        choice = input("گزینه: ").strip()

        if choice == "0":
            return None

        if choice == "1":
            show_exercises(exercises)
            continue

        if choice == "2":
            exercise = get_exercise()
            if exercise is not None:
                exercises.append(exercise)
                print("حرکت اضافه شد (هنوز در فایل ذخیره نشده است).")
            continue

        if choice == "3":
            index = choose_exercise(exercises)
            if index is None:
                continue
            updated = edit_exercise(exercises[index])
            if updated is not None:
                exercises[index] = updated
                print("ویرایش حرکت تأیید شد.")
            continue

        if choice == "4":
            index = choose_exercise(exercises)
            if index is None:
                continue
            confirm = input("برای حذف حرکت، حرف y را وارد کنید: ").strip().lower()
            if confirm == "y":
                removed = exercises.pop(index)
                print(f"حرکت {removed['name']} حذف شد (فقط از فهرست موقت).")
            else:
                print("حذف لغو شد.")
            continue

        if choice == "5":
            if not exercises:
                print("برنامه باید دست‌کم یک حرکت داشته باشد.")
                continue
            return exercises

        print("گزینه نامعتبر است.")


if __name__ == "__main__":
    # صرفاً برای اجرای مستقیم؛ در اتصال به برنامه اصلی تابع manage_exercises فراخوانی می‌شود.
    result = manage_exercises()
    if result is None:
        print("تغییرات لغو شد؛ داده‌ای ذخیره نشد.")
    else:
        print("فهرست نهایی آماده ارسال به بخش ذخیره‌سازی است:")
        show_exercises(result)
