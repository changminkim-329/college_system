from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest

URL = 'sqlite:///./test_db.db'
def return_engine(url):
    # url = 'mysql://root:2160@127.0.0.1:3306/COLLEGE'
    engine = create_engine(url)
    return engine

def return_session(url):
    engine = return_engine(url)
    Session = sessionmaker(bind=engine,autocommit=False)
    return Session

class MyTest(unittest.TestCase):
    def test_db(self):
        Session = return_session(URL)
        session = Session()
        session.close()
        

if __name__ == '__main__':  
    unittest.main()
