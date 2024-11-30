
import unittest
import os
from src.main import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.test_dir = test_dir
        self.test_file = test_file.txt

    def test_create_folder(self):
        self.fs.create_folder(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))

    def test_create_file(self):
        self.fs.touch_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def tearDown(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == __main__:
    unittest.main()

