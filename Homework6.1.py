import string

user_input = input("Please input two letters separated by a hyphen:")

start, end = user_input.split("-")

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

result = letters[start_index:end_index + 1]
print(result)