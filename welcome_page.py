from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal

class WelcomePage(QWidget):
    returnToIndexSignal = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        # Set the background color for the entire widget
        self.setStyleSheet("background-color: #2E2E2E;")

        # Content and layout
        combined_text = '''
        <span style='font-size: 100px; color: #D4D4D4; font-weight: bold;'>
            SQLIX
        </span>
        <br>
        <span style='font-size: 20px; color: #BADA55; font-weight: regular;'>
           Guide to SQL Injection Attack
        </span>
        '''

        text_label = QLabel(combined_text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("padding: 20px; border-radius: 15px; background-color: rgba(255, 255, 255, 0.1);")

        # Main vertical layout
        main_layout = QVBoxLayout(self)

        # Spacer to push content down
        top_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        main_layout.addItem(top_spacer)

        # Adding the text label to the layout
        main_layout.addWidget(text_label)

        # Another spacer to add space between the label and the button
        middle_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        main_layout.addItem(middle_spacer)

        # Button layout
        arrow_button = QPushButton("Begin  ▶︎")
        arrow_button.setStyleSheet(
            """
                QPushButton {
                    font-size: 20px;
                    letter-spacing: 5px;
                    font-weight: bold;
                    background-color: #87CEEB;
                    border: 1px solid #FFFFFF;
                    color: #2DD096;
                    padding: 10px 20px;
                    border-radius: 10px;
                    margin: 2px;
                    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
                }
                
                QPushButton:hover {
                    background-color: #B0E0E6;
                    border: 2px solid #FFFFFF;
                }
                
                QPushButton:pressed {
                    background-color: #ADD8E6;
                    border: 2px solid #FFFFFF;
                }
            """
        )
        arrow_button.clicked.connect(self.emit_navigate_to_index_signal)

        # Horizontal layout for the button
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(arrow_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        # Spacer to push content up
        bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        main_layout.addItem(bottom_spacer)

        # Adjusting margins and spacing
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

    def emit_navigate_to_index_signal(self):
        self.returnToIndexSignal.emit()

