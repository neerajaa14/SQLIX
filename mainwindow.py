import sys
from PyQt6.QtWidgets import QMainWindow, QStackedWidget , QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from homepage import HomePage
from Tutorialpage import TutorialPage
from LevelsPage import LevelsPage
from HelpPage import HelpPage

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("sqlix")  # Set the window title to "sqlix"

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_page = HomePage()
        self.tutorial_page = TutorialPage()
        self.levels_page = LevelsPage()
        self.help_page = HelpPage()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.tutorial_page)
        self.stacked_widget.addWidget(self.levels_page)
        self.stacked_widget.addWidget(self.help_page)

        self.home_page.tutorial_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.tutorial_page))
        self.home_page.levels_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.levels_page))
        self.home_page.help_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.help_page))

        self.tutorial_page.home_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))
        self.levels_page.home_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))
        self.help_page.home_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()
    sys.exit(app.exec())