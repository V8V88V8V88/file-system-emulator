import unittest
import os
from src.main import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.test_dir = "test_dir"
        self.test_file = "test_file.txt"

    def test_create_folder(self):
        self.fs.create_folder(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))

    def test_create_file(self):
        self.fs.touch_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_remove_file(self):
        self.fs.touch_file(self.test_file)
        self.fs.remove_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))

    def test_change_directory(self):
        self.fs.create_folder(self.test_dir)
        current_dir = os.getcwd()
        self.fs.change_directory(self.test_dir)
        self.assertEqual(os.getcwd(), os.path.join(current_dir, self.test_dir))
        self.fs.change_directory(current_dir)  # Reset back to original directory

    def test_file_size(self):
        self.fs.touch_file(self.test_file)
        with open(self.test_file, "w") as f:
            f.write("test content")
        size = os.path.getsize(self.test_file)
        self.assertGreater(size, 0)

    def test_view_logs(self):
        self.fs.log_command("test_command")
        with open('fs_emulator.log', 'r') as log_file:
            logs = log_file.read()
        self.assertIn("test_command", logs)

    def test_timestamped_file(self):
        self.fs.timestamped_file(self.test_file)
        files = [f for f in os.listdir('.') if f.startswith(self.test_file)]
        self.assertTrue(len(files) > 0)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        for file in os.listdir('.'):
            if file.startswith(self.test_file):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()
