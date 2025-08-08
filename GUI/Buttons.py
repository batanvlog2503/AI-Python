
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("Logo_PTIT_University.png"))
        self.setWindowTitle("I LOVE PTIT")
        self.label = QLabel("Helo ptit", self)
        self.initUI()
    def initUI(self):
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size:50px;")

    def on_click(self):
        print("Button Clicked !")
        self.button.setText("clicked!")
        self.label.setText("GoodBye!")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()