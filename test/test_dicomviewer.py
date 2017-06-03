import unittest
from dicomviewer import ConsoleViewer
from dicomviewer import FileViewer
from dicomviewer import CSVViewer
import os
from contextlib import contextmanager
from io import StringIO
import sys


@contextmanager
def captured_output():
    """
    Diverts console output so that it can be validated.
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class ITestCase(unittest.TestCase):
    def get_next_test_directory(self):
        curdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../dicombrowser/testdirectory/')
        expected_results = {os.path.join(curdir, 'slice'):
                                {'Patient\'s Name': 'Anonymized', 'Number Of Files': 1,
                                 'Test Filename': 'Anonymized20170603.dcm',
                                 'Spacing Between Slices': 0.5,
                                 'Window Width': ['00350', '00350'],
                                 'Series Instance UID': '1.2.826.0.1.3680043.8.1055.1.20111102150758591.96842950.07877442',
                                 'Patient\'s Age': '000Y',
                                 'Filter By Tags': ['Patient\'s Name', 'Patient\'s Age', 'Spacing Between Slices']},
                            os.path.join(curdir, 'series'):
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


class TestConsoleViewer(ITestCase):
    def test_can_display_results(self):
        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            with captured_output() as (out, err):
                viewer = ConsoleViewer(directory, tags)
                viewer.draw()
                self.assertIn('Patient\'s Name', out.getvalue())
                self.assertIn('Patient\'s Age', out.getvalue())
                self.assertNotIn('Referring Physician\'s Name', out.getvalue())
                self.assertNotIn('Series Instance UID', out.getvalue())


class TestFileViewer(ITestCase):
    def test_can_write_to_file(self):
        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            tempfilename = 'test_fileviewer.log'
            with open(tempfilename, 'w') as tf:
                viewer = FileViewer(tf, directory, tags)
                viewer.draw()

            with open(tempfilename, 'r') as tf:
                contents = tf.read()
                self.assertIn('Patient\'s Name', contents)
                self.assertIn('Patient\'s Age', contents)
                self.assertNotIn('Referring Physician\'s Name', contents)
                self.assertNotIn('Series Instance UID', contents)

            os.remove(tempfilename)


class TestCSVViewer(ITestCase):
    def test_can_write_to_csv(self):
        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            tempfilename = 'test_csvviewer.log'
            with open(tempfilename, 'w') as tf:
                viewer = CSVViewer(tf, directory, tags)
                viewer.draw()

            with open(tempfilename, 'r') as tf:
                contents = tf.read()
                self.assertIn('Patient\'s Name', contents)
                self.assertIn('Patient\'s Age', contents)
                self.assertNotIn('Referring Physician\'s Name', contents)
                self.assertNotIn('Series Instance UID', contents)

            os.remove(tempfilename)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
