from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.data = {}
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

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def template_helper(self):
        self.main_layout.removeWidget(self.add_template_button)
        self.add_template()
        self.main_layout.addWidget(self.add_template_button)

    def add_template(self):
        template_layout = QVBoxLayout()
        self.data[f'template_{self.count}'] = template_layout
        self.count += 1
        layout = self.label_placer("Workout Name:", QLineEdit(), 'l')
        widget = QWidget()
        widget.setLayout(layout)
        template_layout.addWidget(widget)
        delete_template_button = QPushButton("Delete Workout")
        template_layout.addWidget(delete_template_button)
        self.add_exercise(template_layout)
        add_exercise_button = QPushButton("Add Exercise")
        add_exercise_button.setMaximumWidth(300)
        add_exercise_button.clicked.connect(lambda: self.move_add_exercise_button(template_layout, add_exercise_button))
        template_layout.addWidget(add_exercise_button)
        widget = QWidget()
        widget.setLayout(template_layout)
        self.main_layout.addWidget(widget)
        delete_template_button.clicked.connect(lambda: self.delete_workout_button(widget, self.count))
        self.count += 1

    def add_exercise(self, workout_template):
        workout_layout = QGridLayout()
        workout_layout.addLayout(self.label_placer('Order:', QSpinBox(), 't'), 1, 0)
        workout_layout.addLayout(self.label_placer('Exercise:', QLineEdit(), 't'), 1, 1)
        workout_layout.addLayout(self.label_placer('Intensity:', QSpinBox(), 't'), 1, 2)
        workout_layout.addLayout(self.label_placer('Sets:', QSpinBox(), 't'), 1, 3)
        workout_layout.addLayout(self.label_placer('Rep Range:', QLineEdit(), 't'), 1, 4)
        delete_exercise_button = QPushButton("Delete")
        workout_layout.addLayout(self.label_placer('', delete_exercise_button, 't'), 1, 5)
        widget = QWidget()
        widget.setLayout(workout_layout)
        delete_exercise_button.clicked.connect(lambda: self.delete_exercise_button(widget, workout_template))
        workout_template.addWidget(widget)

    def move_add_exercise_button(self, workout_template, button):
        workout_template.removeWidget(button)
        self.add_exercise(workout_template)
        workout_template.addWidget(button)

    def delete_exercise_button(self, exercise_widget, workout_template):
        exercise_widget.hide()
        workout_template.removeWidget(exercise_widget)
        exercise_widget.deleteLater()

    def delete_workout_button(self, template_widget, count):
        del self.data[f'template_{count}']
        template_widget.hide()
        self.main_layout.removeWidget(template_widget)
        template_widget.deleteLater()

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
        with open("data.json", "w") as file:
            json.dump(self.data, file, indent=4)



app = QApplication(sys.argv)

window = MainWindow()
window.show() #VERY IMPORTANT. Main windows are invisible by default

app.exec()
