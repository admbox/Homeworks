lst = [1, 2, 3, 4, 5]

if len(lst) == 0:
    result = [[], []]
else:
    middle = (len(lst) + 1) // 2
    result = [lst[:middle], lst[middle:]]

print(result)