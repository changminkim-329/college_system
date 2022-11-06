from sqlalchemy import create_engine
import unittest


class MyTest(unittest.TestCase):
    def test_db(self):
        url = ''
        engine = create_engine(url)

if __name__ == '__main__':  
    unittest.main()
