import json

class FoodManager:
    def __init__(self, filepath='foods.json'):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as f:
                self.foods = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"[Error] Could not read {filepath}. A blank dictionary will be used.")
            self.foods = {}

    def get_calories(self, food_name):
        try:
            #return self.foods.get(food_name, 150)
            return self.foods[food_name]
        except KeyError:
            self.foods[food_name] = 150
            try:
                with open(self.filepath, 'w') as f:
                    json.dump(self.foods, f, indent=4)
            except IOError:
                print("[Error] Could not write to the food file.")
            print(f"The food '{food_name}' did not exist. It has been added with 150 kcal.")
            return 150

    def get_all_foods(self):
        return list(self.foods.keys())

    def add_food(self, name, calories):
        self.foods[name] = calories
        self._save_foods()

    def remove_food(self, name):
        if name in self.foods:
            del self.foods[name]
            self._save_foods()

    def _save_foods(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.foods, f, indent=4)
        except IOError:
            print("[Error] Could not write to the food file.")