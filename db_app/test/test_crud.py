from sqlalchemy import create_engine
import unittest
from test_database import return_session,URL
from test_model import Student,Major
from test_schema import *
from typing import List

class CollegeCRUD():
    def __init__(self, session, Object, key):
        self.session = session
        self.Object = Object
        self.key = key

    def read(self, value):
        objects = self.session.query(self.Object).filter(self.key == value).first()
        return objects

    def read_plural(self, offset:int, limit:int):
        objects = self.session.query(self.Object).offset(offset).limit(limit).all()
        return objects

    def create(self,new_object_info):
        new_object = self.Object(**new_object_info)
        self.session.add(new_object)
        self.session.commit()

    def update(self, value, attr:dict):
        self.session.query(self.Object).filter(self.key==value).update(attr)
        self.session.commit()

    @staticmethod
    def student(session):
        return StudentCRUD(session)

    @staticmethod
    def major(session):
        return MajorCRUD(session)

class StudentCRUD(CollegeCRUD):
    def __init__(self, session):
        super().__init__(session, Student,Student.email)
        self.name = 'student'

class MajorCRUD(CollegeCRUD):
    def __init__(self, session):
        super().__init__(session, Major,Major.name)







class MyTest(unittest.TestCase):
    def test_crud(self):
        Session = return_session(URL)
        session = Session()

        test_student = CollegeCRUD.student(session)
        print(test_student.name)

        print("테스트 1")
        student:Student = test_student.read('test@naver.com')
        # student:Student = get_object(session,Student,key=Student.email,value='test@naver.com')
        self.assertEqual(student.id,1)
        self.assertNotEqual(student.id,2)
        student:Student = test_student.read('chang@naver.com')
        self.assertEqual(student.id,2)
        self.assertNotEqual(student.id,3)

        # students = get_students(session,0,3)
        students:List[Student] = test_student.read_plural(0,3)
        # students:List[Student] = get_objects(session,Student,0,3)
        if students:
            self.assertEqual(students[0].id,1)
            self.assertEqual(students[1].id,2)
            self.assertNotEqual(students[1].id,3)
        
        new_student = StudentCreate(
            email='jin@naver.com',name='jin',password='jin',age=22,classes='3-2',major_id=4)
        test_student.create(new_student.dict())
        student:Student = test_student.read(new_student.email)
        self.assertEqual(student.classes,new_student.classes)
        self.assertEqual(student.password,new_student.password)
        # create_object(session,Student,new_student.dict())
        # create_student(session,new_student)
        
        email='test@naver.com'
        attr={'classes':'1-2'}
        test_student.update(email,attr)
        student:Student = test_student.read(email)
        self.assertEqual(student.classes,attr['classes'])
        self.assertNotEqual(student.classes,'1-3')
        # update_object(session,Student,Student.email,email,attr)
        # update_student(session,email,attr)

        print("테스트 2")
        test_major = CollegeCRUD.major(session)
        major:Major = test_major.read('computer')
        # major:Major = get_object(session,Major,Major.name,'computer')
        self.assertEqual(major.name,'computer')
        self.assertNotEqual(major.name,'math')
        major:Major = test_major.read('math')
        self.assertEqual(major.id,3)
        self.assertNotEqual(major.id,1)
        
        # majors = get_majors(session,0,3)
        majors:List[Major] = test_major.read_plural(0,3)
        # majors:List[Major] = get_objects(session,Major,0,3)
        if majors:
            self.assertEqual(majors[0].name,'computer')
            self.assertEqual(majors[1].id,2)
            self.assertNotEqual(majors[1].id,3)
        
        new_major = MajorCreate(name='japen',desc='일본어학과')
        test_major.create(new_major.dict())
        major:Major = test_major.read(new_major.name)
        self.assertEqual(major.desc,new_major.desc)
        self.assertEqual(major.name,new_major.name)
        # create_object(session,Major,new_major.dict())
        # create_major(session,new_major)
        
        name='english'
        attr={'desc':'영문어학과'}
        test_major.update(name,attr)
        major:Major = test_major.read(name)
        self.assertEqual(major.desc,attr['desc'])
        self.assertNotEqual(major.desc,'수학과')
        # update_object(session,Major,Major.name,name,attr)
        # update_major(session,name,attr)

        session.close()
        

if __name__ == '__main__':  
    unittest.main()