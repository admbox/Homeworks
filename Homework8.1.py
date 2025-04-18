def add_one(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    number += 1
    return [int(d) for d in str(number)]

user_input = input("please input digits (for example 1,2,3,4): ")

digits = [int(d.strip()) for d in user_input.split(",")]

result = add_one(digits)

print("Result:", result)