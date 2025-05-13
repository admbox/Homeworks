def is_even(n):
    return (n & 1) == 0
try:
    user_input = int(input("Enter a whole number: "))
    result = is_even(user_input)
    print("Is the number even?" , result)
except ValueError:
    print("Error: Invalid integer entered")