import re

def first_word(text: str) -> str:
    words = re.findall(r"\b[\w']+\b", text)
    return words[0] if words else ''

user_input = input("Please input words list: ")

result = first_word(user_input)
print(f"First word: {result}")