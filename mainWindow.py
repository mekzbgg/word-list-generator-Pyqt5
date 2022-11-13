from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import itertools
import threading
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(291, 297)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LOGO = QLabel(self.centralwidget)
        self.LOGO.setText("")
        self.LOGO.setGeometry(QRect(50, 10, 191, 71))
        self.LOGO.setObjectName("LOGO")
        self.pixmap = QPixmap(f'{os.getcwd()}/alfabu.png')
        self.LOGO.setPixmap(self.pixmap)
        self.LOGO.resize(self.pixmap.width(), self.pixmap.height())
        self.pushButton = QPushButton(self.centralwidget,clicked = lambda: threading.Thread(target=self.creates_word_list()).start())
        self.pushButton.setGeometry(QRect(108, 240, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(80, 160, 131, 31))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QRect(10, 200, 121, 31))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QRect(160, 200, 121, 31))
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(0, 130, 291, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        print(self.lineEdit_2.text())
        print(self.lineEdit.text())
        print(self.lineEdit_3.text())
        try:
            self.lineEdit.textChanged.connect(self.total_words)
        except:
            pass
        try:
            self.lineEdit_2.textChanged.connect(self.total_words)
        except:
            pass
        try:
            self.lineEdit_3.textChanged.connect(self.total_words)
        except:
            pass
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alfabu - ZBGG & FA"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Letters"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Min length"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Max length"))
        self.label_2.setText(_translate("MainWindow", "Count of created words"))
    def total_words(self):
        print(self.lineEdit_3.text())
        if self.lineEdit_3.text() != "" and self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
            _translate = QCoreApplication.translate
            list1 = []
            list1[:0] = self.lineEdit.text()
            min_lenght = int(self.lineEdit_2.text())
            max_lenght = int(self.lineEdit_3.text())
            global list2
            list2=[]
            for i in list1:
                if not i in list2:
                    list2.append(i)
            lenght = len(list2)
            total_words = 0
            for i in range(min_lenght,max_lenght+1):
                total_words = lenght ** i + total_words
            self.label_2.setText(f"Count of created words: {str(total_words)}")

    def creates_word_list(self):
        try:
            os.remove("wordList.txt")
        except Exception as e:
            print(e)
        min_lenght = int(self.lineEdit_2.text())
        max_lenght = int(self.lineEdit_3.text())
        file = open("wordList.txt","a",encoding="utf-8")

        for n in range(min_lenght, max_lenght + 1):
            for xs in itertools.product(list2, repeat=n):
                chars = ''.join(xs)
                file = open("wordList.txt", "a", encoding="utf-8")
                file.write(chars+"\n")
                file.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Word list created")
        msg.setWindowTitle("Alfabu")
        msg.show()
        msg.exec_()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
