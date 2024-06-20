from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
import os

Base = declarative_base()

class LevelPageContent(Base):
    __tablename__ = 'levels_ques_ans'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)
    answer = Column(String)
    requires_input = Column(Integer)

current_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(current_dir, 'level_content.db')

if not os.path.exists(db_file_path):
    engine = create_engine(f'sqlite:///{db_file_path}')
    Base.metadata.create_all(engine)
else:
    engine = create_engine(f'sqlite:///{db_file_path}')

Session = sessionmaker(bind=engine)