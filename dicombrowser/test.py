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

    def get_next_test_directory(self):
        curdir = os.path.dirname(os.path.abspath(__file__))
        expected_results = {os.path.join(curdir, 'testdirectory/slice'):
                                {'Patient\'s Name': 'Anonymized', 'Number Of Files': 1,
                                 'First Filename': 'Anonymized20170603.dcm'},
                            os.path.join(curdir, 'testdirectory/series'):
                                {'Patient\'s Name': 'Anonymized', 'Number Of Files': 11,
                                 'First Filename': 'image-000000.dcm'}
                            }
        for subdir, expected_result in expected_results.items():
            yield subdir, expected_result

    def test_can_init_browser(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)
            self.assertIsNotNone(tree)
            self.assertIsInstance(tree, dict)

    def test_can_find_all_dicom_files_in_directory(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)
            self.assertIsNotNone(tree)
            self.assertEqual(len(tree), expected_result['Number Of Files'])

    def test_first_file_patientsname(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)

            first_filename = os.path.join(directory, expected_result['First Filename'])
            self.assertEqual(tree[first_filename]['Patient\'s Name'], expected_result['Patient\'s Name'])

    def test_keeps_alphabetic_sorting(self):

        for directory, expeced_result in self.get_next_test_directory():
            tree = db.browse(directory)

            self.assertListEqual(sorted(tree.keys()), list(tree.keys()))

    def test_reads_tag_values_correctly(self):
        pass



if __name__ == "__main__":
    unittest.main()
