import unittest
import dicombrowser as db


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

if __name__ == "__main__":
    unittest.main()
