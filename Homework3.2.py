def shift_last_to_first(lst):
    if len(lst) > 1:
        lst = [lst[-1]] + lst[:-1]
    return lst

print(shift_last_to_first([1, 2, 3, 4, 5]))