import json

class ConfigLoader:
    def __init__(self, filepath='config.json'):
        with open(filepath, 'r') as f:
            self.config = json.load(f)

    def get_calories_limit(self, sex, activity_level):
        return self.config["calories"][sex][activity_level]