# radiobutton

#PyQt Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QButtonGroup

from PyQt5.QtCore import Qt, QTime
#QButtonGroup hieu don gian la
# khi ta dung radiobutton khong the an cung 1 luc 2 thuoc tinh

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700 , 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("Online", self)
        self.radio5 = QRadioButton("In-store", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                            "font-size:40px;"
                            "font-family:Arial;"
                            "padding:10px"
                            "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        #toggled.connect
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
    def radio_button_changed(self):
        radio_button = self.sender() # lay tin hien xem da nhan cai nao
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()