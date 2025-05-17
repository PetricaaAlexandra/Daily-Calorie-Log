import json
import os
from datetime import datetime

class LogManager:
    def __init__(self, filepath='log.json'):
        self.filepath = filepath
        self.logs = self.load_logs()

    def load_logs(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[Error] The file {self.filepath} is corrupted. A new log will be created.")
            return []

    def save_logs(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.logs, f, indent=4)
        except IOError:
            print("[Error] Could not save the log file.")

    def add_log(self, data):
        data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(data)
        self.save_logs()