"""
Unit tests for triangle classification program.
"""

import unittest
from triangle import classify_triangle


class TestTriangleClassification(unittest.TestCase):
    """Test cases for classify_triangle function."""

    def test_equilateral(self):
        """Test equilateral triangle."""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        """Test isosceles triangle."""
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")

    def test_scalene(self):
        """Test scalene triangle."""
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_right_triangle(self):
        """Test right triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_isosceles_right(self):
        """Test invalid isosceles right triangle."""
        self.assertEqual(classify_triangle(1, 1, 2), "Not a triangle")

    def test_invalid_triangle(self):
        """Test triangle inequality violation."""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_negative_values(self):
        """Test negative side values."""
        self.assertEqual(classify_triangle(-1, 2, 3), "Not a triangle")

    def test_zero_value(self):
        """Test zero side value."""
        self.assertEqual(classify_triangle(0, 2, 3), "Not a triangle")


if __name__ == "__main__":
    unittest.main()