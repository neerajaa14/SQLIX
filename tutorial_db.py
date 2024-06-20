from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Text
import os

Base = declarative_base()

class TutorialPageContent(Base):
    __tablename__ = 'tutorial_page_content'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)

current_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(current_dir, 'tutorial_content.db')

if not os.path.exists(db_file_path):
    engine = create_engine(f'sqlite:///{db_file_path}')
    Base.metadata.create_all(engine)
else:
    engine = create_engine(f'sqlite:///{db_file_path}')

Session = sessionmaker(bind=engine)