my_list = [0, 9, 5, 0, 4, 0, 8]

non_zeros = [x for x in my_list if x != 0]

zeros = my_list.count(0)

non_zeros.extend([0] * zeros)

print(non_zeros)