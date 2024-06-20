import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QApplication
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, pyqtSignal

basedir = os.path.dirname(__file__)

class ArrowIcon(QWidget):
    def __init__(self, png_path, icon_size):
        super().__init__()
        pixmap = QPixmap(png_path).scaled(*icon_size)
        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

class IndexPage(QWidget):
    navigateToPage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setup_layout()

    def setup_layout(self):
        chapters_list = ["TUTORIAL", "LEVELS", "HELP"]
        path = os.path.join(basedir, 'down_arrow.png')

        # Set background image
        self.setStyleSheet("""
            QWidget {
                background-image: url('path_to_background_image.jpg');
                background-size: cover;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

        # Add a label for the app name
        app_name_label = QLabel("WELCOME TO\nSQLIX")
        app_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        app_name_label.setStyleSheet("""
            font-size: 65px;
            font-weight: bold;
            color: #FFFFFF;
            margin-top: 50px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
        """)
        main_layout.addWidget(app_name_label)

        # Create a horizontal layout for the icons
        icon_layout = QHBoxLayout()
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_layout.setSpacing(40)

        for chapter in chapters_list:
            icon_button = QPushButton(chapter)
            icon_button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    font-weight: bold;
                    background-color: qlineargradient(
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 #4CAF50, stop: 1 #81C784);
                    color: #FFFFFF;
                    border: 2px solid #FFFFFF;
                    border-radius: 15px;
                    padding: 15px 30px;
                    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
                    transition: background-color 0.3s, transform 0.3s;
                }
                
                QPushButton:hover {
                    background-color: qlineargradient(
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 #66BB6A, stop: 1 #A5D6A7);
                    transform: scale(1.05);
                }
                
                QPushButton:pressed {
                    background-color: qlineargradient(
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 #388E3C, stop: 1 #66BB6A);
                    transform: scale(0.95);
                }
            """)
            icon_button.clicked.connect(lambda _, ch=chapter: self.navigateToPage.emit(ch))
            icon_layout.addWidget(icon_button)

        main_layout.addLayout(icon_layout)

        # Add a label for the arrow icon
        arrow_icon = ArrowIcon(path, icon_size=(50, 50))
        main_layout.addWidget(arrow_icon, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = IndexPage()
    window.show()
    sys.exit(app.exec())




