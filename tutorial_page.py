
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QSizePolicy, QGridLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap
from tutorial_db import Session, TutorialPageContent

basedir = os.path.dirname(__file__)

class TutorialPage(QWidget):
    returnToIndexSignal = pyqtSignal()
    resetPageSignal = pyqtSignal()

    def __init__(self, session):
        super().__init__()

        self.page_state = "initial"
        self.session = session
        self.chapters = self.fetch_chapter_titles()
        self.current_chapter_index = 0
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.GlobalColor.darkGray)
        self.setPalette(p)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        top_layout = QHBoxLayout()
        self.setup_index_button(top_layout)
        main_layout.addLayout(top_layout)

        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: #333333;")
        scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(scroll_area)

        inner_widget = QWidget()
        self.inner_layout = QVBoxLayout(inner_widget)
        self.inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.inner_layout.addWidget(self.content_widget)

        self.bottom_layout = QHBoxLayout()
        main_layout.addLayout(self.bottom_layout)

        self.setLayout(main_layout)

        self.show_initial_page()

    def setup_index_button(self, layout):
        index_button = QPushButton("☰")
        index_button.clicked.connect(self.emit_return_to_index_signal)
        index_button.setStyleSheet(
            """
                QPushButton {
                    font-size: 25px;
                    background-color: rgba(215,215,215,1);
                    color: #2DD096;
                    padding: 2px 25px;
                    border-radius: 5px;
                }
                
                QPushButton:hover {
                    background-color: rgba(186, 218, 85, 1);
                }
                
                QPushButton:pressed {
                    background-color: rgba(85, 208, 150, 1);
                }
            """
        )
        layout.addWidget(index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def show_initial_page(self):
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        tutorial_label = QLabel("TUTORIALS")
        tutorial_label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold; color: #FFFFFF;")
        tutorial_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(tutorial_label)

        self.add_paragraph("Welcome to the <span>Tutorials</span> Section. This is where you will be learning what SQLi is, what tools are available to perform XSS attacks on vulnerable websites, how you can prevent them from happening, and you will also get to know some real-life incidents of SQLi attacks. It is advised to complete this section first in order to answer the questions provided in the <span>Levels</span> Section.", self.content_layout)

        self.add_heading("CHAPTERS:", self.content_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)

        chapters_widget = QWidget()
        chapters_layout = QGridLayout(chapters_widget)
        chapters_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        row = 0
        col = 0
        for chapter_title in self.chapters:
            if col >= 3:  # Assuming 3 chapters per row
                col = 0
                row += 1
            self.add_chapter_button(chapter_title, chapters_layout, row, col)
            col += 1

        self.content_layout.addWidget(chapters_widget)

        btn_cont = QPushButton("Continue")
        btn_cont.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
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
                """
        )
        btn_cont.clicked.connect(self.show_current_chapter)
        self.bottom_layout.addWidget(btn_cont)

    def add_chapter_button(self, chapter_title, parent_layout, row, col):
        chapter_button = QPushButton(chapter_title)
        chapter_button.setStyleSheet("""
            QPushButton {
                font-size: 25px;
                background-color: rgba(0, 0, 0, 0);
                color: #2DD096;
                padding: 5px 25px;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            
            QPushButton:hover {
                background-color: rgba(186,218,85,1);
            }
            
            QPushButton:pressed {
                background-color: rgba(45, 208, 150, 1);
            }
        """)
        chapter_button.clicked.connect(lambda _, title=chapter_title: self.show_page_by_title(title))
        parent_layout.addWidget(chapter_button, row, col)
    
    def add_heading(self, text, parent_layout, font_size, alignment):
        heading_label = QLabel(text)
        heading_label.setStyleSheet(f"font-size: {font_size}px; text-decoration: underline; letter-spacing: 2px; padding-bottom: 10px; color: #FFFFFF;")
        heading_label.setAlignment(alignment)
        parent_layout.addWidget(heading_label)

    def add_paragraph(self, text, parent_layout):
        paragraph_label = QLabel(text)
        paragraph_label.setStyleSheet("font-size: 25px; text-align: justify; padding: 10px 60px 60px 60px; letter-spacing: 2px; color: #FFFFFF;")
        paragraph_label.setWordWrap(True)
        paragraph_label.setTextFormat(Qt.TextFormat.RichText)
        paragraph_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        parent_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)

    def show_page_by_title(self, title):
        self.clear_layout(self.content_layout)
        self.clear_layout(self.bottom_layout)

        clicked_index = self.chapters.index(title)
        self.current_chapter_index = clicked_index

        tutorial_content = self.fetch_tutorial_content(title)
        
        if tutorial_content:
            heading = QLabel(tutorial_content.title)
            heading.setStyleSheet("font-size: 36px; color: #2DD096; font-weight: bold; text-decoration: underline;")
            heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.content_layout.addWidget(heading)

            content = tutorial_content.content.strip().split('\n\n')            
            for idx, paragraph in enumerate(content):
                paragraph_label = QLabel(paragraph)
                paragraph_label.setStyleSheet("font-size: 24px; color: white; font-weight: regular; text-align: justify;")
                paragraph_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
                paragraph_label.setWordWrap(True)
                self.content_layout.addWidget(paragraph_label)

                if paragraph.startswith("IMAGE 1:"):
                    image_label = QLabel()
                    pixmap = QPixmap(os.path.join(basedir, 'vulnweb.png'))
                    image_label.setPixmap(pixmap)
                    self.content_layout.addWidget(image_label)
                elif paragraph.startswith("IMAGE 2:"):
                    image_label = QLabel()
                    pixmap = QPixmap(os.path.join(basedir, 'pwnxss.png'))
                    image_label.setPixmap(pixmap)
                    self.content_layout.addWidget(image_label)
                elif paragraph.startswith("IMAGE 3:"):
                    image_label = QLabel()
                    pixmap = QPixmap(os.path.join(basedir, 'cookie.png'))
                    image_label.setPixmap(pixmap)
                    self.content_layout.addWidget(image_label)

        self.add_navigation_buttons()

    def fetch_tutorial_content(self, title):
        tutorial_content = self.session.query(TutorialPageContent).filter_by(title=title).first()
        return tutorial_content

    def fetch_chapter_titles(self):
        titles = [chapter.title for chapter in self.session.query(TutorialPageContent).all()]
        return titles

    def show_current_chapter(self):
        title = self.chapters[self.current_chapter_index]
        self.show_page_by_title(title)

    def show_previous_chapter(self):
        self.current_chapter_index -= 1
        if self.current_chapter_index < 0:
            self.current_chapter_index = 0
            self.show_initial_page()
        else:
            self.show_current_chapter()

    def show_next_chapter(self):
        self.current_chapter_index += 1
        if self.current_chapter_index >= len(self.chapters):
            self.current_chapter_index = len(self.chapters) - 1
        self.show_current_chapter()

    def add_navigation_buttons(self):
        btn_prev = QPushButton("Prev")
        btn_prev.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
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
                """
        )
        btn_prev.clicked.connect(self.show_previous_chapter)
        self.bottom_layout.addWidget(btn_prev)

        btn_home = QPushButton("Back to Home")
        btn_home.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
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
                """
        )
        btn_home.clicked.connect(self.emit_return_to_index_signal)
        self.bottom_layout.addWidget(btn_home)

        btn_next = QPushButton("Next")
        btn_next.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
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
                """
        )
        btn_next.clicked.connect(self.show_next_chapter)
        self.bottom_layout.addWidget(btn_next)

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

# Example usage:
# Assuming session is an instance of SQLAlchemy session
# session = Session()
# tutorial_page = TutorialPage(session)
# tutorial_page.returnToIndexSignal.connect(some_function_to_handle_return_to_index)
