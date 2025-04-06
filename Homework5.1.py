import string
import keyword

name = input("Please enter your name: ")

if (name[0].isdigit() or
    any(char.isupper() for char in name) or
    any(char in string.punctuation.replace('_', '') for char in name) or
    name in keyword.kwlist or
    name.count('_') > 1):
    print(False)
else:
    print(True)