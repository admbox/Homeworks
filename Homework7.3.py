def second_index(text: str, target: str) -> int | None:
    first = text.find(target)
    if first == -1:
        return None

    second = text.find(target, first + len(target))
    if second == -1:
        return None

    return second

text_input = input("Please input search string: ")
target_input = input("Please input substring we are looking for: ")

result = second_index(text_input, target_input)

if result is not None:
    print(f"Second occurrence index: {result}")
else:
    print("The second entry was not found.")