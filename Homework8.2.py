def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

user_input = input("Please input a string to check for palindrome: ")

if is_palindrome(user_input):
    print("True")
else:
    print("False")