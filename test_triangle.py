import unittest
from triangle import classify_triangle

class TestTriangleClassification(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_isosceles_right(self):
        self.assertEqual(classify_triangle(1, 1, 2), "Not a triangle")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_negative_values(self):
        self.assertEqual(classify_triangle(-1, 2, 3), "Not a triangle")

    def test_zero_value(self):
        self.assertEqual(classify_triangle(0, 2, 3), "Not a triangle")


if __name__ == "__main__":
    unittest.main()
