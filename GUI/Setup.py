#Graphic user Interface
#PyQt5
#sys System specific parameters and Function
# thư viện sys làm việc với hệ thống làm việc với đối số
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon , QFont,QPixmap# setup favicon
from PyQt5.QtCore import Qt

# Qt.widgets dùng để tạo giao diện, nút bấm, cửa sổ, layout
#Qy.Gui xử lí đồ họa hình ảnh 2d, icon
#QtMultimedia xử lí âm thanh hình ảnh video
#QApplication là phần tạo app
#QMainWindow đây là phần giao diện chính
# đây là 2 class bạncosos thế kế thừa từ nó

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("I Love PTIT")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("Logo_PTIT_University.png"))
        #
        label = QLabel("Hello PTIT", self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 450, 450)
        label.setStyleSheet("color: blue;"
                            "background-color: white;"
                            "font-weight: bold;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignRight) #lefft
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # tọa độ
        pixmap = QPixmap("Logo_PTIT_University.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) //2,
                          label.width(), label.height())
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__== "__main__":
    main()