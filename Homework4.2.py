my_list = [0, 1, 2, 3, 4, 5]

if my_list:

    even_index_sum = sum(my_list[i] for i in range(0, len(my_list), 2))

    result = even_index_sum * my_list[-1]
else:
    result = 0

print(result)