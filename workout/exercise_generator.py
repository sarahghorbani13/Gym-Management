"""ابزار پیمایش حرکات تمرینی با Generator"""


def iter_exercises(exercises, min_sets=1):
    """حرکت‌های دارای تعداد ست حداقل min_sets را یک‌به‌یک تولید می‌کند.

    ورودی exercises: لیستی از دیکشنری‌های خروجی get_exercises
    خروجی: مولد (generator) که دیکشنری هر حرکت واجد شرایط را تولید می‌کند.
    """
    # اعتبارسنجی پارامتر فیلتر: تعداد ست حداقل باید عدد صحیح مثبت باشد.
    if type(min_sets) is not int or min_sets < 1:
        raise ValueError("min_sets باید یک عدد صحیح مثبت باشد.")

    # پیمایش تک‌تک حرکات
    for exercise in exercises:
        # فقط حرکت‌هایی که تعداد ست کافی دارند برگردانده می‌شوند.
        if exercise["sets"] >= min_sets:
            yield exercise


if __name__ == "__main__":

    sample_exercises = [
        {"name": "Squat", "sets": 3, "reps": 12, "rest": 60, "description": ""},
        {"name": "Plank", "sets": 1, "reps": 1, "rest": 30, "description": ""},
        {"name": "Push-up", "sets": 4, "reps": 10, "rest": 45, "description": ""},
    ]
    # هر بار درخواست حرکت بعدی، Generator از محل قبلی ادامه می‌دهد.
    for exercise in iter_exercises(sample_exercises, min_sets=3):
        print(f"{exercise['name']}: {exercise['sets']} ست")
