from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import program_bluprint
import sys
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        test = program_bluprint.ProgramBluprint()
        self.setCentralWidget(test.main_widget)
        self.main_layout = QVBoxLayout()
        #Need to Make button for tabs 



app = QApplication(sys.argv)

window = MainWindow()
window.show() #VERY IMPORTANT. Main windows are invisible by default

app.exec()
