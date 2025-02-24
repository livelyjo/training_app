from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from pathlib import Path
import json

class TrackerTab(QWidget):
    def __init__(self):
        super().__init__()
        with open('data.json', 'r') as file:
            self.blueprint = json.load(file)
        file_path = Path("past_data.json")
        if file_path.exists():
            with file_path.open('r') as file:
                self.past_data = json.load(file)
        else:
            self.past_data = None

        self.main_layout = QVBoxLayout()
        tracker_title = QLabel("Tracker")
        self.main_layout.addWidget(tracker_title)
        print(self.blueprint)

