import unittest
from string_calculator import add_number_string as add

class TestStringCalculator(unittest.TestCase):
    def test_string_cal(self):
        self.assertEqual(add(""),0) # test case 1 - takes empty string, return 0


if __name__ == "__main__":
    unittest.main()