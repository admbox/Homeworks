def popular_words(text: str, words: list) -> dict:
    text_words = text.lower().split()
    return {word: text_words.count(word) for word in words}

text_input = input("please input words:\n")

words_input = input("Enter your search terms separated by commas (no spaces):\n")
words_list = words_input.lower().split(',')
result = popular_words(text_input, words_list)

print("Result:")
for word, count in result.items():
    print(f"{word}: {count}")