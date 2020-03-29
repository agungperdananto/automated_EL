import local_settings as settings
from sqlalchemy import bool, Column, ForeignKey, create_engine, Integer, MetaData, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()



class Course(Base):
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    is_active = Column(bool)


class Forum(Base):
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship("Course", back_populates="courses")
    forum_id = Column(Integer)
    is_active = Column(bool)


class ForumSubject(Base):
    id = Column(Integer, primary_key=True)
    forum_id = Column(Integer, ForeignKey('forum.id'))
    forum = relationship("Forum", back_populates="forum_subjects")
    subject = Column(String)
    is_active = Column(bool)

# def migrate_all():
#     meta = MetaData()
#     meta.create_all()
