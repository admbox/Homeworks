number = int(input("Please input 4-digit number: "))

first_digit, remainder = divmod(number, 1000)
second_digit, remainder = divmod(remainder, 100)
third_digit, fourth = divmod(remainder, 10)


print(first_digit)
print(second_digit)
print(third_digit)
print(fourth)