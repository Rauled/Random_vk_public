#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, webbrowser, random
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Random', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showRandom)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('random')
        self.show()


    def showRandom(self):
        url = "https://vk.com/public"
        ok = random.randint(11111111, 99999999)
        return webbrowser.open_new_tab(url+str(ok))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
