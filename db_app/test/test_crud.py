from sqlalchemy import create_engine
import unittest
from test_database import return_session,URL
from test_model import Student,Major
from test_schema import *
from typing import List,Dict

def get_student(session, student_email:str) -> Student:
    student = session.query(Student).filter(Student.email == student_email).first()
    return student

def get_major(session,major_name) -> Major:
    major = session.query(Major).filter(Major.name == major_name).first()
    return major



def get_students(session, offset:int, limit:int) -> List[Student]:
    students = session.query(Student).offset(offset).limit(limit).all()
    return students

def get_majors(session, offset:int, limit:int) -> List[Major]:
    majors = session.query(Major).offset(offset).limit(limit).all()
    return majors



def create_student(session,student:StudentCreate):
    new_student = Student(
        email=student.email,name=student.name,password=student.password,age=student.age,
        classes=student.classes,major_id=student.major_id)
    print(new_student)
    print("creas")
    session.add(new_student)
    a = session.commit()
    print(a)

def create_major(session,major:MajorCreate):
    new_major = Major(name=major.name,desc=major.desc)
    print(new_major)
    print("creas")
    session.add(new_major)
    a = session.commit()
    print(a)



def update_student(session, email:str,attr:dict):
    student_email = email
    student_attr = attr
    student = session.query(Student).filter(Student.email==student_email).update(student_attr)
    session.commit()
    print("출력:",student)

def update_major(session, name:str,attr:dict):
    major_name = name
    major_attr = attr
    major = session.query(Major).filter(Major.name==major_name).update(major_attr)
    session.commit()
    print("출력:",major)





class MyTest(unittest.TestCase):
    def test_crud(self):
        Session = return_session(URL)
        session = Session()
        student:Student = get_student(session,student_email='test@naver.com')
        print(type(student))
        self.assertEqual(student.id,1)

        students = get_students(session,0,3)
        if students:
            self.assertEqual(students[0].id,1)
        
        # new_student = StudentCreate(
        #     email='chang@naver.com',name='chang',password='chang',age=21,classes='3-2',major_id=1)

        # create_student(session,new_student)
        
        email='test@naver.com'
        attr={'classes':'1-2'}
        
        update_student(session,email,attr)


        major:Major = get_major(session,'computer')
        print(major)
        self.assertEqual(major.name,'computer')
        majors = get_majors(session,0,3)
        print(majors)
        if majors:
            self.assertEqual(majors[0].name,'computer')
        
        # new_major = MajorCreate(name='english',desc='영문학과')
        
        # create_major(session,new_major)
        name='english'
        attr={'desc':'영문어학과'}
        update_major(session,name,attr)

        session.close()
        

if __name__ == '__main__':  
    unittest.main()