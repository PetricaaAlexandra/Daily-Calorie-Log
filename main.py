from utils import Utils
from calorie_calculator import CalorieCalculator
from food_manager import FoodManager
from log_manager import LogManager

def calculate(gender, activity, age, weight, height, breakfast, lunch, dinner, snacks):
    food_manager = FoodManager()

    gender = gender.lower().strip()
    activity = Utils.normalize_activity(activity)

    breakfast_calories = CalorieCalculator.calculate_total(breakfast, food_manager)
    lunch_calories = CalorieCalculator.calculate_total(lunch, food_manager)
    dinner_calories = CalorieCalculator.calculate_total(dinner, food_manager)
    snack_calories = CalorieCalculator.calculate_total(snacks, food_manager)

    total_calories = breakfast_calories + lunch_calories + dinner_calories + snack_calories
    limit = CalorieCalculator.calculate_limit(gender, activity, weight, height, age)

    logger = LogManager()
    logger.add_log({
        "gender": gender,
        "weight": weight,
        "height": height,
        "age": age,
        "activity": activity,
        "calories_consumed": total_calories,
        "calories_limit": limit,
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "snacks": snacks
    })

    return {
        "breakfast": breakfast_calories,
        "lunch": lunch_calories,
        "dinner": dinner_calories,
        "snacks": snack_calories,
        "total": total_calories,
        "limit": limit
    }
