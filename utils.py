from PyQt6.QtWidgets import QMessageBox

class Utils:
    @staticmethod
    def normalize_activity(activity):
        activity = activity.lower().strip()
        tip_activity = {
            "sedentary": "sedentary",
            "active": "active",
            "moderate": "moderate",
            "very active": "very active"
        }
        return tip_activity.get(activity)


    @staticmethod
    def show_message(title, message):
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle(title)
            msg_box.setText(message)
            msg_box.exec()
        except Exception as e:
            print(f"Eroare la afișarea mesajului: {e}")