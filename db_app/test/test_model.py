import unittest
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class Student(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(20))
    password = Column(String(50))
    email = Column(String(50),unique=True)
    age = Column(Integer)
    classes = Column(String(10))
    major_id = Column(Integer,ForeignKey('major.id'))
    majors = relationship('Major')

    def __getitem__(self,key):
        return getattr(self, key)

    

class Major(Base):
    __tablename__ = 'major'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(20),unique=True)
    desc = Column(String)
    
    def __getitem__(self,key):
        return getattr(self, key)

class MyTest(unittest.TestCase):
    def test_model(self):
        student: Student = Student()
        major : Major = Major()
        student.majors = major

        new_student = Student(
            email='test@gmail.com',name='test',password='test',age=26,
            classes='3-1',major_id=1)

        data = {'email':'test@gmail.com','name':'test','password':'test','age':26,'classes':'3-1','major_id':1}
        student = Student(**data)

    # def test_migrate(self):
    #     engine = return_engine(URL)
    #     Base.metadata.create_all(bind=engine)



if __name__ == '__main__':  
    unittest.main()