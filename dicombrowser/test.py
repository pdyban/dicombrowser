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
                                 'Test Filename': 'Anonymized20170603.dcm',
                                 'Spacing Between Slices': 0.5,
                                 'Window Width': ['00350', '00350'],
                                 'Series Instance UID': '1.2.826.0.1.3680043.8.1055.1.20111102150758591.96842950.07877442',
                                 'Patient\'s Age': '000Y',
                                 'Filter By Tags': ['Patient\'s Name', 'Patient\'s Age', 'Spacing Between Slices']},
                            os.path.join(curdir, 'testdirectory/series'):
                                {'Patient\'s Name': 'Anonymized', 'Number Of Files': 11,
                                 'Test Filename': 'image-000000.dcm',
                                 'Spacing Between Slices': 4.5,
                                 'Window Width': '4005',
                                 'Series Instance UID': '1.2.826.0.1.3680043.8.1055.1.20111103111204584.92619625.78204558',
                                 'Patient\'s Age': '000Y',
                                 'Filter By Tags': ['Patient\'s Name', 'Patient\'s Age']},
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

    def test_correct_patientsname(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)

            test_filename = os.path.join(directory, expected_result['Test Filename'])
            self.assertEqual(tree[test_filename]['Patient\'s Name'], expected_result['Patient\'s Name'])

    def test_keeps_alphabetic_sorting(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)

            self.assertListEqual(sorted(tree.keys()), list(tree.keys()))

    def test_reads_tag_values_correctly(self):
        for directory, expected_result in self.get_next_test_directory():
            tree = db.browse(directory)

            test_filename = os.path.join(directory, expected_result['Test Filename'])
            for tag_name in ('Spacing Between Slices', 'Window Width', 'Patient\'s Age', 'Series Instance UID'):
                self.assertEqual(str(tree[test_filename][tag_name]), str(expected_result[tag_name]),
                                 msg="%s tag value incorrect" % tag_name)

    def test_can_filter_by_taglist(self):
        for directory, expected_result in self.get_next_test_directory():
            selected_tags = expected_result['Filter By Tags']
            tree = db.browse(directory, select_tags=selected_tags)
            test_filename = os.path.join(directory, expected_result['Test Filename'])

            available_tag_names = set(tree[test_filename].keys())
            expected_tag_names = set(selected_tags)

            self.assertSetEqual(available_tag_names, expected_tag_names)



if __name__ == "__main__":
    unittest.main(warnings='ignore')
