import string

input_string = input("Please input a string: ")

cleaned_string = ''.join(char for char in input_string if char not in string.punctuation and char != ' ')

words = cleaned_string.split()

hashtag = '#' + ''.join(word.capitalize() for word in words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)