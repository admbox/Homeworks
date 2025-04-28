def is_even(number: int) -> bool:
    return number % 2 == 0

num = int(input("Please input digit: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} isn't even.")