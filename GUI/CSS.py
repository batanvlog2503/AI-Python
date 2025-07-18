
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QVBoxLayout, QLabel, QWidget, QHBoxLayout

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       # self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("I Love PTIT")
        self.setWindowIcon(QIcon("Logo_PTIT_University.png"))

        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.setStyleSheet("""
            QPushButton{
                font_size: 40px;
                font-family: Arial;
                margin:25px;
                padding: 15px 75px;
                border: 3px solid;
                border-radius: 15px
            }
            QPushButton#button1{
                background-color: red;
            }
            QPushButton#button2{
                background-color: yellow;
            }
            QPushButton#button3{
                background-color: green;
            }
            QPushButton#button1:hover{
                background-color: orange;
            }
            QPushButton#button2:hover{
                background-color: grey;
            }
            QPushButton#button3:hover{
                background-color: brown;
            }
        """)

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()