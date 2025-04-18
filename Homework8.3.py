def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

user_input = input("Please input a digits (for example: 1,2,2,3,3): ")

numbers = [int(x.strip()) for x in user_input.split(",")]

unique = find_unique_value(numbers)

print("Unique_digit:", unique)