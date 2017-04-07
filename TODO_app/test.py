import unittest
from todo_app import Frontend
from backend import Backend

class Test_Todo(unittest.TestCase):
    def test_open(self):
        open = Backend()
        self.assertEquals(open.open_separate(), [["0","test\n"]])
        
if __name__ == "__main__":
    unittest.main()

