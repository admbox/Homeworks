import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}) = {self.area()}"

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __add__(self, other):
        total_area = self.area() + other.area()
        side = math.sqrt(total_area)
        return Rectangle(round(side, 2), round(total_area / side, 2))

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("Multiplication is only possible by a number")
        new_area = self.area() * n
        side = math.sqrt(new_area)
        return Rectangle(round(side, 2), round(new_area / side, 2))

    def __rmul__(self, n):
        return self.__mul__(n)

def get_rectangle_input(index):
    print(f"Entering a rectangle {index}:")
    width = float(input("  Width: "))
    height = float(input("  Height: "))
    return Rectangle(width, height)

def main():
    print("=== Rectangle ===")
    r1 = get_rectangle_input(1)
    r2 = get_rectangle_input(2)

    print("\nFirst rectangle:", r1)
    print("Second rectangle:", r2)

    print("\nComparison:")
    if r1 == r2:
        print("Rectangles are equal in area")
    elif r1 > r2:
        print("The first rectangle is larger in area")
    else:
        print("The second rectangle is larger in area")

    r3 = r1 + r2
    print("\nSum of rectangles:", r3)

    # Множення
    factor = float(input("\nEnter the multiplier for the first rectangle: "))
    r4 = r1 * factor
    print("Multiplication result:", r4)

if __name__ == "__main__":
    main()