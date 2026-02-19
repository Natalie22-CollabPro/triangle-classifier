"""
Triangle classification module.
Determines the type of triangle based on side lengths.
"""


def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on three side lengths.

    Returns:
        - "Equilateral"
        - "Isosceles"
        - "Scalene"
        - "Right" appended if it is a right triangle
        - "Not a triangle" if invalid
    """

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Not a triangle"

    if side_a + side_b <= side_c or \
       side_a + side_c <= side_b or \
       side_b + side_c <= side_a:
        return "Not a triangle"

    sides = sorted([side_a, side_b, side_c])
    side_a, side_b, side_c = sides

    if side_a == side_b == side_c:
        triangle_type = "Equilateral"
    elif side_b in (side_a, side_c):
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if side_a**2 + side_b**2 == side_c**2:
        triangle_type += " Right"

    return triangle_type


if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(2, 2, 2))
    print(classify_triangle(2, 2, 3))
    print(classify_triangle(3, 4, 6)) 