from PyQt6 import QtCore, QtGui, QtWidgets
from main import calculate
from calorie_calculator import CalorieCalculator
from food_manager import FoodManager
from utils import Utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 786)
        MainWindow.setFixedSize(800, 786)
        MainWindow.setStyleSheet("font: 12pt 'Times New Roman';")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setStyleSheet("""
            #centralwidget {
                background-color: #FFE4B5;
            }
        """)

        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(280, 20, 381, 51))
        self.title_label.setStyleSheet("font: 16pt 'MS Shell Dlg 2'; color: #DAA520;")
        self.title_label.setObjectName("title_label")

        self.food_tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.food_tableWidget.setGeometry(QtCore.QRect(30, 90, 551, 261))
        self.food_tableWidget.setObjectName("food_tableWidget")
        self.food_tableWidget.setColumnCount(4)
        self.food_tableWidget.setRowCount(6)

        self.food_tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.food_tableWidget.setStyleSheet("""
            QTableWidget {
                margin: 0px;
                padding: 0px;
                border: none;
                background-color: white;
                gridline-color: lightgray;
            }
            QHeaderView::section {
                background-color: #FFD700;
                padding: 2px;
                border: 1px solid lightgray;
            }
        """)
        self.food_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.food_tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        for i in range(6):
            self.food_tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(4):
            self.food_tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.gender_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.gender_comboBox.setGeometry(QtCore.QRect(300, 380, 141, 31))
        self.gender_comboBox.setStyleSheet("font: 12pt 'Times New Roman';")
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("Female")
        self.gender_comboBox.addItem("Male")

        self.gender_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(40, 390, 101, 21))
        self.gender_label.setStyleSheet("font: 14pt 'Times New Roman';")
        self.gender_label.setObjectName("gender_label")

        self.activity_level_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.activity_level_label.setGeometry(QtCore.QRect(40, 430, 211, 16))
        self.activity_level_label.setStyleSheet("font: 14pt 'Times New Roman';")
        self.activity_level_label.setObjectName("activity_level_label")

        self.activity_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.activity_comboBox.setGeometry(QtCore.QRect(300, 420, 141, 31))
        self.activity_comboBox.setStyleSheet("font: 12pt 'Times New Roman';")
        self.activity_comboBox.setObjectName("activity_comboBox")
        self.activity_comboBox.addItems(["Sedentary", "Active", "Moderate", "Very Active"])

        self.age_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(40, 470, 151, 31))
        self.age_label.setStyleSheet("font: 14pt 'Times New Roman';")
        self.age_label.setObjectName("age_label")

        self.height_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(40, 530, 101, 16))
        self.height_label.setStyleSheet("font: 14pt 'Times New Roman';")
        self.height_label.setObjectName("height_label")

        self.weight_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(40, 590, 101, 16))
        self.weight_label.setStyleSheet("font: 14pt 'Times New Roman';")
        self.weight_label.setObjectName("weight_label")

        self.calculate_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_pushButton.setGeometry(QtCore.QRect(200, 640, 411, 71))
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.calculate_pushButton.setToolTip("Click to calculate daily calories")
        self.calculate_pushButton.setStyleSheet("background-color: black; color: white; font: 12pt 'Times New Roman';")
        self.calculate_pushButton.clicked.connect(self.calculate_calories)

        self.age_spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.age_spinBox.setGeometry(QtCore.QRect(300, 470, 141, 31))
        self.age_spinBox.setObjectName("age_spinBox")

        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(300, 520, 141, 31))
        self.spinBox.setObjectName("spinBox")

        self.weight_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.weight_doubleSpinBox.setGeometry(QtCore.QRect(300, 570, 131, 31))
        self.weight_doubleSpinBox.setObjectName("weight_doubleSpinBox")

        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(200, 720, 500, 30))
        self.result_label.setStyleSheet("font: 12pt 'Times New Roman'; color: green;")
        self.result_label.setObjectName("result_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "           DAILY CALORIE LOG"))

        for i, text in enumerate(["1.", "2.", "3.", "4.", "5.", "6."]):
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", text))
            self.food_tableWidget.setVerticalHeaderItem(i, item)

        for i, text in enumerate(["Breakfast", "Lunch", "Dinner", "Snacks"]):
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", text))
            self.food_tableWidget.setHorizontalHeaderItem(i, item)

        self.gender_label.setText(_translate("MainWindow", "GENDER:"))
        self.activity_level_label.setText(_translate("MainWindow", "ACTIVITY LEVEL:"))
        self.age_label.setText(_translate("MainWindow", "AGE:"))
        self.height_label.setText(_translate("MainWindow", "HEIGHT:"))
        self.weight_label.setText(_translate("MainWindow", "WEIGHT:"))
        self.calculate_pushButton.setText(_translate("MainWindow", "CALCULATE"))

    def calculate_calories(self):
        gender = self.gender_comboBox.currentText()
        activity = self.activity_comboBox.currentText()
        age = self.age_spinBox.value()
        weight = self.weight_doubleSpinBox.value()
        height = self.spinBox.value()


        print(f"Age: {age}, Weight: {weight}, Height: {height}")

        if weight <= 0 or height <= 0 or age <= 0:
            Utils.show_message("Error", "All values must be greater than zero.")
            return

        breakfast = self.get_food_list_from_table(0)
        lunch = self.get_food_list_from_table(1)
        dinner = self.get_food_list_from_table(2)
        snacks = self.get_food_list_from_table(3)


        print(f"Breakfast: {breakfast}, Lunch: {lunch}, Dinner: {dinner}, Snacks: {snacks}")

        results = calculate(gender, activity, age, weight, height, breakfast, lunch, dinner, snacks)


        print(f"Results: {results}")

        message = (
            f"Calories consumed:\n\n"
            f"Breakfast: {results['breakfast']} kcal\n"
            f"Lunch: {results['lunch']} kcal\n"
            f"Dinner: {results['dinner']} kcal\n"
            f"Snacks: {results['snacks']} kcal\n\n"
            f"Total: {results['total']} kcal\n"
            f"Limit: {results['limit']} kcal"
        )

        QtWidgets.QMessageBox.information(None, "Calorie Results", message)

        if results['total'] > results['limit']:
            Utils.show_message("You have exceeded your daily calorie limit!", "Warning!!")
        else:
            Utils.show_message("You're within your daily calorie limit.", "Congratulations!!")

        self.result_label.setText(f"Total: {results['total']} kcal / Limit: {results['limit']} kcal")

    def get_food_list_from_table(self, column_index):
        food_list = []
        for row in range(self.food_tableWidget.rowCount()):
            item = self.food_tableWidget.item(row, column_index)
            if item is not None:
                food_list.append(item.text())
        return food_list


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

    }