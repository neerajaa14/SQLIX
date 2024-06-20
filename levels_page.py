import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QRadioButton
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont
from level_db import Session, LevelPageContent

class LevelsPage(QMainWindow):
    returnToIndexSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Levels")
        self.setGeometry(100, 100, 800, 600)

        # Setting necessary variables
        self.question_index = 0
        self.score = 0
        self.questions = []

        self.load_questions()
        self.setup_intro_ui()

    def setup_intro_ui(self):
        font = QFont("JetBrains Mono", 15)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        label_intro = QLabel("Welcome to the Levels!\n\nRules and Conditions:")
        label_intro.setFont(font)
        label_intro.setStyleSheet("letter-spacing: 2px; font-weight: bold; color: #2DD096;")
        label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_intro)

        rules = [
            "- It is recommended to go through the Tutorial Sections before attending this section.",
            "- This quiz can be taken any number of times.",
            "- Each question will have multiple-choice options or require user input.",
            "- For multiple-choice questions, select the correct option.",
            "- For questions requiring user input, type your answer in the provided field.",
            "- Please ensure that the answer typed or marked is the one that you had in mind before submitting the same.",
            "- Practice till you get the perfect score.",
            "- Click the 'Start Levels' button to begin."
        ]

        for rule in rules:
            label_rule = QLabel(rule)
            label_rule.setFont(font)
            layout.addWidget(label_rule)

        btn_start = QPushButton("Start Levels")
        btn_start.setFont(font)
        btn_start.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                letter-spacing: 5px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0);
                border: 1px solid #FFFFFF;
                color: #2DD096;
                padding: 10px 20px;
                border-radius: 10px;
                margin: 6px;
            }
            
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        btn_start.clicked.connect(self.show_question)
        layout.addWidget(btn_start, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        central_widget.setStyleSheet("background-color: #333333; color: white;")  # Set background color to dark gray
        self.setCentralWidget(central_widget)

    def load_questions(self):
        session = Session()
        self.questions = session.query(LevelPageContent).all()
        session.close()

    def setup_ui(self):
        font = QFont("JetBrains Mono", 15)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)
        self.central_widget.setLayout(main_layout)

        top_layout = QHBoxLayout()
        self.hamburger_menu_button = QPushButton("☰")
        self.hamburger_menu_button.setStyleSheet("""
            QPushButton {
                font-size: 25px;
                background-color: rgba(212,212,212,1);
                color: #2DD096;
                padding: 2px 25px;
                border-radius: 5px;
            }
            
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.hamburger_menu_button.clicked.connect(self.emit_return_to_index_signal)
        top_layout.addWidget(self.hamburger_menu_button)
        top_layout.addStretch()
        main_layout.addLayout(top_layout)

        self.question_layout = QVBoxLayout()
        main_layout.addLayout(self.question_layout)

        self.label_question = QLabel()
        self.label_question.setFont(font)
        self.label_question.setStyleSheet("color: #2DD096; background-color: #2F2F2F; padding: 10px; border-radius: 10px;")
        self.label_question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_layout.addWidget(self.label_question, alignment=Qt.AlignmentFlag.AlignCenter)

        self.radio_buttons = []
        for i in range(4):
            radio_button = QRadioButton()
            radio_button.setChecked(False)
            radio_button.setFont(font)
            radio_button.setStyleSheet("color: #FFFFFF;")
            self.radio_buttons.append(radio_button)
            self.question_layout.addWidget(radio_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.answer_field = QLineEdit()
        self.answer_field.setFont(font)
        self.answer_field.setStyleSheet("color: #FFFFFF; background-color: #2F2F2F; padding: 5px; border-radius: 5px;")
        self.question_layout.addWidget(self.answer_field)

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setFont(font)
        self.btn_submit.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                letter-spacing: 10px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0);
                border: 1px solid #FFFFFF;
                color: #2DD096;
                padding: 10px 20px;
                border-radius: 10px;
                margin: 6px;
            }
            
            QPushButton:hover {
                background-color: rgba(186, 218, 85, 1);
            }
            
            QPushButton:pressed {
                background-color: rgba(45,208,85,1);
            }
        """)
        self.btn_submit.clicked.connect(self.next_question)
        main_layout.addWidget(self.btn_submit, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_return = QPushButton("Return to Index Page")
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                letter-spacing: 10px;
                font-weight: bold;
                background-color: rgba(212,212,212,1);
                border: 1px solid #FFFFFF;
                color: #2DD096;
                padding: 10px 20px;
                border-radius: 10px;
                margin: 6px;
            }
            
            QPushButton:hover {
                background-color: rgba(186, 218, 85, 1);
            }
            
            QPushButton:pressed {
                background-color: rgba(45,208,85,1);
            }
        """)
        self.btn_return.clicked.connect(self.emit_return_to_index_signal)
        self.btn_return.hide()
        main_layout.addWidget(self.btn_return, alignment=Qt.AlignmentFlag.AlignCenter)
        self.central_widget.setStyleSheet("background-color: #333333; color: white;")

    def reset(self):
        self.question_index = 0
       

        self.score = 0
        self.btn_submit.show()
        self.btn_return.hide()
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
        self.answer_field.clear()
        self.load_questions()
        self.setup_ui()
        self.show_question()

    def show_question(self):
        self.centralWidget().deleteLater()
        self.setup_ui()
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            question = question_data.question
            options = [question_data.option1, question_data.option2, question_data.option3, question_data.option4]
            requires_input = question_data.requires_input

            self.label_question.setText(question)
            self.answer_field.clear()

            if requires_input:
                self.answer_field.show()
                for radio_button in self.radio_buttons:
                    radio_button.hide()
            else:
                if options:
                    for i, option in enumerate(options):
                        self.radio_buttons[i].setText(option)
                    self.answer_field.hide()
                    for radio_button in self.radio_buttons:
                        radio_button.show()
                else:
                    self.answer_field.show()
                    for radio_button in self.radio_buttons:
                        radio_button.hide()
        else:
            for radio_button in self.radio_buttons:
                radio_button.hide()
            self.answer_field.hide()
            self.show_result()

    def next_question(self):
        typed_answer = self.answer_field.text().strip()

        selected_option_text = None
        for i, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                selected_option_text = self.radio_buttons[i].text().strip().lower()
                break

        correct_answer = self.questions[self.question_index].answer.strip().lower()

        if selected_option_text is not None and selected_option_text == correct_answer:
            self.score += 1
            QMessageBox.information(self, "MCQ Answer", "Correct answer")
        elif typed_answer.lower() == correct_answer:
            self.score += 1
            QMessageBox.information(self, "Typed Answer", "Correct answer")
        else:
            QMessageBox.information(self, "Answer", "Incorrect answer")

        self.question_index += 1
        self.show_question()

    def show_result(self):
        result_msg = f"Your score: {self.score}/{len(self.questions)}"
        QMessageBox.information(self, "Quiz Finished", result_msg)
        self.btn_return.show()
        self.btn_submit.hide()

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit("Returning to Index")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LevelsPage()
    window.show()
    sys.exit(app.exec())




