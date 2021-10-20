# Filename: hello.py

"""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import QtCore
def clicked():
    print("toto")
    
def window():
    app = QApplication(sys.argv)
    win =QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Tech With Mehdi")
    
    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(50,50)
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(clicked)
    win.show()
    sys.exit(app.exec_())

window()