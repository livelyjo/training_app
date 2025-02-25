from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import program_bluprint
import tracker
import sys
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        tracker_button = QPushButton("Tracker")
        blueprint_button = QPushButton("Bluprint")
        tracker_button.clicked.connect(self.tracker_clicked)
        blueprint_button.clicked.connect(self.blueprint_clicked)
        tab_layout = QHBoxLayout()
        tab_layout.addWidget(blueprint_button)
        tab_layout.addWidget(tracker_button)
        self.tab_widget = QWidget()
        self.tab_widget.setLayout(tab_layout)
        self.main_layout.addWidget(self.tab_widget)
        blueprint = program_bluprint.ProgramBluprint()
        self.main_layout.addWidget(blueprint.main_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

    def tracker_clicked(self):
        tracker_tab = tracker.TrackerTab()
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        layout.addWidget(tracker_tab.main_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        new_central_widget = QWidget()
        new_central_widget.setLayout(layout)
        self.setCentralWidget(new_central_widget)

    def blueprint_clicked(self):
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show() #VERY IMPORTANT. Main windows are invisible by default

app.exec()
