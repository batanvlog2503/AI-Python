# Qtime lay moc thoi gian hien tai

import sys
import time
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase


# khi tao 1 thanh phan nho thi dung (QWdiget)
class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0,0)
        self.setWindowTitle("StopWatch")
        self.time_label = QLabel("00:00:00:00", self)
        self.timer = QTimer(self)

        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.setGeometry(600, 300, 900, 350)
        self.initUI()

    def initUI(self):
        self.time_label.setStyleSheet("background-color:#00FFFF;"
                                      "font-size: 120px;"
                                      "padding:20px;"
                                      "border-radius:45px")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.start_button.setStyleSheet("font-size:40px;"
                                        "padding:15px;")
        self.stop_button.setStyleSheet("font-size:40px;"
                                        "padding:15px;")
        self.reset_button.setStyleSheet("font-size:40px;"
                                        "padding:15px;")
        # cho hết vào 1 khung đã
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.start_button.clicked.connect(self.start_time)
        self.stop_button.clicked.connect(self.start_time)
        self.reset_button.clicked.connect(self.start_time)
        self.timer.timeout.connect(self.update_time)


    def start_time(self):
        self.timer.start(10)


    def stop_time(self):
        self.timer.stop()


    def reset_time(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00:00", self)
    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        milisecon = time.msec() // 10

        return f"{hour:02}:{minute:02}:{second:02}:{milisecon:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    app.exec_()