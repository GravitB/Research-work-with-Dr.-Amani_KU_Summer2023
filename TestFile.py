import unittest

from src.main import read_text_files


class MyTestCase(unittest.TestCase):
    def test_read_text_files(self):
        file_contents = []
        file_contents = read_text_files(file_paths=["C:\\files\M1.txt"])
        self.assertEqual(file_contents[0], "Gravit")  # add assertion here


if __name__ == '__main__':
    unittest.main()
