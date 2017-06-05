import unittest
from dicomviewer import Model
from dicomviewer import ConsoleViewModel, ConsoleView
from dicomviewer import FileViewModel, FileView
from dicomviewer import CSVView, CSVViewModel
from dicomviewer import WebView, WebViewModel
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
        curdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdirectory/')
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
            tags = ['Patient\'s Name', 'Patient\'s Age', 'Spacing Between Slices']

            with captured_output() as (out, err):
                # MVVM pattern
                model = Model(directory, tags)  # contains the model
                view = ConsoleView()  # pointer to the visual widget (command line)
                viewmodel = ConsoleViewModel(model, view)  # updates the view with the model's contents
                view.update()

                contents = out.getvalue()
                self.assertNotIn('Referring Physician\'s Name', contents)
                self.assertNotIn('Series Instance UID', contents)
                for tag in tags:
                    self.assertIn(tag, contents)
                    self.assertIn(str(expected_result[tag]), contents)


class TestFileViewer(ITestCase):
    def test_can_write_to_file(self):
        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            tempfilename = 'test_fileviewer.log'
            with open(tempfilename, 'w') as tf:
                # MVVM pattern
                model = Model(directory, tags)  # contains the model
                view = FileView(tf)  # pointer to the visual widget (command line)
                viewmodel = FileViewModel(model, view)  # updates the view with the model's contents
                view.update()

            with open(tempfilename, 'r') as tf:
                contents = tf.read()
                self.assertNotIn('Referring Physician\'s Name', contents)
                self.assertNotIn('Series Instance UID', contents)
                for tag in tags:
                    self.assertIn(tag, contents)
                    self.assertIn(str(expected_result[tag]), contents)

            os.remove(tempfilename)


class TestCSVViewer(ITestCase):
    def test_can_write_to_csv(self):
        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            tempfilename = 'test_csvviewer.log'
            with open(tempfilename, 'w') as tf:
                # MVVM pattern
                model = Model(directory, tags)  # contains the model
                view = CSVView(tf)  # pointer to the visual widget (command line)
                viewmodel = CSVViewModel(model, view)  # updates the view with the model's contents
                view.update()

            with open(tempfilename, 'r') as tf:
                contents = tf.read()
                self.assertNotIn('Referring Physician\'s Name', contents)
                self.assertNotIn('Series Instance UID', contents)
                for tag in tags:
                    self.assertIn(tag, contents)
                    self.assertIn(str(expected_result[tag]), contents)

            os.remove(tempfilename)


class TestWebViewer(ITestCase):
    def test_can_connect_client_to_server(self):

        for directory, expected_result in self.get_next_test_directory():
            tags = ['Patient\'s Name', 'Patient\'s Age']

            model = Model(directory, tags)  # contains the model
            view = WebView()  # pointer to the visual widget (command line)
            viewmodel = WebViewModel(model, view)  # updates the view with the model's contents
            view.update()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
