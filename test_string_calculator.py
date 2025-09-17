import unittest
from string_calculator import add_number_string as add

class TestStringCalculator(unittest.TestCase):
    def test_number_add(self):
        self.assertEqual(add(""),0) # test case 1 - takes empty string, return 0
        self.assertEqual(add("4"),4)  # test case 2 - takes single number string, returns same number
         # for simplicity delimiter used for these cases is only ','.
        self.assertEqual(add("3,4"),7)  # test case 3 - takes two number string, returns addition of it
        self.assertEqual(add("1,2,3"),6)    # test case 4 - takes three numbers string, returns addition of it
        self.assertEqual(add("1,2,3,4,5,6,7,8,9"),45) # testing with any number of numbers present in string

    def test_new_lines(self):
        self.assertEqual(add("1,2\n3"),6) # test case 1 - new line inside string
        self.assertEqual(add("1,2\n\n3"),6)    # test case 2 - multiple new lines inside string

if __name__ == "__main__":
    unittest.main()