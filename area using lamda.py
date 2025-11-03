def calculate_square_area(side):
    return side * side

def calculate_triangle_area(base, height):
    return 0.5 * base * height

sqs = int(input("Enter the side of the square: "))

print("Enter the base and height of the triangle:")
ht = int(input("Height: "))
bs = int(input("Base: "))

print("Enter the length and breadth of the rectangle:")
l = int(input("Length: "))
b = int(input("Breadth: "))

square_area = calculate_square_area(sqs)
print("Area of the square:", square_area)

triangle_area = calculate_triangle_area(bs, ht)
print("Area of the triangle:", triangle_area)
