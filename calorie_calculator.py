from food_manager import FoodManager


class CalorieCalculator:
    @staticmethod
    def calculate_limit(sex, activity, weight, height, age):
        try:
            print(f"Calorie limit calculation: sex={sex}, activity={activity}, weight={weight}, height={height}, age={age}")

            if weight <= 0 or height <= 0 or age <= 0:
                raise ValueError("Weight, height, and age must be positive values.")
            if sex not in ['male', 'female']:
                raise ValueError("Sex must be 'male' or 'female'.")
            if activity not in ['sedentary', 'moderate', 'active', 'very active']:
                raise ValueError("Activity level is not valid.")

            if sex == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            factors = {
                'sedentary': 1.2,
                'moderate': 1.55,
                'active': 1.9,
                'very active': 1.375
            }

            limit = round(bmr * factors[activity])
            print(f"BMR: {bmr}, Activity: {activity}, Limit: {limit}")
            return limit
        except Exception as e:
            print(f"Error calculating calorie limit: {e}")
            return 0

    @staticmethod
    def calculate_total(food_list: list, food_manager: FoodManager) -> int:
        try:
            total = 0
            for food in food_list:
                calories = food_manager.get_calories(food)
                if calories is None:
                    print(f"Unknown food: {food}")
                    continue
                total += calories
            return total
        except Exception as e:
            print(f"Error calculating total calorie count: {e}")
            return 0
#am facut un comentariu