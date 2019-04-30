import unittest
from calculator import Calculator

class TestPython(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_calc(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
    def test_calc_returns_error(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
if __name__ == '__main__':
    unittest.main()
