lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(lst) > 1:
    last_element = lst.pop()
    lst.insert(0, last_element)

print(lst)