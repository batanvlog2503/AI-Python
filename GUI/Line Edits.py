# PyQt5 Line Edit
#PyQt Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLineEdit, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt, QTime

#Qt dung de can chinh le
#Qt.checked = 2
#Qt.unchecked = 0
#Qt.PartiallyChecked = 1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700 , 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setPlaceholderText("Enter your name: ")
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family: Arial")
        self.button.setGeometry(210,10, 100, 40)
        self.button.setStyleSheet("font-size:25px;"
                                     "font-family: Arial")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Helo {text}")
        print("You Clicked the button !")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()