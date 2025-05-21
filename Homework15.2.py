import math

class ImproperFractionError(ValueError):
    pass

class ProperFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be zero")
        if abs(numerator) >= abs(denominator):
            raise ImproperFractionError("This is an improper fraction. The numerator must be less than the denominator")

        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator

    def __eq__(self, other):
        return self.to_float() == other.to_float()

    def __lt__(self, other):
        return self.to_float() < other.to_float()

    def __le__(self, other):
        return self.to_float() <= other.to_float()

    def __gt__(self, other):
        return self.to_float() > other.to_float()

    def __ge__(self, other):
        return self.to_float() >= other.to_float()

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return ProperFraction._from_raw(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return ProperFraction._from_raw(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return ProperFraction._from_raw(num, den)

    @staticmethod
    def _from_raw(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        if abs(numerator) >= abs(denominator):
            raise ImproperFractionError("The result is an improper fraction")
        return ProperFraction(numerator, denominator)

def read_fraction(index):
    while True:
        try:
            print(f"\nEnter the correct fraction. #{index}:")
            numerator = int(input("  Numerator: "))
            denominator = int(input("  Denominator: "))
            return ProperFraction(numerator, denominator)
        except (ValueError, ZeroDivisionError, ImproperFractionError) as e:
            print("error:", e, "\nTry again..")

def main():
    print("=== Working with proper fractions ===")
    a = read_fraction(1)
    b = read_fraction(2)

    print("\n--- Entered fractions ---")
    print("A =", a)
    print("B =", b)

    # Арифметика
    try:
        print("\n--- Arithmetic operations ---")
        print("A + B =", a + b)
    except ImproperFractionError as e:
        print("A + B: error —", e)

    try:
        print("A - B =", a - b)
    except ImproperFractionError as e:
        print("A - B: error —", e)

    try:
        print("A * B =", a * b)
    except ImproperFractionError as e:
        print("A * B: error —", e)

    print("\n--- Comparison ---")
    print("A == B:", a == b)
    print("A < B:", a < b)
    print("A > B:", a > b)

if __name__ == "__main__":
    main()
