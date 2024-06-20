import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt

class HelpPage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(top_layout)

        self.index_button = QPushButton("☰")
        self.index_button.setStyleSheet("""
                                        QPushButton {
                                            font-size: 25px;
                                            background-color: rgba(0, 0, 0, 0);
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
            """
        )
        self.index_button.clicked.connect(self.emit_return_to_index_signal)
        layout.addWidget(self.index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        top_layout.addWidget(self.index_button)
        top_layout.addSpacing(30)

        help_label = QLabel("HELP")
        help_label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold;")
        top_layout.addWidget(help_label)

        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: dark grey;")
        layout.addWidget(scroll_area)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        self.add_paragraph("A walkthrough on how to use this application.", inner_layout)

        self.add_heading("TUTORIALS:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section is where you will be learning the concepts of SQLI and how to implement them. It is recommended that you go through this section before attending the <span>Levels</span> Section.
        """, inner_layout)

        self.add_heading("LEVELS:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section is designed to test the knowledge you have gained from the <span>Tutorials</span>. Recommended to attend the <span>Tutorials</span> Section before this. Your score will be resulted at last. Can attend multiple times. Going back resets your progress. Make sure you have marked/entered the correct answer before submitting the same and moving to the next question.
        """, inner_layout)

        self.add_heading("ABOUT:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            This section provides a description about the app.
        """, inner_layout)
        self.add_heading("CONTACT:", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            For more details or queries, contact sqlix@gmaill.com
        """, inner_layout)

    def add_heading(self, text, parent_layout, font_size, alignment):
        heading_label = QLabel(text)
        heading_label.setStyleSheet(f"font-size: {font_size}px; text-decoration: underline; letter-spacing: 2px;")
        parent_layout.addWidget(heading_label, alignment=alignment)

    def add_paragraph(self, text, parent_layout):
        paragraph_label = QLabel(text)
        paragraph_label.setStyleSheet("font-size: 25px; text-align: justify; padding: 10px 60px 60px 60px; letter-spacing: 2px;")
        paragraph_label.setWordWrap(True)

        paragraph_label.setTextFormat(Qt.TextFormat.RichText)
        paragraph_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        for word in ["Tutorials", "Levels"]:
            text = text.replace(word, f"<em>{word}</em>")

        paragraph_label.setText(text)

        parent_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()