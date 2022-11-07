from sqlalchemy import create_engine
import unittest
from test_database import return_session,URL
from test_model import Student,Major
from test_schema import *
from typing import List,Dict

def get_object(session, Object, key, value):
    objects:Object = session.query(Object).filter(key == value).first()
    return objects

# def get_student(session, student_email:str) -> Student:
#     student = session.query(Student).filter(Student.email == student_email).first()
#     return student

# def get_major(session,major_name) -> Major:
#     major = session.query(Major).filter(Major.name == major_name).first()
#     return major


def get_objects(session, Object, offset:int, limit:int):
    objects:List[Object] = session.query(Object).offset(offset).limit(limit).all()
    return objects

# def get_students(session, offset:int, limit:int) -> List[Student]:
#     students = session.query(Student).offset(offset).limit(limit).all()
#     return students

# def get_majors(session, offset:int, limit:int) -> List[Major]:
#     majors = session.query(Major).offset(offset).limit(limit).all()
#     return majors



def create_object(session,Object,new_object_info):
    new_object:Object = Object(**new_object_info)
    session.add(new_object)
    a = session.commit()

# def create_student(session,student:StudentCreate):
#     new_student = Student(
#         email=student.email,name=student.name,password=student.password,age=student.age,
#         classes=student.classes,major_id=student.major_id)
#     print(new_student)
#     print("creas")
#     session.add(new_student)
#     a = session.commit()
#     print(a)

# def create_major(session,major:MajorCreate):
#     new_major = Major(name=major.name,desc=major.desc)
#     print(new_major)
#     print("creas")
#     session.add(new_major)
#     a = session.commit()
#     print(a)



def update_object(session, Object,key, value, attr:dict):
    objects = session.query(Object).filter(key==value).update(attr)
    session.commit()

# def update_student(session, email:str,attr:dict):
#     student_email = email
#     student_attr = attr
#     student = session.query(Student).filter(Student.email==student_email).update(student_attr)
#     session.commit()
#     print("출력:",student)

# def update_major(session, name:str,attr:dict):
#     major_name = name
#     major_attr = attr
#     major = session.query(Major).filter(Major.name==major_name).update(major_attr)
#     session.commit()
#     print("출력:",major)





class MyTest(unittest.TestCase):
    def test_crud(self):
        Session = return_session(URL)
        session = Session()

        print("테스트 1")
        student:Student = get_object(session,Student,key=Student.email,value='test@naver.com')
        self.assertEqual(student.id,1)

        # students = get_students(session,0,3)
        students:List[Student] = get_objects(session,Student,0,3)
        if students:
            self.assertEqual(students[0].id,1)
        
        # new_student = StudentCreate(
        #     email='deny@naver.com',name='deny',password='deny',age=27,classes='4-2',major_id=2)
        # print(new_student.dict())
        # create_object(session,Student,new_student.dict())
        # create_student(session,new_student)
        
        email='test@naver.com'
        attr={'classes':'1-2'}
        update_object(session,Student,Student.email,email,attr)
        # update_student(session,email,attr)

        print("테스트 2")
        major:Major = get_object(session,Major,Major.name,'computer')
        self.assertEqual(major.name,'computer')
        
        # majors = get_majors(session,0,3)
        majors:List[Major] = get_objects(session,Major,0,3)
        if majors:
            self.assertEqual(majors[0].name,'computer')
        
        # new_major = MajorCreate(name='math',desc='수학과')
        # create_object(session,Major,new_major.dict())
        # create_major(session,new_major)
        
        name='english'
        attr={'desc':'영문어학과'}
        update_object(session,Major,Major.name,name,attr)
        # update_major(session,name,attr)

        session.close()
        

if __name__ == '__main__':  
    unittest.main()