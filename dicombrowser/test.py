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
        dicoms_count = {"testdirectory/slice": 1, "testdirectory/series": 11}
        for directory in dicoms_count:
            testdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)
            tree = db.browse(testdir)
            self.assertIsNotNone(tree)
            self.assertEqual(len(tree), dicoms_count[directory])

    def test_first_file_patientsname(self):
        fnames = {"testdirectory/slice": ('Anonymized20170603.dcm', 'Anonymized'),
                  "testdirectory/series": ('image-000000.dcm', 'Anonymized')}
        for directory in fnames:
            testdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)
            tree = db.browse(testdir)

            first_filename = os.path.join(testdir, fnames[directory][0])

            self.assertEqual(tree[first_filename]['Patient\'s Name'], fnames[directory][1])

    def test_keeps_alphabetic_sorting(self):
        subdirs = ("testdirectory/slice", "testdirectory/series")
        for directory in subdirs:
            testdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)
            tree = db.browse(testdir)

            self.assertListEqual(sorted(tree.keys()), list(tree.keys()))


if __name__ == "__main__":
    unittest.main()
