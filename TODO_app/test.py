import unittest
from todo_app import Frontend
from backend import Backend

class Test_Frontend(unittest.TestCase):
    def test_sys_argvs(self):
        front = Frontend()
        front.sys_argvs()


if __name__ == "__main__":
    unittest.main()

