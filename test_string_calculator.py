import unittest
from string_calculator import add_number_string as add

class TestStringCalculator(unittest.TestCase):
    def test_string_cal(self):
        self.assertEqual(add(""),0) # test case 1 - takes empty string, return 0
        self.assertEqual(add("4"),4)  # test case 2 - takes single number string, returns same number
        self.assertEqual(add("3,4"),7)  ## test case 3 - takes two number string, returns addition of it


if __name__ == "__main__":
    unittest.main()