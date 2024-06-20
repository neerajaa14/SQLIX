import sys,os
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont, QColor, QIcon
from welcome_page import WelcomePage
from index_page import IndexPage
from tutorial_page import TutorialPage
from levels_page import LevelsPage
from help_page import HelpPage
from about_page import AboutPage
from tutorial_db import Session
from tutorial_content import add_tutorial_content_to_database
from level_content import add_level_content_to_database


basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    navigateToPage = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        welcome_page = WelcomePage()
        self.setCentralWidget(welcome_page)

        # App window title and icon
        self.setWindowTitle("XSSify")
        self.setWindowIcon(QIcon(os.path.join(basedir, 'bug.png')))

        # Setting default font
        app_font = QFont("JetBrains Mono")
        QApplication.instance().setFont(app_font)

        # Setting main bg color
        main_window_color = QColor("#333333")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), main_window_color)
        self.setPalette(p)

        # Create instances of pages
        self.welcome_page = WelcomePage()
        self.index_page = IndexPage()
        session = Session()
        self.tutorial_page = TutorialPage(session)
        self.levels_page = LevelsPage()
        self.help_page = HelpPage()
        self.about_page = AboutPage()

        # Add pages to stacked widget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.welcome_page)
        self.stackedWidget.addWidget(self.index_page)
        self.stackedWidget.addWidget(self.tutorial_page)
        self.stackedWidget.addWidget(self.levels_page)
        self.stackedWidget.addWidget(self.help_page)
        self.stackedWidget.addWidget(self.about_page)
        self.setCentralWidget(self.stackedWidget)

        # Connect signals
        self.welcome_page.returnToIndexSignal.connect(self.show_index_page)
        self.index_page.navigateToPage.connect(self.navigate_to_page)
        self.tutorial_page.returnToIndexSignal.connect(self.show_index_page)
        self.levels_page.returnToIndexSignal.connect(self.show_index_page)
        self.help_page.returnToIndexSignal.connect(self.show_index_page)
        self.about_page.returnToIndexSignal.connect(self.show_index_page)

    def show_index_page(self):
        self.stackedWidget.setCurrentWidget(self.index_page)

    def navigate_to_page(self, page_name):
        if page_name == "TUTORIAL":
            self.stackedWidget.setCurrentWidget(self.tutorial_page)
        elif page_name == "LEVELS":
            self.stackedWidget.setCurrentWidget(self.levels_page)
        elif page_name == "HELP":
            self.stackedWidget.setCurrentWidget(self.help_page)
        elif page_name == "ABOUT":
            self.stackedWidget.setCurrentWidget(self.about_page)

    def center_window(self):
        screen_geo = QApplication.primaryScreen().geometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)


# Main function
if __name__ == "__main__":
    add_tutorial_content_to_database()
    add_level_content_to_database()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()
    sys.exit(app.exec())