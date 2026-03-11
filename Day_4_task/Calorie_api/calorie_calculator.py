def get_activity_level(days):
    if days == 0:
        return "Sedentary", 1.2
    elif days <= 2:
        return "Lightly Active", 1.375
    elif days <= 5:
        return "Moderately Active", 1.55
    else:
        return "Very Active", 1.725

def calculate_bmr(age, gender, height_cm, weight_kg):
    if gender.lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    return bmr

def calculate_daily_calories(age, gender, height_cm, weight_kg, exercise_days):
    activity_level, multiplier = get_activity_level(exercise_days)

    bmr = calculate_bmr(age, gender, height_cm, weight_kg)

    daily_calories = bmr * multiplier

    return round(daily_calories)