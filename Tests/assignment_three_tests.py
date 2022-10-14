import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(150, assignment_three.totalArea(4, 3, 9))  # If the width is 4, length is 3, and height is 9, the total surface area will be 150


if __name__ == '__main__':
    unittest.main()
