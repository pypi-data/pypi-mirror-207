import unittest
from square_vilavr.square.square_formula import square_formula

class TestSquareFormula(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(square_formula(2, 3), 25)
        self.assertEqual(square_formula(5, 10), 225)
        self.assertEqual(square_formula(7, 2), 81)

    def test_negative_numbers(self):
        self.assertEqual(square_formula(-2, -3), 25)
        self.assertEqual(square_formula(-5, -10), 225)
        self.assertEqual(square_formula(-7, -2), 81)

    def test_mixed_numbers(self):
        self.assertEqual(square_formula(2, -3), 1)
        self.assertEqual(square_formula(-5, 10), 25)
        self.assertEqual(square_formula(-7, 2), 25)

if __name__ == '__main__':
    unittest.main()