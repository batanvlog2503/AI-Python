#Qtime lay moc thoi gian hien tai

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
# khi tao 1 thanh phan nho thi dung (QWdiget)
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 400, 300,100)
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("Logo_PTIT_University1.png"))
       # tao bo dem
        self.time_label = QLabel(self)
        self.timer = QTimer(self) # day la bo dem

        self.initUI()
    def initUI(self):
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        #AlignCeter set cho doi tuong la clocl
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;"
                                      
                                      "color: hsl(111, 100%, 50%);")



        #set cho man hinh chinh
        self.setStyleSheet("background-color:black;")
        # setFont
        font_id = QFontDatabase.addApplicationFont("Technology-Italic.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # set thoi giam
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # vi no la ms nen 1000ms  = 1
        self.update_time()
    def update_time(self):

        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    app.exec_()