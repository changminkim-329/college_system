from sqlalchemy import create_engine
import unittest


class MyTest(unittest.TestCase):
    def test_db(self):
        url = 'mysql://root:2160@127.0.0.1:3306/COLLEGE'
        engine = create_engine(url)
        print(engine)
        
if __name__ == '__main__':  
    unittest.main()
