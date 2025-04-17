def correct_sentence(sentence: str) -> str:

    sentence = sentence[0].upper() + sentence[1:]

    if not sentence.endswith('.'):
        sentence += '.'

    return sentence
user_input = input("Please input senteces: ")
print(correct_sentence(user_input))
