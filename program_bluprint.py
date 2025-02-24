from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import json

class ProgramBluprint(QWidget):
    def __init__(self):
        super().__init__()

        self.data = {}
        self.exercise_count = 0
        self.count = 1
        self.setWindowTitle("Training App")
        label = QLabel("Program Blueprint")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.main_layout = QVBoxLayout()


        self.main_layout.addWidget(label)
        save_button = QPushButton("Save")
        save_button.setMaximumWidth(200)
        save_button.clicked.connect(self.save_data)
        self.main_layout.addWidget(save_button)
        self.add_template()
        self.add_template_button = QPushButton("Add Workout")
        self.add_template_button.clicked.connect(self.template_helper)
        self.main_layout.addWidget(self.add_template_button)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

    def template_helper(self):
        self.main_layout.removeWidget(self.add_template_button)
        self.add_template()
        self.main_layout.addWidget(self.add_template_button)

    def add_template(self):
        template_layout = QVBoxLayout()
        workout_name_widget = QLineEdit()
        layout = self.label_placer("Workout Name:", workout_name_widget, 'l')
        widget = QWidget()
        widget.setLayout(layout)
        template_layout.addWidget(widget)
        delete_template_button = QPushButton("Delete Workout")
        template_layout.addWidget(delete_template_button)
        template_id = self.count
        widget = QWidget()
        widget.setLayout(template_layout)
        self.data[f'template_{template_id}'] = [workout_name_widget, {}]
        self.count += 1
        self.add_exercise(template_layout, template_id)
        add_exercise_button = QPushButton("Add Exercise")
        add_exercise_button.setMaximumWidth(300)
        add_exercise_button.clicked.connect(lambda: self.move_add_exercise_button(template_layout, add_exercise_button, template_id))
        template_layout.addWidget(add_exercise_button)
        self.main_layout.addWidget(widget)
        delete_template_button.clicked.connect(lambda: self.delete_workout_button(widget, template_id))

    def add_exercise(self, workout_template, template_id):
        workout_layout = QGridLayout()
        order_widget = QSpinBox()
        exercise_name_widget = QLineEdit()
        intensity_widget = QSpinBox()
        sets_widget = QSpinBox()
        rep_range_widget = QLineEdit()
        workout_layout.addLayout(self.label_placer('Order:', order_widget, 't'), 1, 0)
        workout_layout.addLayout(self.label_placer('Exercise:', exercise_name_widget, 't'), 1, 1)
        workout_layout.addLayout(self.label_placer('Intensity:', intensity_widget, 't'), 1, 2)
        workout_layout.addLayout(self.label_placer('Sets:', sets_widget, 't'), 1, 3)
        workout_layout.addLayout(self.label_placer('Rep Range:', rep_range_widget, 't'), 1, 4)
        delete_exercise_button = QPushButton("Delete")
        workout_layout.addLayout(self.label_placer('', delete_exercise_button, 't'), 1, 5)
        exercise_widget = QWidget()
        exercise_widget.setLayout(workout_layout)
        workout_template.addWidget(exercise_widget)
        exercise_key = self.exercise_count
        self.exercise_count += 1
        self.data[f"template_{template_id}"][1][exercise_key] = [order_widget, exercise_name_widget, intensity_widget, sets_widget, rep_range_widget]
        delete_exercise_button.clicked.connect(lambda: self.delete_exercise_button(exercise_widget, workout_template, template_id, exercise_key))

    def move_add_exercise_button(self, workout_template, button, template_id):
        workout_template.removeWidget(button)
        self.add_exercise(workout_template, template_id)
        workout_template.addWidget(button)

    def delete_exercise_button(self, exercise_widget, workout_template, template_id, exercise_key):
        exercise_widget.hide()
        workout_template.removeWidget(exercise_widget)
        exercise_widget.deleteLater()
        del self.data[f'template_{template_id}'][1][exercise_key]

    def delete_workout_button(self, template_widget, template_id):
        template_widget.hide()
        self.main_layout.removeWidget(template_widget)
        template_widget.deleteLater()
        del self.data[f'template_{template_id}']

    def label_placer(self, title, q_widget, orientation):
        label = QLabel(title)
        layout = QHBoxLayout()
        if orientation == 'l':
            layout.addWidget(label)
            layout.addWidget(q_widget)
            return layout
        elif orientation == 'r':
            layout.addWidget(q_widget)
            layout.addWidget(label)
            return layout
        elif orientation == 'b':
            layout.addWidget(q_widget)
            layout.addWidget(label)
            return layout
        elif orientation == 't':
            layout.addWidget(label)
            layout.addWidget(q_widget)
            return layout

    def save_data(self):
        """Working on saving Data"""
        result = {}
        for key in self.data:
            workout_name_widget, exercise_dict= self.data[key]
            result[workout_name_widget.text()] = []
            for exercise in exercise_dict.values():
                result[workout_name_widget.text()].append({
                    "Order": exercise[0].value(),
                    "Execise Name": exercise[1].text(),
                    "Intensity": exercise[2].value(),
                    "Sets": exercise[3].value(),
                    "Rep Range": exercise[4].text()
                })
        print(result)
        with open("data.json", "w") as file:
            json.dump(result, file, indent=4)
