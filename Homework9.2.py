def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)

input_numbers = input("Please input digits: ")

if input_numbers.strip():
    numbers = list(map(float, input_numbers.split()))
    result = difference(*numbers)
else:
    result = difference()

print(f"different: {result}")