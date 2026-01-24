def classify_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0: 
        return "Not a triangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    

    sides = sorted([a, b, c])
    a, b, c = sides

    triangle_type = "" 

    if a == b == c: 
        triangle_type = "Equilateral" 
    elif a==b or b==c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene" 

    if a**2 + b**2 == c**2:
        triangle_type += " Right"

    return triangle_type 

if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(2, 2, 2))
    print(classify_triangle(2, 2, 3))
    print(classify_triangle(3, 4, 6)) 