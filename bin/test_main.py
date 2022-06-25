from testify import *
from io import StringIO
from unittest.mock import patch
import unittest
import main

class TestMain(TestCase):
    """docstring for TestMain."""
    def test_col(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.col(0, 1)
            assert_equal(captured.getvalue(), "1,\n1,1,\n")

    def test_row(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.row(0, 1, 1)
            assert_equal(captured.getvalue(), "1,1,")

if __name__ == '__main__':
    run()
