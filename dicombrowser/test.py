import unittest
import dicombrowser as db
import os


class TestBrowser(unittest.TestCase):
    # def __init__(self):
    #    pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_init_browser(self):
        directory = "testdirectory"
        tree = db.browse(directory)
        self.assertIsNotNone(tree)
        self.assertIsInstance(tree, dict)

    def test_can_find_all_dicom_files_in_directory(self):
        directories = {"testdirectory/slice": 1, "testdirectory/series": 361}
        for directory in directories:
            testdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)
            tree = db.browse(testdir)
            self.assertIsNotNone(tree)
            self.assertEqual(len(tree), directories[directory])


if __name__ == "__main__":
    unittest.main()
