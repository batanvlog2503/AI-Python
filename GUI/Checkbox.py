#PyQt Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt, QTime

#Qt dung de can chinh le
#Qt.checked = 2
#Qt.unchecked = 0
#Qt.PartiallyChecked = 1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700 , 300, 500, 500)
        self.checkbox = QCheckBox("Do you like Food?", self)
        self.initUI()
    def initUI(self):
        self.checkbox.setGeometry(10,0, 500, 100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
    def checkbox_changed(self, state):
        print(state) # no se tra ve 2 neu da checked
        # tra ve 0 neu chua check
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()