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
        for key in self.blueprint.keys():
            workout_layout = QVBoxLayout()
            workout_layout.addWidget(QLabel(key)) #workout_name 
            column_header_layout = QHBoxLayout()
            column_header_layout.addWidget(QLabel('Exercise'))
            column_header_layout.addWidget(QLabel('Intensity'))
            column_header_layout.addWidget(QLabel('Sets'))
            column_header_layout.addWidget(QLabel('Rep Range'))
            column_header_layout.addWidget(QLabel('Weight'))
            column_header_layout.addWidget(QLabel('Reps'))
            column_header_layout.addWidget(QLabel('RIR'))
            column_header_widget = QWidget()
            workout_layout.addWidget(column_header_widget)
            for exercise in self.blueprint[key]:
                row_layout = QHBoxLayout()
                row_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                row_layout.addWidget(QLabel(exercise['Exercise Name'])) #exercise_name
                row_layout.addWidget(QLabel(str(exercise['Intensity']))) #intensity
                row_layout.addWidget(QLabel(str(exercise['Sets']))) #sets
                row_layout.addWidget(QLabel(exercise['Rep Range'])) #rep_range
                #previous_workous_weight
                weight_input = QDoubleSpinBox()
                #previous_reps_compted
                reps_completed = QSpinBox()
                rir = QSpinBox()
                row_layout.addWidget(weight_input)
                row_layout.addWidget(reps_completed)
                row_layout.addWidget(rir)
                row_widget = QWidget()
                row_widget.setLayout(row_layout)
                workout_layout.addWidget(row_widget)
            workout_widget = QWidget()
            workout_widget.setLayout(workout_layout)
            self.main_layout.addWidget(workout_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)





