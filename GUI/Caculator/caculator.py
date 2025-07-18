
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton, QGridLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap

class Caculator(QWidget):
    def __init__(self):
        super().__init__()
        #set title
        self.setGeometry(600, 300, 300, 400)
        self.setWindowTitle("Caculator")
        self.setWindowIcon(QIcon("Logo_PTIT_University2.png"))
        self.line_edit = QLineEdit(self)
        self.setStyleSheet("background-color:black")
        self.initUI()
    def initUI(self):
        self.line_edit.setReadOnly(False)
        #self.line_edit.setGeometry(0, 0, self.width(), 50)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     " height:50px;"
                                     "background-color:grey;"
                                     "border:1px solid;")

        grid = QGridLayout()
        button = [
            ('7', 0, 0) , ('8', 0, 1), ('9', 0, 2),('/', 0, 3),
            ('4', 1, 0) , ('5', 1, 1), ('6', 1, 2),('*', 1, 3),
            ('1', 2, 0) , ('2', 2, 1), ('3', 2, 2),('-', 2, 3),
            ('0', 3, 0) , ('C', 3, 1), ('=', 3, 2),('+', 3, 3),
        ]
        for text, row, col in button:
            button = QPushButton(text)
            if text.isdigit():
                button.setFixedSize(60, 60)  # Kích thước vuông phải mặc định nó 1 kích thuojcs cụ thể mới radius được
                button.setStyleSheet("""
                   QPushButton {
                       background-color: grey;
                       color: white;
                       font-size: 20px;
                       border-radius: 30px;
                       
                   }
                   QPushButton:hover {
                       background-color: white;
                       color: black;
                   }
               """)

            else:
                button.setFixedSize(60, 60)  # Kích thước vuông
                button.setStyleSheet("""
                                   QPushButton {
                                       background-color: orange;
                                       color: white;
                                       font-size: 20px;
                                       border-radius: 30px;

                                   }
                                   QPushButton:hover {
                                       background-color: pink;
                                   }
                               """)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid.addWidget(button, row, col)
        # add phần line_edit
        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)

        vbox.addLayout(grid)
        self.setLayout(vbox)

    def on_button_click(self, text):
        if text == 'C':
            self.line_edit.clear()
        elif text == '=':
            try:
                result = str(eval(self.line_edit.text()))
                self.line_edit.setText(result)
            except:
                self.line_edit.setText("ERROR")
        else:
            self.line_edit.setText(self.line_edit.text() + text)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    caculator = Caculator()
    caculator.show()
    app.exec_()
