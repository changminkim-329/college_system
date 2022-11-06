import unittest
from pydantic import BaseModel
from typing import Union, Dict


class StudentBase(BaseModel):
    email: str

class StudentCreate(StudentBase):
    name: str
    password: str
    age: int
    classes: str
    major_id: int

class StudentUpdate(StudentBase):
    attr: Union[Dict[str,Union[str,int,None]],None] = None



class MajorBase(BaseModel):
    name: str

class MajorCreate(MajorBase):
    desc: str

class MajorUpdate(MajorBase):
    attr: Union[Dict[str,Union[str,int,None]],None] = None



class MyTest(unittest.TestCase):
    def test_schema(self):
        student = StudentCreate(
            name='test',email='test@naver.com',
            password='test',age=20,classes='4-1',major_id=1)
        
        self.assertEqual(student.age,20)
        self.assertNotEqual(student.name,'test1')

        student = StudentBase(email='test@naver.com')
        self.assertEqual(student.email,'test@naver.com')
        
        student = StudentUpdate(email='test@naver.com')
        print(student.attr)

        major = MajorCreate(name='test',desc="test")
        self.assertNotEqual(major.name,'test1')
        self.assertEqual(major.desc,'test')


        major = MajorUpdate(name='test',attr={'hello':5})
        self.assertIsNotNone(major.attr)
        major = MajorUpdate(name='test2')
        self.assertIsNone(major.attr)



if __name__ == '__main__':  
    unittest.main()