from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Training App")
        label = QLabel("Program Blueprint")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.main_layout = QVBoxLayout()


        self.main_layout.addWidget(label)
        self.add_exercise()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def add_exercise(self):
        workout_layout = QGridLayout()
        workout_layout.addLayout(self.label_placer('Name:', QLineEdit(), 't'), 0, 0)
        workout_layout.addLayout(self.label_placer('Order:', QSpinBox(), 't'), 1, 0)
        workout_layout.addLayout(self.label_placer('Exercise:', QLineEdit(), 't'), 1, 1)
        workout_layout.addLayout(self.label_placer('Intensity:', QSpinBox(), 't'), 1, 2)
        workout_layout.addLayout(self.label_placer('Sets:', QSpinBox(), 't'), 1, 3)
        workout_layout.addLayout(self.label_placer('Rep Range:', QLineEdit(), 't'), 1, 4)
        delete_exercise_button = QPushButton("Delete")
        workout_layout.addLayout(self.label_placer('', delete_exercise_button, 't'), 1, 5)
        add_exercise_button = QPushButton("Add Exercise")
        add_exercise_button.clicked.connect(lambda: self.add_exercise_button(workout_layout, add_exercise_button))
        workout_layout.addWidget(add_exercise_button, 2, 0)
        widget = QWidget()
        widget.setLayout(workout_layout)
        delete_exercise_button.clicked.connect(lambda: self.delete_exercise_button(widget))
        self.main_layout.addWidget(widget)

    def add_exercise_button(self, layout, button):
        button.hide()
        layout.removeWidget(button)
        button.deleteLater()
        self.add_exercise()

    def delete_exercise_button(self, exercise_widget):
        exercise_widget.hide()
        self.main_layout.removeWidget(exercise_widget)
        exercise_widget.deleteLater()


    def label_placer(self, title, q_widget, orientation):
        label = QLabel(title)
        if orientation == 'l':
            layout = QHBoxLayout()
            layout.addWidget(label)
            layout.addWidget(q_widget)
            return layout
        elif orientation == 'r':
            layout = QHBoxLayout()
            layout.addWidget(q_widget)
            layout.addWidget(label)
            return layout
        elif orientation == 'b':
            layout = QVBoxLayout()
            layout.addWidget(q_widget)
            layout.addWidget(label)
            return layout
        elif orientation == 't':
            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(q_widget)
            return layout



app = QApplication(sys.argv)

window = MainWindow()
window.show() #VERY IMPORTANT. Main windows are invisible by default

app.exec()
